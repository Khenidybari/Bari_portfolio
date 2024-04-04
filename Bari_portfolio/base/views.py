from backend.forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    user = User.objects.get(id=1)
    project = Project.objects.all()
    context = {'project':project, 'user':user}
    return render(request, 'home.html',context)
    
@login_required(login_url="/auth/login")
def cms(request):
    user = User.objects.get(username='admin')
    print(user.user_skill.all())
    context = {'user_data': user}
    return render(request, 'cms.html', context)


#user
def personal(request):
    user=User.objects.get(username='admin')
    if request.method == 'POST': 
        form = Personalinfoform(request.POST,request.FILES,instance=user)
        if form.is_valid():
            try: 
                form.save()
                return redirect('base:personal')
            except Exception as e: 
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving. Please try again."}
        else:
            print(form.errors)
    else:
        form = Personalinfoform()

    context = {'form': form}
    return render(request, 'cms.html',context)


#skills
def skills(request):
     if request.method == 'POST': 
        form = Skillform(request.POST,request.FILES)
        if form.is_valid():
          
            try: 
                instance = form.save(commit=False)
                instance.user=User.objects.get(username='admin')
                instance.save()
                return redirect('base:cms')
            except Exception as e: 
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving. Please try again."}
        else:
            print(form.errors)
     else:
        form = Skillform()

     context = {'form': form}
     return render(request, 'cms.html')


def updateskill(request):
   if request.method == 'POST': 
        if request.POST.get('skillid'):
            skill = Skill.objects.get(id=request.POST.get('skillid'))
            form = Skillform(request.POST,request.FILES,instance = skill)
            if form.is_valid():
            
                try: 
                    form.save()
                    return redirect('base:cms')
                except Exception as e: 
                    print(f"Error:{e}")
                    context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
            else:
                print(form.errors)
        else:
            form = Skillform()

   context = {'form': form}
   return render(request, 'cms.html')


def deleteskill(request):

    if request.method == "POST":
        skillid=request.POST.get('skillid')
        if skillid: 
            try:
                skill = Skill.objects.get(id=skillid)
                skill.delete()
                return redirect('base:cms')
            except Exception as e:
                print(request,f"an error occured:{e}")
    return redirect('base:cms')


#projects
def projects(request):
    if request.method == 'POST': 
        form = Projectform(request.POST,request.FILES)
        if form.is_valid():
          
            try: 
                instance = form.save(commit=False)
                instance.user=User.objects.get(username='admin')
                instance.save()
                return redirect('base:cms')
            except Exception as e: 
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
        else:
            print(form.errors)
    else:
        form = Projectform()

    context = {'form': form}
    return render(request, 'cms.html',context)


def updateproject(request):
   if request.method == 'POST': 
        project = Project.objects.get(request.POST.get('project_id'))
        form = Projectform(request.POST,request.FILES,instance = project)
        if form.is_valid():
          
            try: 
                form.save()
                return redirect('base:cms')
            except Exception as e: 
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
        else:
            print(form.errors)
   else:
        form = Projectform()

   context = {'form': form}
   return render(request, 'cms.html')


def deleteproject(request):
    if request.method == 'POST': 
        project = Project.objects.get(request.POST.get('project_id'))
          
        try: 
            project.delete()
            return redirect('base:cms')
        except Exception as e: 
            print(f"Error:{e}")
            context = {'error_message': "There was a problem saving the project. Please try again."}
        
    return render(request, 'cms.html')