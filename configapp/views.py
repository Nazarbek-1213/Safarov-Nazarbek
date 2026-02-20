from django.shortcuts import render
from .models import *

def home(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile,
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "education": Education.objects.all(),
    }
    return render(request, "portfolio/home.html", context)