# Generated by Django 3.1.1 on 2021-01-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210121_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlejob',
            name='eligibility',
            field=models.CharField(help_text='Separate with comma', max_length=5000),
        ),
        migrations.AlterField(
            model_name='articlejob',
            name='exam_date',
            field=models.CharField(default='Notified Soon', max_length=200),
        ),
        migrations.AlterField(
            model_name='articlejob',
            name='interview_date',
            field=models.CharField(default='Notified Soon', max_length=200),
        ),
        migrations.AlterField(
            model_name='articlejob',
            name='location',
            field=models.CharField(help_text='Separate with comma', max_length=500),
        ),
        migrations.AlterField(
            model_name='articlejob',
            name='selection_procedure',
            field=models.CharField(max_length=5000),
        ),
    ]
