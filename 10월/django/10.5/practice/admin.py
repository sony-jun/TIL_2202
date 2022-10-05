from django.contrib import admin
from .models import Practice

# Register your models here.


class PracticeAdmin(admin.ModelAdmin):
    fields = ["title"]


admin.site.register(Practice, PracticeAdmin)
