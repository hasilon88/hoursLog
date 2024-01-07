# Generated by Django 3.2.19 on 2024-01-05 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours_logger', '0006_auto_20240105_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='PauseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pause_time', models.DateTimeField()),
                ('resume_time', models.DateTimeField(blank=True, null=True)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pauselogs', to='hours_logger.shift')),
            ],
        ),
    ]