# Generated by Django 3.0.2 on 2020-03-07 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organize', '0001_initial'),
        ('poll', '0006_remove_poll_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organize.user'),
        ),
    ]
