from django.shortcuts import render
from django import forms


class InputForm(forms.Form):
    loginID = forms.CharField(label="email")
    password = forms.CharField(label="password")
    start = forms.DateField(label="start date")
    end = forms.DateField(label="end date")


def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # return HttpResponseRedirect()
        else:
            return render(request,"login.html",{
                "form": form
            })
    return render(request, "login.html", {
        "form": InputForm()
    })