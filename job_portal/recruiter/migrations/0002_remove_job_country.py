# Generated by Django 3.1 on 2020-09-30 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='country',
        ),
    ]
