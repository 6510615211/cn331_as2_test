from django.db import models

# Create your models here.
class Subject(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_field = models.CharField(max_length=100) #ภาควิชา
    course_semester = models.IntegerField()
    course_year = models.IntegerField()
    course_amount = models.IntegerField()
    course_status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.course_id +' '+ self.course_name+' ,'+' '+'field : ' + self.course_field+' ,'+' '+'STATUS : '  + self.course_status