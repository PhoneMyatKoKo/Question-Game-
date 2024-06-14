from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=128)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Question No. {self.pk}.{self.question_text}'
    
class Choices(models.Model):
    choice_text=models.CharField(max_length=64)
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.choice_text} related to Question{self.question_id}'   
    

class Answer(models.Model):
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_id=models.ForeignKey(Choices,on_delete=models.CASCADE)

    def __str__(self):
        return f'Answer No.{self.pk}'
  
  
class User(AbstractUser) :
     attempt=models.IntegerField(verbose_name='Number of Attempts',null=True,default=0)
       
class ScoreBoard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField()
           
    def __str__(self) -> str:
        return '{}'.format(self.score)     
           
           
# class Test(models.Model):
#     pass    

