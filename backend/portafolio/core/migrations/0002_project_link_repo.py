# Generated by Django 3.2.15 on 2022-10-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_repo',
            field=models.CharField(default='null', max_length=100),
        ),
    ]