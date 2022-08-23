from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def homePage(request):
    
    return render(request,"index.html")

def careers(request):
    return render(request,"careerspage.html")

def indexpage1(request):
    return render(request,"indexpage1.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"footer.html") 

def userform(request):
    finalans=0
    data={}
    try:
        if request.method=="POST":

            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }

            return  HttpResponseRedirect('/careers/')

    except:
        pass  

    return render(request,"userform.html",data)
    

def aboutus(request):
    return HttpResponse(" <h1><b>welcome to mysite</h1>")

def courses(request):
    return HttpResponse("welcome to mysite1") 

def courseDetails(request,courseid):
    return HttpResponse(courseid)