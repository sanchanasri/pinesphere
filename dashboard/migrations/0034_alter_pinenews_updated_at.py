# Generated by Django 5.1 on 2024-09-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_pinenewsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinenews',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
