from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeCreateView.as_view(), name='home'),
    path('set_languages', views.set_languages, name='set_language'),
]
