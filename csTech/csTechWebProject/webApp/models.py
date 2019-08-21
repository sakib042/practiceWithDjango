from django.db import models
from datetime import datetime

# Create your models here.


class TutorialCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class TutorialSeries(models.Model):
    tutorial_series_name = models.CharField(max_length=200)
    category_name = models.ForeignKey(TutorialCategory, default=None, null=True, blank=True, verbose_name="Categories", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series_name


class Tutorial(models.Model):
    tutorial_title = models.CharField("Title", max_length=200)
    tutorial_content = models.TextField("Content")
    tutorial_published = models.DateTimeField("Date Published", default=datetime.now())

    tutorial_series_name = models.ForeignKey(TutorialSeries, default=None, null=True, blank=True, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title


class PhoneBook(models.Model):
    contact_name = models.CharField("Name", max_length=200)
    contact_number = models.CharField("Number",  max_length=20, default="8800000000000")
    contact_address = models.TextField("Address")
    contact_added = models.DateTimeField("Date Added/Updated", default=datetime.now())

    def __str__(self):
        return self.contact_name
