from django.db import models

from users.models import User

import uuid


# Create your models here.
class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    user = models.ForeignKey(User, related_name="courses" , on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100,null=False,blank=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    public = models.BooleanField(default=True, null=False, blank=False)
    favorite = models.BooleanField(default = False, null=True, blank=True)
    par = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Hole(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    hole = models.IntegerField(blank=False, null=False)
    par = models.IntegerField(blank=False, null=False)
    distance = models.IntegerField(blank=True, null=True)
    tee_longitude = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=6)
    tee_latitude = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=6)
    course = models.ForeignKey(Course, related_name="holes", on_delete=models.CASCADE,null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Hole ' + str(self.hole)
    
class Hazard(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    hole = models.ForeignKey(Hole, related_name="hazards", on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name