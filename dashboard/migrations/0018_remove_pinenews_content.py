# Generated by Django 5.1 on 2024-08-30 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_alter_pinenews_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinenews',
            name='content',
        ),
    ]
