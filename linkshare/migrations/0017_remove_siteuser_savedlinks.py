# Generated by Django 5.0.5 on 2024-06-06 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkshare', '0016_siteuser_savedlinks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='savedlinks',
        ),
    ]