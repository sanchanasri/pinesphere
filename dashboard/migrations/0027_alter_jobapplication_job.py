# Generated by Django 5.1 on 2024-09-02 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_job_jobapplication_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.job'),
        ),
    ]
