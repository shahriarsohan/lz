# Generated by Django 3.2.8 on 2021-11-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_coursecontent_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='video',
            field=models.FileField(upload_to='video/%Y'),
        ),
    ]
