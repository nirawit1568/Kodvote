# Generated by Django 3.0.2 on 2020-03-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_auto_20200307_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(),
        ),
    ]