# Generated by Django 3.1.1 on 2020-11-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerAndDish', '0014_auto_20201112_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableinfo',
            name='in_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
