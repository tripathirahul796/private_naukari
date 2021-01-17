# Generated by Django 3.1.1 on 2021-01-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
                ('begin_date', models.DateField()),
                ('last_date', models.DateField()),
                ('exam_date', models.DateField()),
                ('interview_date', models.DateField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('total_post', models.IntegerField()),
                ('post_name', models.CharField(max_length=200)),
                ('eligibility1', models.CharField(max_length=500)),
                ('eligibility2', models.CharField(blank=True, max_length=500)),
                ('eligibility3', models.CharField(blank=True, max_length=500)),
                ('eligibility4', models.CharField(blank=True, max_length=500)),
                ('eligibility5', models.CharField(blank=True, max_length=500)),
                ('apply_link', models.URLField()),
                ('offical_link', models.URLField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
