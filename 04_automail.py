import yagmail
import datetime

print("Sending Email please wait")
yag = yagmail.SMTP("vinayaksutar782001@gmail.com", "dlfvawifeswtuucv")

today = datetime.date.today()
contents = [
    "This month Attendace Excel ",
    "You can find a file attached.",
    "attendance/" + str(today.month) + str(today.year) + ".xlsx",
]
yag.send("vinayaksutar782001@gmail.com", "subject", contents)
print("Email Send Successfully")
