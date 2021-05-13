# Generated by Django 3.1.3 on 2021-05-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rno', models.CharField(max_length=30)),
                ('dob', models.DateField(max_length=30)),
                ('mark', models.CharField(max_length=3)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]