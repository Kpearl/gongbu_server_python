from django.contrib import admin
from django.urls import path, include
from health import views as health_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_views.index),
    path("users/", include('users.urls'))
]
