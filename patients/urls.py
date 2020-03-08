from django.urls import path
from .views import PatientCreateView, PatientUpdateView, PatientDeleteView
from . import views

urlpatterns = [
    path('index', views.index, name='patient-index'),
    path('new/', PatientCreateView.as_view(), name='patient-create'),
    path('<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
]