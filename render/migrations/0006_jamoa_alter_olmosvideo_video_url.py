# Generated by Django 4.0.3 on 2022-03-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0005_olmosvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jamoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('rasm', models.ImageField(upload_to='')),
                ('nomer', models.FloatField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='olmosvideo',
            name='video_url',
            field=models.FileField(upload_to='media/media/'),
        ),
    ]
