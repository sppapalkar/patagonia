from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Patient


@login_required
def index(request):
    return render(request, 'patients/index.html')


class PatientCreateView(CreateView):
    model = Patient
    fields = ['first_name','last_name', 'email']

    def form_valid(self, form):
        form.instance.physician = self.request.user
        return super().form_valid(form)