# Generated by Django 4.0.3 on 2022-03-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0002_quljangi'),
    ]

    operations = [
        migrations.CreateModel(
            name='bodybuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('rasm', models.ImageField(upload_to='media/media/')),
                ('haqida', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='quljangi',
            name='haqida',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quljangi',
            name='rasm',
            field=models.ImageField(upload_to='model/model/'),
        ),
    ]
