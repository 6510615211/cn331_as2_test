from django.db import models

# Create your models here.
class Subject(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_semester = models.CharField(max_length=100)
    course_year = models.IntegerField()
    course_field = models.CharField(max_length=100)
    course_amount = models.IntegerField()
    course_status = models.CharField(max_length=10)

    def __str__(self):
        return self.course_id +' '+self.course_field+' '+ self.course_name +' '+ str(self.course_semester) +' '+ 'STATUS : ' + self.course_status
    
    
    
