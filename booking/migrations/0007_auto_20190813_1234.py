# Generated by Django 2.2.1 on 2019-08-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_confirm_saet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirm',
            old_name='saet',
            new_name='seat',
        ),
    ]
