from django.shortcuts import render
from portfolio.models import Skill, Project, Education, Experience, Recommendation


def index(request):
    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "educations": Education.objects.all().order_by("-id"),
        "experiences": Experience.objects.all().order_by("-id"),
        "recommendations": Recommendation.objects.all(),
    }
    return render(request, "index.html", context)
