from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import csv
import io
import os

app = Flask(__name__)
CORS(app)

MDB_FILE   = r"D:\SYSTEMPOS2\maindata.mdb"
MDB_EXPORT = r"D:\mdbtools\mdb-export.exe"   # path ที่แตก mdbtools ไว้


def run_export(table):
    """Export ตารางออกมาเป็น list of dict"""
    result = subprocess.run(
        [MDB_EXPORT, MDB_FILE, table],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    reader = csv.DictReader(io.StringIO(result.stdout))
    return list(reader)


@app.route("/bill/<codebill>", methods=["GET"])
def get_bill(codebill):
    try:
        # ดึงข้อมูลบิลหลัก
        bills = run_export("Totalbill")
        bill  = next((b for b in bills if b.get("codebill","").strip() == codebill.strip()), None)
        if not bill:
            return jsonify({"error": f"ไม่พบบิลเลขที่ {codebill}"}), 404

        # ดึงรายการสินค้า
        items_all = run_export("Dessell")
        items = [
            {
                "desc":  row.get("list", "").strip(),
                "qty":   float(row.get("QtyValue", 1) or 1),
                "price": float(row.get("ListPrice", 0) or 0),
            }
            for row in items_all
            if row.get("NumCode", "").strip() == codebill.strip()
               and row.get("list", "").strip()
        ]

        return jsonify({
            "codebill": bill.get("codebill", "").strip(),
            "date":     bill.get("TDate", "").strip(),
            "total":    float(bill.get("sumbill", 0) or 0),
            "items":    items
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print("Server running at http://0.0.0.0:5000")
    print(f"MDB file : {MDB_FILE}")
    print(f"mdb-export: {MDB_EXPORT}")
    app.run(host="0.0.0.0", port=5000, debug=False)
