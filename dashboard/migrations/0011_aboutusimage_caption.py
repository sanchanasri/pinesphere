# Generated by Django 5.1 on 2024-08-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_aboutus_block_title_alter_aboutus_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusimage',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
