# Generated by Django 4.0 on 2022-03-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoinUs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapp',
            name='dob',
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='resume',
            field=models.FileField(upload_to='files'),
        ),
    ]
