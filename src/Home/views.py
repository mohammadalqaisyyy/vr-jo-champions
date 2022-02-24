from multiprocessing import active_children, context
from tkinter import ACTIVE
from django.shortcuts import render
from .models import *

# Create your views here.
def _home(request):
    cover = home.objects.filter(active=True).last
    Challenge = Challenges.objects.filter(active=True)
    about = about_us.objects.filter(active=True).last
    goal = our_goal.objects.filter(active=True).last
    conta = contact.objects.filter(active=True).last
    Train = training.objects.filter(active=True)
    
    context = {
        'cover':cover,
        'Challenges':Challenge,
        'about_us':about,
        'contact': conta,
        'Trainings':Train,
        'goals':goal
    }

    return render(request,'vr.html',context)

