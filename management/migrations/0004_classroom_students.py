# Generated by Django 3.0.3 on 2020-02-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('management', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(through='classes.StudentAttendance', to='management.Student'),
        ),
    ]
