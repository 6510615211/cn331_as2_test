from django.shortcuts import render
from django.http import HttpResponse
from registprogram.models import Subject

# Create your views here.
def index(request):
    return render(request, "index.html")

def course(request):
    subjects = Subject.objects.all()
    return render(request, "course.html", {"subjects": subjects})

