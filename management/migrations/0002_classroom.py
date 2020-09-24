# Generated by Django 3.0.3 on 2020-02-12 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.SmallIntegerField()),
                ('weekday', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday'), ('Su', 'Sunday')], max_length=2)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('room', models.CharField(max_length=10)),
                ('student_amount', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Course')),
            ],
        ),
    ]
