# Generated by Django 3.0.2 on 2020-03-08 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organize', '0001_initial'),
        ('poll', '0012_auto_20200308_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organize.User'),
        ),
        migrations.AlterField(
            model_name='pollvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organize.User'),
        ),
    ]
