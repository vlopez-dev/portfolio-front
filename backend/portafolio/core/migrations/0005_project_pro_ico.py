# Generated by Django 4.1.4 on 2022-12-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_project_link_repo"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="pro_ico",
            field=models.ImageField(default="", upload_to=""),
        ),
    ]
