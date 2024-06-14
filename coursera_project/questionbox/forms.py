from django import forms
from .models import Question,Answer,Choices
from .models import User as CUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields='__all__'

class ChoiceForm(forms.ModelForm):
    class Meta:
        model=Choices
        fields='__all__'        


class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields='__all__'         


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        
class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=100,required=True) 
    
    class Meta:
        model=  CUser 
        fields=['username','first_name','last_name','email','password1','password2']
        
