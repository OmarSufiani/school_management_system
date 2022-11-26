from django.db import models

# Create your models here.
class Unit(models.Model):
    name=models.CharField(max_length=50, null=True)
    code=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    genderType=(
               ('Male','Male'),
               ('Female','Female'),
               )
    name=models.CharField(max_length=50, null=False)
    regNo=models.CharField(max_length=50)
    gender=models.CharField(max_length=50, choices = genderType)
    units=models.ManyToManyField(Unit)

    def __str__(self):
        return self.name        

class Teacher(models.Model):
    genderType=(
               ('Male','Male'),
               ('Female','Female'),
               )
    name=models.CharField(max_length=50)
    tscNo=models.CharField(max_length=50)
    gender=models.CharField(max_length=50, choices = genderType)
    units=models.ManyToManyField(Unit)

    def __str__(self):
        return self.name  


class Mark(models.Model):
    students=models.ForeignKey(Student, on_delete= models.CASCADE)
    units=models.ForeignKey(Unit, on_delete= models.CASCADE, null=True)
    cat=models.IntegerField()
    exam=models.IntegerField()
    

    def __str__(self):
        return self.students.name            