# Generated by Django 2.2.1 on 2019-08-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190807_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theatre_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='udata',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
