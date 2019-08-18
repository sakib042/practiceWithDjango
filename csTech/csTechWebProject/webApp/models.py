from django.db import models
from datetime import datetime

# Create your models here.

class Tutorial(models.Model):
    tutorial_title = models.CharField("Title", max_length=200)
    tutorial_content = models.TextField("Content")
    tutorial_published = models.DateTimeField("Date Published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title

class Phonebook(models.Model):
    contact_name = models.CharField("Name", max_length=200)
    contact_number = models.CharField("Number",  max_length=20, default="8800000000000")
    contact_address = models.TextField("Address")
    contact_added = models.DateTimeField("Date Added/Updated", default=datetime.now())

    def __str__(self):
        return self.contact_name
