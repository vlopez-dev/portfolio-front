# Generated by Django 4.1.7 on 2023-03-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_alter_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="description",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="contact",
            name="description",
            field=models.TextField(max_length=500),
        ),
    ]
