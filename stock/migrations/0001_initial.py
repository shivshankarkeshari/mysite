# Generated by Django 2.0.7 on 2020-04-13 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('1', 'red'), ('2', 'blue'), ('3', 'Yellow')], max_length=15)),
                ('name', models.CharField(max_length=25)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=4)),
                ('lng', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='TrainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.IntegerField()),
                ('train_route_details', models.ManyToManyField(to='stock.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UserTravelDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_string', models.CharField(default='ok', max_length=50)),
                ('destination_station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_station', to='stock.Station')),
                ('start_station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_station', to='stock.Station')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Users')),
            ],
        ),
    ]