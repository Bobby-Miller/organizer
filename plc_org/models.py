from django.db import models


class Department(models.Model):
    department = models.CharField(primary_key=True, unique=True, max_length=255)

    def __str__(self):
        return self.department


class Workcell(models.Model):
    workcell = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.department, self.workcell)


class Equipment(models.Model):
    equipment_description = models.CharField(max_length=32, unique=True, primary_key=True)
    equip_num = models.IntegerField()
    equipment_id = models.CharField(max_length=255)
    workcell = models.ManyToManyField(Workcell)

    def __str__(self):
        return


class CommunicationType(models.Model):
    communication_type = models.CharField(max_length=255, primary_key=True, unique=True)

    def __str__(self):
        return self.communication_type


class ControllerType(models.Model):
    controller_type = models.CharField(max_length=255, unique=True, primary_key=True)
    communication = models.ManyToManyField(CommunicationType)

    def __str__(self):
        return self.controller_type


class Controller(models.Model):
    name = models.CharField(max_length=255)
    controller_type = models.ForeignKey(ControllerType, on_delete=models.SET_NULL, null=True)
    primary_workcell = models.ForeignKey(Workcell, on_delete=models.SET_NULL, null=True)
    ip_address = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class PointType(models.Model):
    point_type = models.CharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return self.point_type


class Rack(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)
    rack_count = models.IntegerField()
    point_type = models.ForeignKey(PointType, on_delete=models.SET_NULL, null=True)
    rack_location = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.controller, self.rack_location)


class Point(models.Model):
    controller_point_name = models.CharField(max_length=32)
    tag_name = models.CharField(max_length=255)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    point_type = models.ForeignKey(PointType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s - %s' % (self.equipment, self.tag_name)
