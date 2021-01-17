from django import forms
from .models import ArticleInfo
class ArticleDes(forms.ModelForm):
    class Meta:
        model = ArticleInfo
        fields = '__all__'