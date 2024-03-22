from django.urls import path
from . import views
app_name='base'

urlpatterns = [
    path ('', views.home, name='home'),
    path ('cms/', views.cms, name='cms'),
    path ('personal/', views.personal, name='personal'),
    
    path ('skills/', views.skills, name='skills'),
    path ('updateskill/', views.updateskill, name='updateskill'),
    path ('deleteskill/', views.deleteskill, name='deleteskill'),

    path ('projects/', views.projects, name='projects'),
    path ('updateproject/', views.updateproject, name='updateproject'),
    path ('deleteproject/', views.deleteproject, name='deleteproject')
]