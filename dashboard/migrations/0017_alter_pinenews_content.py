# Generated by Django 5.1 on 2024-08-30 09:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_pinenews_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinenews',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
