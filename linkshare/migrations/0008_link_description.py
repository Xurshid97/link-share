# Generated by Django 5.0.5 on 2024-05-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkshare", "0007_category_ispublic_category_isshared"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]