# Generated by Django 3.1.3 on 2020-11-22 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdata',
            old_name='title',
            new_name='output',
        ),
        migrations.RemoveField(
            model_name='blogdata',
            name='link',
        ),
    ]