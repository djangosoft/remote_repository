# Generated by Django 3.0.1 on 2020-01-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.ImageField(upload_to='')),
                ('cname', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('fees', models.ImageField(upload_to='')),
                ('content', models.FileField(upload_to='files')),
            ],
        ),
    ]
