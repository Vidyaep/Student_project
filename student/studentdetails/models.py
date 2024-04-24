from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    department=models.CharField(max_length=50)
    year=models.IntegerField()

    def __str__(self):
        return self.department
    
class Student(models.Model):
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    Gender=(('male','Male'),('female','Female'),('others','Others'))
    gender=models.CharField(max_length=50,choices=Gender,default=1)
    
    def __str__(self):
        return self.name