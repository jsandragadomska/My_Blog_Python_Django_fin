# Generated by Django 3.1 on 2020-08-26 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
    ]