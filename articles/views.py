from django.shortcuts import render
from .models import ArticleInfo
# Create your views here.
def home(request):
   # obj = ArticleInfo.objects.get(category=)

    
    return render(request,'articles/home.html')
def details(request):
    return render(request,'articles/details.html')
def about_us(request):
    return render(request,'articles/about.html')
def contact_us(request):
    return render(request,'articles/contact.html')