# Generated by Django 4.0.3 on 2022-03-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0007_mashqvideo_alter_jamoa_nomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MashqRasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('video', models.FileField(upload_to='media/media/')),
            ],
        ),
    ]