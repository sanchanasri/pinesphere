# Generated by Django 5.1 on 2024-08-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_remove_aboutus_images_aboutusimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='block_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='heading',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
