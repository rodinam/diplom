# Generated by Django 3.2.4 on 2022-01-07 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_works', '0003_solution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='work_id',
            new_name='work',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='work_id',
            new_name='work',
        ),
        migrations.RenameField(
            model_name='workuser',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='workuser',
            old_name='work_id',
            new_name='work',
        ),
    ]