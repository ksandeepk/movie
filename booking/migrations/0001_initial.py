# Generated by Django 2.2.1 on 2019-08-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=120)),
                ('cast', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=120)),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('HINDI', 'Hindi'), ('TAMIL', 'Tamil'), ('TELUGU', 'Telugu'), ('MALAYALAM', 'Malayalam'), ('KANNADA', 'Kannada')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='udata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=25)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
