from django import forms
from .models import ArticleInfo
class ArticleDes(forms.ModelForm):
    eligibility = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})
    class Meta:
        model = ArticleInfo
        fields = '__all__'
        # widgets ={
        #     'eligibility':forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        # } 
        
class LatesJob(forms.ModelForm):
    eligibility = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})
    class Meta:
        model