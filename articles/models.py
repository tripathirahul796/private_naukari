from django.db import models

# Create your models here.
class ArticleInfo(models.Model):
    job_title = models.CharField(max_length=500)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    begin_date = models.DateField()
    last_date = models.DateField()
    exam_date = models.CharField(max_length=200)
    interview_date = models.CharField(max_length=200)
    experiance = models.CharField(max_length=300)
    batch = models.CharField(max_length=300)
    total_post = models.IntegerField()
    post_name = models.CharField(max_length=200)
    eligibility1 = models.CharField(max_length=500)
    eligibility2 = models.CharField(max_length=500,blank=True)
    eligibility3 = models.CharField(max_length=500,blank=True)
    eligibility4 = models.CharField(max_length=500,blank=True)
    eligibility5 = models.CharField(max_length=500,blank=True)
    apply_link = models.URLField()
    offical_link = models.URLField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True)
