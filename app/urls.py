from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="home"),
    path('<id>/delete', views.delete_view, name="delete"),
    path('<id>/update', views.edit_view, name="update"),
    path('<id>/select', views.select_view, name="read"),
]
