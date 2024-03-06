from django.urls import path
from . import viewsGreet

app_name = "hello"
urlpatterns = [
    path('', viewsGreet.index, name="index"),
    path('<str:name>', viewsGreet.greethtml, name="greet")
]