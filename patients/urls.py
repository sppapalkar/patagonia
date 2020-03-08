from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PatientCreateView
from . import views

urlpatterns = [
    path('index', views.index, name='patients-index'),
    path('new/', login_required(PatientCreateView.as_view()), name='patients-create')
]