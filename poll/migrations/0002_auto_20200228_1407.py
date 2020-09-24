# Generated by Django 3.0.2 on 2020-02-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('detail', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('password', models.CharField(max_length=10)),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
