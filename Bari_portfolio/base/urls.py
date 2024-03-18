from django.urls import path
from . import views
app_name='base'

urlpatterns = [
    path ('', views.home, name='home'),
    path ('cms/', views.cms, name='cms'),
    path ('personal/', views.personal, name='personal'),
    path ('skills/', views.skills, name='skills'),
    path ('projects/', views.projects, name='projects')
]