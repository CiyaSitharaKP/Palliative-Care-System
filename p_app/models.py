from django.db import models
from django.contrib.auth.models import User

class staffdata(models.Model):
    staff_id = models.IntegerField()
    name = models.CharField(max_length=600)
    email = models.EmailField()
    gender = models.CharField(max_length=500)
    phoneno = models.BigIntegerField()
    photo = models.ImageField(upload_to='staffs/')
    USER = models.OneToOneField(User, on_delete=models.CASCADE) 

class bedequip(models.Model):
    equipment = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    description = models.TextField()

class division(models.Model):
    name = models.CharField(max_length=600)

class medicinedata(models.Model):
    name = models.CharField(max_length=600)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='medicines/')
    STAFF = models.ForeignKey(staffdata, on_delete=models.CASCADE)

class feedback(models.Model):
    STAFF = models.ForeignKey(staffdata, on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True)

class report(models.Model):
    file = models.FileField(upload_to='reports/')
    date = models.DateField()
    STAFF = models.ForeignKey(staffdata, on_delete=models.CASCADE)

class patientdata(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=500)
    phoneno = models.BigIntegerField()
    photo = models.ImageField(upload_to='patients/')
    place = models.CharField(max_length=600)
    district = models.CharField(max_length=600)
    state = models.CharField(max_length=600)
    pin = models.IntegerField()
    DIV = models.ForeignKey(division, on_delete=models.CASCADE)

    
