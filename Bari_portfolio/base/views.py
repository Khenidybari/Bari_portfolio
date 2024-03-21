from backend.forms import *
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def cms(request):
    return render(request, 'cms.html')

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
                context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
        else:
            print(form.errors)
    else:
        form = Personalinfoform()

    context = {'form': form}
    return render(request, 'cms.html',context)

def skills(request):
     if request.method == 'POST': 
        form = Skillform(request.POST,request.FILES)
        if form.is_valid():
          
            try: 
                instance = form.save(commit=False)
                instance.user=User.objects.get(username='admin')
                instance.save()
                return redirect('base:skills')
            except Exception as e: 
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
        else:
            print(form.errors)
     else:
        form = Skillform()

     context = {'form': form}
     return render(request, 'cms.html')

def projects(request):
    if request.method == 'POST': 
        form = Projectform(request.POST,request.FILES)
        if form.is_valid():
          
            try: 
                instance = form.save(commit=False)
                instance.user=User.objects.get(username='admin')
                instance.save()
                return redirect('base:projects')
            except Exception as e: 
                print(f"Error:{e}")
                context = {'form': form, 'error_message': "There was a problem saving the skill. Please try again."}
        else:
            print(form.errors)
    else:
        form = Projectform()

    context = {'form': form}
    return render(request, 'cms.html')