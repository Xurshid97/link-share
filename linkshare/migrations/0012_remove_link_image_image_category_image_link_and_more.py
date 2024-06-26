# Generated by Django 5.0.5 on 2024-05-23 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkshare", "0011_rename_image_image_rasm"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="link",
            name="image",
        ),
        migrations.AddField(
            model_name="image",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="linkshare.category",
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="linkshare.link",
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="linkshare.siteuser",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="linkshare.siteuser",
            ),
        ),
        migrations.AlterField(
            model_name="siteuser",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
