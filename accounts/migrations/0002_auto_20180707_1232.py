# Generated by Django 2.0.6 on 2018-07-07 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Password',
            new_name='password',
        ),
    ]
