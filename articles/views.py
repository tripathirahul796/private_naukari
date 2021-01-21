from django.shortcuts import render
from .models import ArticleJob
# Create your views here.
def home(request):
    
    job_obj = ArticleJob.objects.all()
    return render(request,'articles/home.html',{'job_list':job_obj})
def details(request,id,title):
    obj = ArticleJob.objects.filter(id=id)
    return render(request,'articles/details.html',{'job_details':obj})
def about_us(request):
    return render(request,'articles/about.html')
def contact_us(request):
    return render(request,'articles/contact.html')