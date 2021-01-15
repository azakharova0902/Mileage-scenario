# Generated by Django 3.1.5 on 2021-01-15 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='mileage',
            new_name='new_mileage',
        ),
        migrations.AlterField(
            model_name='cars',
            name='mileage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_mileage', to='tracker.logs'),
        ),
    ]
