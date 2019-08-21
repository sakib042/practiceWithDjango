from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries, PhoneBook
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class TutorialAdminClass(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("URL", {"fields": ["tutorial_slug"]}),
        ("Series", {"fields": ["tutorial_series_name"]}),
        ("Contents", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdminClass)
admin.site.register(PhoneBook)

