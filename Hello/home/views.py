from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import pandas
import home.backend2
import home.appointment
# Create your views here.
ls=[]
d1=d2={}
disease=[]#done in order
probability=[]#done in order
symptoms=[]
desc=[]
name = ""
email = ""
sex = ""
symptom=[]
age= []
disease_to_send=[]
symptom_to_send=[]
def index(request):
    # pname={'name': ["Piyush Karmhe","Ayushi","Sparsh","Sami","Anna"],
    #         'dis':"Very Talented"}
    #messages.success(request,"This is am Test message")
    return render(request,"index.html")
    #return HttpResponse("Sparsh tu nalla Hai") 
def about(request):
    return render(request,"about.html")
def services(request): 
    global name
    global email
    global sex
    global symptom
    global age
    global disease_to_send
    global symptom_to_send
    l=[]
    csvFile = pandas.read_csv(r'static\\file\\Sev Final.csv')
    for i in csvFile['Symptom']:
        i=i.replace("_","  ")
        i=i.title()
        i=i.strip("\n")
        l.append(i)
    pname={'name': l,
            'dis':"Very Talented"}
    symptom=[]
    if request.method=="POST":
        # for i in l:
        #     name.append(request.POST.get("flexCheckDefault"+i))
        name = request.POST.get("name")
        email = request.POST.get("emailfeild")
        sex = request.POST.getlist("btnradio")
        symptom=request.POST.getlist('checks')
        age= request.POST.get("ageselect")
        symptom_to_send=symptom
        for i in range(len(symptom)):
            symptom[i]=symptom[i].replace("  ","_")
            symptom[i]=symptom[i].lower()
        # print("Request Received")
        # print("Symptoms : ",symptom)
        # print("Result : ")
        # print("Name : ",name)
        # print("Age : ",age)
        # print("Email : ",email)
        # print("Sex : ",sex)
        # print("Symptoms : ",symptom)
        d1,d2,ls=home.backend2.disease_predict(symptom)
        for i in d1:
            probability.append(round(i*100,2))
            disease.append(d1[i])
            desc.append(d2[d1[i]])
        for i in disease:
            k=0
            for j in d2:
                if(i==j):
                    symptoms.append(ls[k])
                k+=1
        # print("Printing Values received at view :")
        # print(disease)
        # #print(probability)
        # #print(d2)
        # #print(t)
        # #print(ls)
        # print(symptoms)
        # #print(desc)
        disease_to_send=disease
    return render(request,"services.html",pname)
def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("dis")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been delivered')
    return render(request,"contact.html")
def result(request):
    global disease#done in order
    global probability#done in order
    global symptoms
    global desc
    global name
    global email
    global sex
    global symptom
    global age
    global disease_to_send
    global symptom_to_send
    l=[]
    for i in symptoms:
        a=[]
        for j in i:
            j=j.replace("_","  ")
            j=j.title()
            a.append(j)
        l+=[a]
    dic={'disease':disease,
         'pro':probability,
         'sym':l,
         'desc':desc,
         'r':''}
    # print("\nPrinting the Values sending to Result :\n")
    # print(disease)
    # print(probability)
    # print(l)
    # print(desc)
    if request.method=="POST":
        l=[]
        for i in symptom_to_send:
            i=i.replace("_","  ")
            i=i.title()
            i=i.strip("\n")
            l.append(i)
        home.appointment.send_mail(name,age,email,sex,l,disease_to_send)
        dic={'disease':disease,
         'pro':probability,
         'sym':l,
         'desc':desc,
         'r':'1'}
    disease=[]#done in order
    probability=[]#done in order
    symptoms=[]
    desc=[]
    return render(request,"result.html",dic)