# Generated by Django 3.1.1 on 2020-11-02 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerAndDish', '0003_auto_20201102_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableinfo',
            name='in_time',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
