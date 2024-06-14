from django import forms
from django.forms import widgets

class Person(forms.Form):
    name=forms.CharField(max_length=100,label="Your name",widget=forms.Textarea(attrs={'class':'form'}))
    age=forms.IntegerField(max_value=10,min_value=5)
    birthday=forms.DateField(widget=widgets.NumberInput({"type":"date"}))
    favorite_color=forms.ChoiceField(choices=(('Red','red'),('Blue','blue'),('Green','green')))
    # file_field=forms.FileField()
    # time_stamp=forms.TimeField()
