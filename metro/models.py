from django.db import models
from django.contrib.postgres.fields import ArrayField


class Users(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Users"


COLORS = [('r', 'red'),
          ('b', 'blue'),
          ('y', 'Yellow')]


class Station(models.Model):
    color = models.CharField(choices=COLORS, max_length=15)
    name = models.CharField(max_length=25)
    lat = models.DecimalField(max_digits=4, decimal_places=2)
    lng = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name + self.color

    class Meta:
        verbose_name_plural = "Stations"


class TrainData(models.Model):
    train_no = models.IntegerField()
    train_route_details = models.ManyToManyField(Station)
    # train_route_details = ArrayField(models.ForeignKey(Station, on_delete=models.CASCADE))
    '''You can't create an array of foreign keys. It is not a Django limitation, it is a PostgreSQL "limitation".
        The reason is that a foreign key is not a type, it is a constraint on a field. An array of foreign keys 
        does not make any sens.
    '''

    def __str__(self):
        return str(self.train_no)

    class Meta:
        verbose_name_plural = "Train Data"


class UserTravelDetails(models.Model):

    usr = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_station_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_station')
    destination_station_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='destination_station')
    # route_string = models.CharField(max_length=50, default="ok")

    @property
    def route_string(self):

        if self.start_station_id.color == self.destination_station_id.color:
            return f"{self.start_station_id.name}---> {self.destination_station_id.name}"
        else:
            color1_objects = [i.name for i in Station.objects.all().filter(color=self.start_station_id.color)]
            color2_objects = [i.name for i in Station.objects.all().filter(color=self.destination_station_id.color)]
            junction_station = list(set(color1_objects).intersection(color2_objects))
            if junction_station:
                return f"{self.start_station_id.name}--> {junction_station[0]}--> {self.destination_station_id.name}"

    def __str__(self):
        return str(self.usr)

    class Meta:
        verbose_name_plural = "Users Travel History"

