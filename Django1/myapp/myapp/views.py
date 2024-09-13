from django.http import HttpResponse 
import datetime
from django.shortcuts import render

def home(request):
    #POST is used to send data and it is secured and GET is used to fetch the data
    isActive=True
    if request.method=='POST':
        check=request.POST.get('check')
        #post show error if not not check checkbox or dont write anything in input box but get will return none if you submit blank
        print(check)
        if check is None: isActive=False
        else: isActive=True

    date=datetime.datetime.now()

    #print("This is test function")
    #return HttpResponse("<h1>Hello Tested</h1>" + str(date))

    #isActive=True 
    #if it is false the the dynamic thing will not show to web page

    name="SAHIL LOKHANDE"
    list_of_program=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print pascals triangle'
    ]

    student={
        'student_name':"Rahul",
        'student_college':"XYZ",
        'student_city':"INDIA"
    }

    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student_data':student
    }

    return render(request, "home.html", data)

def about(request):
    #return HttpResponse("<h1>This is about Page</h1>")
    return render(request, "about.html", {})

def services(request):
    #return HttpResponse("<h1>This is Services Page</h1>")
    return render(request, "services.html", {})