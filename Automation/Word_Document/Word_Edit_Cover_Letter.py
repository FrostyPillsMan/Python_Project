from docxtpl import DocxTemplate
from datetime import datetime


doc = DocxTemplate("./Automation/Word_Document/Black_Style_Professional_Sales_Cover_Letter.docx")

name = "Adam"
phone_number = "(+60) 13-5690-4832"
address = "Jalan PJU 5/10, Dataran Sunway, Kota Damansara, 47810 Petaling Jaya, Selangor"
email = "DoomSlayer456@gmail.com"
date = datetime.today().strftime("%d %b, %Y")
person_name = "Cillian Murphy" 
full_name = "Muhammad Adam"


extract_context = {
    "name": name,
    "phone number": phone_number,
    "address": address,
    "email": email,
    "date": date,
    "person_name": person_name,
    "full_name": full_name
}


doc.render(extract_context)
doc.save("Automation/Generate_Doc_Edit.docx")
print("Document successfully generated.")
