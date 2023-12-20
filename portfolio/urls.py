from portfolio.views import index, convert_markdown_to_pdf, download_curriculo
from django.urls import path

urlpatterns = [
    path("", index, name="homepage"),
    path("build-curricullum", convert_markdown_to_pdf, name="build"),
    path("curriculum/download", download_curriculo, name="download"),
]
