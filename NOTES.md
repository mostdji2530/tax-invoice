# ระบบใบเสร็จรับเงิน — บันทึกโปรเจกต์

## ไฟล์หลัก
- `tax-invoice.html` — ระบบใบเสร็จรับเงิน (Single-file HTML, ใช้งานได้เลยไม่ต้อง server)

## URL
- **GitHub Pages (เปิดใช้งาน):** https://mostdji2530.github.io/tax-invoice/tax-invoice.html
- **GitHub Repo:** https://github.com/mostdji2530/tax-invoice

## Google Sheets
- **Sheet:** https://docs.google.com/spreadsheets/d/1ekAz092beZfiJu0k5SICR6jE4xzyqs-hCm_hH9aQy9k/edit
- **Apps Script URL:** https://script.google.com/macros/s/AKfycbyUx-R7RhH1mc9mWhUBMdPnaBhCICLZjo6FQp5EgoOnmBLaC3qSFKrMYwafm20sm3wLuQ/exec
- ทุกครั้งที่กด **บันทึก** ข้อมูลจะส่งไป Sheet อัตโนมัติ
- คอลัมน์: เลขที่เอกสาร | วันที่ | ชื่อลูกค้า | ที่อยู่ | สาขา | เลขภาษี | รายการสินค้า | ยอดก่อน VAT | VAT | ยอดรวม | บันทึกเมื่อ

## ฟีเจอร์ระบบ
- Run Number อัตโนมัติ (prefix + padding ตั้งค่าได้)
- VAT modes: ราคารวม VAT แล้ว / ไม่คิด VAT (default: ไม่คิด VAT)
- โลโก้บริษัท (ปรับขนาดได้), ลายน้ำเอกสาร
- หมายเหตุ/Remark กำหนดจากหน้าตั้งค่า (แสดงในเอกสารพิมพ์ทุกใบ)
- ประวัติเอกสาร, แก้ไข, Preview, พิมพ์
- บันทึกข้อมูลใน localStorage

## อัปเดต GitHub
```
cd "/Users/oc/Documents/Claude/Projects/แบบ From"
git add tax-invoice.html
git commit -m "update"
git push
```
