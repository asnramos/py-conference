# Generated by Django 3.2 on 2022-05-27 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0025_auto_20220527_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='paid',
        ),
    ]
