# Generated by Django 3.1.5 on 2021-01-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20210115_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='mileage',
        ),
        migrations.AlterField(
            model_name='logs',
            name='log_date',
            field=models.DateField(),
        ),
    ]