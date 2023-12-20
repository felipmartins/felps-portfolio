import os

from django.http import Http404
from django.shortcuts import render
from portfolio.models import (
    Skill,
    Project,
    Education,
    Experience,
    Recommendation,
)
from mdpdf.converter import Converter
from django.http import HttpResponse


def index(request):
    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "educations": Education.objects.all().order_by("-id"),
        "experiences": Experience.objects.all().order_by("-id"),
        "recommendations": Recommendation.objects.all(),
    }
    return render(request, "index.html", context)


def convert_markdown_to_pdf(request):
    output_file = "staticfiles/curriculo.pdf"
    markdown_file = "portfolio/curriculo.md"

    Converter(output_file).convert([markdown_file])

    return HttpResponse(
        f"Curriculo gerado em {output_file}.", content_type="text/plain"
    )


def download_curriculo(request):
    file_path = "staticfiles/curriculo.pdf"
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            res = HttpResponse(fh.read(), content_type="application/pdf")
            res["Content-Disposition"] = "attachment; filename=cv_felps.pdf"
            return res

    raise Http404
