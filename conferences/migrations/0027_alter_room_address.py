# Generated by Django 3.2 on 2022-05-31 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0026_remove_grant_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='conferences.address'),
        ),
    ]
