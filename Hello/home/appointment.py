import smtplib
from datetime import datetime, date,timedelta


def send_mail(name,age,email,sex,symptom,diseases):
    server = smtplib.SMTP('smtp.gmail.com', 587) #server estabilishment
    server.ehlo()
    server.starttls()
    server.ehlo()

    # with open('password.txt', 'r') as x:    # password stored in file in order to not violate the code
    #     password = x.read()
    password="9494708899"
    server.login('hapr.service@gmail.com', password) # login

    subject = "Appointment Booking confirmation" #subject

    # with open('body.txt', 'r') as n: #text template for the body
    #     body = n.read()
    if age=="0":
        age="Select Age Category"
    elif age=="1":
        age="0 - 28 d (newborn)"
    elif age=="2":
        age="29 d - 1 yr (infant)"
    elif age=="3":
        age="1 - 5 yrs (younger child)"
    elif age=="4":
        age="6 - 12 yrs  (older child)"
    elif age=="5":
        age="13 - 16 yrs (adolescent)"
    elif age=="6":
        age="17 - 29 yrs (young adult)"
    elif age=="7":
        age="30 - 39 yrs (adult)"
    elif age=="8":
        age="40 - 49 yrs (adult)"
    elif age=="9":
        age="50 - 64 yrs (adult)"
    elif age=="10":
        age="65 yrs - over (senior)"
    ssex="".join(sex)
    sdiseases=', '.join(diseases)
    appdate=date.today()+timedelta(days=1)
    ssymptom=', '.join(symptom)
    body=f"Dear {name},\n\nThis is to inform you that as per your arising symptoms, you have asked us to book an appointment so, here is the confirmation mail for the same.\nYour appointment with XYZ hospital has been booked successfully.The details for the same is attached below.\nDetails of Appoints as follows:\nDate and Time of Booking: {datetime.today()}\nAppointment Date: {appdate}\nAppointment Time: 6:00 pm\nDoctor Name: Dr.Vikas Panthi\nVenue: XYZ hospitalLocation:- XYZ, #1-60/10, ABC Nagar, Yunlanga, Volanga, Andikandra Presist 531167\nPatient Name: {name}\nAge: {age}\nPatient Sex: {ssex}\nPatient Symptoms: {ssymptom}\nPossible disases according to the provided symptoms: {sdiseases}.\n\n\nThank You\nWith regards,Team HAPR"
    msg = f"subject: {subject} \n\n\n {body}"

    server.sendmail(
        'hapr.service@gmail.com', #sending a copy to self
        email, #to
        msg
    )
    print('Message is sent succesfully!') # inorder to know whether the mail is sent or not
    return 1
#send_mail("Piyush","karmhepiyush@gmail.com","Male","Stomach Pain","Gas")