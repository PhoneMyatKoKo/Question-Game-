from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as l
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .models import User as CUser
from .forms import *
import random


ans=Answer.objects.all()

# for i in range(len(Question.objects.all())):

#     answer_list.append(ans[i].choice_id.id)
    
# Create your views here.

def home(request):
    return render(request,'questionbox/home.html')

@login_required(login_url='/questionlogin')
def index(request):
    questions_all=list(Question.objects.all())
    if questions_all:
     question=random.sample(questions_all,5)
    question_id=[]
    
    for q in question:
        question_id.append(q.pk)

    request.session['answer_list']=[]
    for i in range(5):
        request.session['answer_list'].append(Answer.objects.get(question_id_id=question[i].pk).choice_id.id)    
        request.session.modified=True
    
   
    
    

    choices=Choices.objects.all()
    select=''

    try:
        select=request.GET['redirect']
        select="Select the answers."
    except:
        select=''    

    context={'questions':question,'choices':choices,'select':select,'answer':request.session.get('answer_list',[]),'q_id':question_id}
    return render(request,'questionbox/index.html',context)

# def get_answerlist(question):
#     for i in range(5):
#         answer_list.append(Answer.objects.get(question_id_id=question[i].pk).pk)
#     return answer_list

def get_answers(ans_list):
    ans=[]
    for i in ans_list:
        ans.append(Choices.objects.get(pk=i))

    return ans    


def check_result(request):
    
    ans_list=request.session.get('answer_list',[])
    if request.method=='POST': 
     
     choice_list=[]
     score=0
     wrong_questions=[]

     for i in range(1,6,1):

        try:
            choice_list.append(int(request.POST[f'choice{i}']))
        except:
            return HttpResponseRedirect(f'{reverse('question:index')}?redirect=select%all')   
    

     for i in range(5):

        if choice_list[i]==ans_list[i]:
            score+=1
        else:
            wrong_questions.append(i+1)
            
     scoreboard=ScoreBoard(user_id=request.user.pk,score=score)  
     scoreboard.save()
     user=CUser.objects.get(pk=request.user.pk)
     user.attempt+=1
     user.save()      

 
     context={'choice':get_answers(choice_list),'answer':get_answers(ans_list),'score':score,'wrong':wrong_questions,'total':5}
     return render(request,'questionbox/results.html',context)
    
    else:
        return HttpResponse("Permission Denied.")
    


def add_question(request):

    if request.method=='GET':
     question_form=QuestionForm()

    else:
        question_form=QuestionForm(request.POST)  
        if question_form.is_valid():
            question_form.save()
            return HttpResponseRedirect(reverse('question:add_choice'))

        

    context={'form':question_form}
    return render(request,'questionbox/add_question.html',context)   


def add_choice(request):

    if request.method=='GET':
     choice_form=ChoiceForm()

    else:
        choice_form=ChoiceForm(request.POST)  
        if choice_form.is_valid():
            choice_form.save()
            return HttpResponseRedirect(reverse('question:add_answer'))

        

    context={'form':choice_form}
    return render(request,'questionbox/add_choice.html',context) 


def add_answer(request):

    if request.method=='GET':
     answer_form=AnswerForm()

    else:
        answer_form=AnswerForm(request.POST)  
        if answer_form.is_valid():
            answer_form.save()
            return HttpResponseRedirect(reverse('question:add_question'))

        

    context={'form':answer_form}
    return render(request,'questionbox/add_answer.html',context)

def profile(request):
    if request.user.is_authenticated:
        user=CUser.objects.get(pk=request.user.pk)
        attempt=user.attempt
        score=user.scoreboard_set.all()
        score_order=user.scoreboard_set.order_by()
        highest_score=0
        if score_order:
            highest_score=score_order[len(score_order)-1]
        context={'attempt':attempt,'score':score,'highest_score':highest_score,'ip':request.META["REMOTE_ADDR"],'middleware':request.kk,}
        return render(request,'questionbox/profile.html',context)
        
    else:
        return HttpResponseRedirect(reverse('question:login'))    
        

def signup(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            l(request,user)
            return HttpResponseRedirect(reverse('question:home'))
        
        else:
            
         context={'form':form}    
         return render(request,'questionbox/signup.html',context)
        
    else:
        form=SignUpForm()
        context={'form':form}    
        return render(request,'questionbox/signup.html',context)
    
    
def login(request):
    if request.method=='GET':
        form=UserForm
        context={'form':form}
        return render(request,'questionbox/login.html',context)
    
    else:
          username = request.POST["username"]
          password = request.POST["password"]
          user = authenticate(request, username=username, password=password)
          if user is not None:
              l(request,user)
              return HttpResponseRedirect(reverse('question:home'))
              
              
          else:
              return HttpResponseRedirect(reverse('question:login'))
    
def Logout(request):
    if request.method=='POST':
     logout(request)
     return redirect('question:home')
    
    
        
        
    
