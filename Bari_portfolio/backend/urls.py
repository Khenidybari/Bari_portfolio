from django.urls import path
from .views import *

app_name = "backend"

urlpatterns = [
    path('login/', signin, name="signin"),
    path('logout/', signout, name="signout"),
    path('changepass/', forgetpass, name="forgetpass")]