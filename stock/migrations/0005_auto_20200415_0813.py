# Generated by Django 2.0.7 on 2020-04-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_remove_usertraveldetails_route_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='color',
            field=models.CharField(choices=[('r', 'red'), ('b', 'blue'), ('y', 'Yellow')], max_length=15),
        ),
    ]
