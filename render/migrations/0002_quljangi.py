# Generated by Django 4.0.3 on 2022-03-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='quljangi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('rasm', models.ImageField(upload_to='model/model')),
                ('haqida', models.TextField(max_length=100)),
            ],
        ),
    ]
