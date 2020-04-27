# Generated by Django 2.0.7 on 2020-04-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=80, unique=True)),
                ('First_Name', models.CharField(max_length=80)),
                ('Last_Name', models.CharField(max_length=80)),
            ],
        ),
    ]
