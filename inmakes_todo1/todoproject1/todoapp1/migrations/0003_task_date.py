# Generated by Django 3.1.7 on 2021-03-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp1', '0002_remove_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-11-09'),
            preserve_default=False,
        ),
    ]
