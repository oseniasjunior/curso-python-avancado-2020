# Generated by Django 3.1.2 on 2020-10-06 00:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_column='dt_created_at', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, db_column='dt_modified_at'),
        ),
    ]
