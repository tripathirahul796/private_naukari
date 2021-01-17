from django.contrib import admin
from .models import ArticleInfo
# Register your models here.
@admin.register(ArticleInfo)
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ('id','job_title','category','sub_category','begin_date',\
        'last_date','exam_date','interview_date','total_post','post_name')
