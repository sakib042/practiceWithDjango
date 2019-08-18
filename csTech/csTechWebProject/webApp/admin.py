from django.contrib import admin
from .models import Tutorial
from .models import Phonebook
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class TutorialAdminClass(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Contents", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Tutorial, TutorialAdminClass)
admin.site.register(Phonebook)

