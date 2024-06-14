from django.shortcuts import render
from django.http import HttpResponse
from .forms import Person
from .models import Menu
from django.contrib.auth.decorators import login_required
from django.template import loader

question_list=["What is your name?","How old are you?","What is your current status?"]
# Create your views here.
@login_required
def index(request):
    context={"questions":question_list}
    return render(request,'myapp/home.html',context)
 
 
 

@login_required
def test_form(request):
    if request.method=='GET':

     person_form=Person()
     context={"form":person_form}
     return render(request,'myapp/test_form.html',context)
    
    if request.method=='POST':
       person_form=Person(request.POST)
       if person_form.is_valid():
          return HttpResponse("Success")
       else:
          return HttpResponse("fail")
       

@login_required
def coursera(request):
   template=loader.get_template('myapp/coursera.html')
   try :
      menus=Menu.objects.all()
   except Exception:
      menus=None   

   
   context={'title':"Hello World Mf","name":"Phone Myat","list":[0,2,3,4,5],"menu":menus}
   return HttpResponse(template.render(context=context,request=request))






