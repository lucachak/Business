from django.contrib import admin
from django.urls import path

from . import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.index, name="index"),
    path("project/<int:project_id>/", v.project_detail, name="project_detail"),
]
