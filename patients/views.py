from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patients/index.html'
    context_object_name = 'patients'

    def get_queryset(self):
        physician = self.request.user
        return self.model.objects.filter(physician=physician)


class PatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'email']
    success_message = 'Patient added successfully!'

    def form_valid(self, form):
        form.instance.physician = self.request.user
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'email']
    success_message = 'Patient updated successfully!'

    def form_valid(self, form):
        form.instance.physician = self.request.user
        return super().form_valid(form)

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.physician:
            return True
        return False


class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.physician:
            return True
        return False

    def get_success_url(self):
        return reverse('patient-index')