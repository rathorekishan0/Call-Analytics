from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.core.urlresolvers import reverse

from django.core.validators import FileExtensionValidator
# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255, null=True, blank=True)
    userphoto=models.ImageField(upload_to='static/userimages',validators=[FileExtensionValidator(['jpeg','png','bmp','jpg'],"file exteion not valid")],null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
    )
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    contact_no = models.IntegerField(default=0)
    gender = models.IntegerField(choices=GENDER, default=1)
    userphoto=models.ImageField(upload_to='static/music/userimages',validators=[FileExtensionValidator(['jpeg','png','bmp','jpg'],"file exteion not valid")],null=True)

    def __str__(self):
        return self.name


class Recordings(models.Model):
    TYPE = (
        (1, 'Enquiry'),
        (2, 'Complaint'),
    )
    staff = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE, default=0)
    timestamp = models.DateTimeField(null=True, blank=True)
    recording = models.FileField(upload_to='static/callmemaybe/userimages', validators=[FileExtensionValidator(['wav','mp3'], "file format not supported")])

    def __str__(self):
        return "staff:{}, customer:{}".format(self.staff, self.customer)


    class Meta:
        ordering = ['timestamp']

    def get_absolute_url(self):
        return reverse('callmemaybe:detail',kwargs={'pk':self.pk})


class Score(models.Model):
    recording = models.OneToOneField(Recordings, null=True, on_delete=models.CASCADE)
    positive = models.IntegerField(default=0)
    trending = models.IntegerField(default=0, null=True)
    negative = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)
    recording_length = models.IntegerField(default=0)

