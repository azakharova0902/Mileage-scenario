# Generated by Django 3.1.5 on 2021-01-15 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('unit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'mileage_data',
                'get_latest_by': 'mileage',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField(auto_now_add=True)),
                ('mileage', models.IntegerField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.cars')),
            ],
            options={
                'db_table': 'data_logs',
            },
        ),
        migrations.AddField(
            model_name='cars',
            name='mileage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tracker.logs'),
        ),
    ]
