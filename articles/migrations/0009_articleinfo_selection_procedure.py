# Generated by Django 3.1.1 on 2021-01-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210120_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleinfo',
            name='selection_procedure',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
