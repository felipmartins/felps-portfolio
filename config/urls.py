from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
    path("tasks/", include("tasks.urls")),
    path("unicorn/", include("django_unicorn.urls")),
]
