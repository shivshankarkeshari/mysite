# Generated by Django 2.0.7 on 2020-04-14 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='station',
            options={'verbose_name_plural': 'Stations'},
        ),
        migrations.AlterModelOptions(
            name='traindata',
            options={'verbose_name_plural': 'Train Data'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='usertraveldetails',
            options={'verbose_name_plural': 'Users Travel History'},
        ),
        migrations.RemoveField(
            model_name='usertraveldetails',
            name='route_string',
        ),
    ]
