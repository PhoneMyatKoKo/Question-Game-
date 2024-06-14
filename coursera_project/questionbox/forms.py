from django import forms
from .models import Question,Answer,Choices
from django.contrib.auth.models import User


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
        
