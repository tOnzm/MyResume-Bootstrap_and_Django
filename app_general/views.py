from django.shortcuts import render ,redirect
from django.http.response import HttpResponse
from app_general.models import Education,Experience,Skills,Languages,MyProject
from .forms import MyImageForm
from django.http import Http404




# Create your views here.


def index(request):
    return render(request,'app_general/index.html')

def about(request):
     return render(request,'app_general/about.html')

def projects(request):
     myproject = MyProject.objects.all()
     return render(request,'app_general/projects.html',{"myproject":myproject})

def contact(request):
     return render(request,'app_general/contact.html')

def resume(request):
    education_data = Education.objects.all()
    experience_data = Experience.objects.all() 
    skills_data = Skills.objects.all()  
    languages = Languages.objects.all()
    
    return render(request,'app_general/resume.html',
                  {"education_data":education_data,
                   "experience_data":experience_data,
                   "skills_data":skills_data,
                   "languages":languages,
                   })

def upload_image(request):
    if request.method == 'POST':
        form = MyImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')  # Redirect to a list view
    else:
        form = MyImageForm()
    return render(request, 'upload_image.html', {'form': form})

