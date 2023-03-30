# Generated by Django 4.1.7 on 2023-03-29 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=200)),
                ('project', models.ManyToManyField(related_name='technology', to='core.project')),
            ],
        ),
    ]
