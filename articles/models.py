from django.db import models

# Create your models here.
class ArticleJob(models.Model):
    job_title = models.CharField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length=400)    
    post_name = models.CharField(max_length=200)
    begin_date = models.DateField()
    last_date = models.DateField()
    exam_date = models.CharField(max_length=200,blank=True,help_text="If not then enter Notified Soon")
    interview_date = models.CharField(max_length=200,blank=True)
    selection_procedure = models.CharField(max_length=5000,help_text="Separate with comma")
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    location = models.CharField(max_length=500,help_text="Separate with comma")
    total_post = models.IntegerField()
    eligibility = models.CharField(max_length=5000,help_text="Separate with comma")
    job_description = models.CharField(max_length=5000)
    about_company = models.CharField(max_length=5000)
    apply_link = models.URLField()
    offical_link = models.URLField()
    admitcard_date = models.CharField(max_length=300,blank=True)
    admitcard_link = models.URLField(default="",blank=True)
    result_date = models.CharField(max_length=300, blank=True )
    result_link = models.URLField(blank=True)
    syllabus_link = models.URLField(blank=True)

