# Generated by Django 2.2.1 on 2019-08-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20190813_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirm',
            name='ticket_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]