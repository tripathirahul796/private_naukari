from django.contrib import admin
from .models import ArticleJob
# Register your models here.
@admin.register(ArticleJob)
class ArticleJobAdmin(admin.ModelAdmin):
    list_display = ('id','job_title','post_name','company_name','post_name','begin_date',\
        'last_date','exam_date','interview_date','admitcard_date','result_date')
