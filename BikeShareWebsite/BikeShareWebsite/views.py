from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
import datetime

class InputForm(forms.Form):
    loginID = forms.CharField(label="email")
    password = forms.CharField(label="password")
    start = forms.DateField(label="start date")
    end = forms.DateField(label="end date")

# Create your views here.
def index(request):
    return render(request,"index.html")

def add(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # return HttpResponseRedirect()
        else:
            return render(request,"greet.html",{
                "form": form
            })
    return render(request, "greet.html", {
        "form": InputForm()
    })