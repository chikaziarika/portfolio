# Generated by Django 3.1.4 on 2020-12-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='sample.jpg', null=True, upload_to='img'),
        ),
    ]
