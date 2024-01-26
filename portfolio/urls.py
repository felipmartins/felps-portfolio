from portfolio.views import (
    index,
    convert_markdown_to_pdf,
    download_curriculo,
    convert_markdown_to_pdf_en,
    download_curriculo_en,
)
from django.urls import path

urlpatterns = [
    path("", index, name="homepage"),
    path("build-curricullum", convert_markdown_to_pdf, name="build"),
    path("build-curricullum-en", convert_markdown_to_pdf_en, name="build_en"),
    path("curriculum/download", download_curriculo, name="download"),
    path("curriculum/download-en", download_curriculo_en, name="download_en"),
]
