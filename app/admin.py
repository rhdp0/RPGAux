from django.contrib import admin
from .models import main

admin.site.register(main)

class QuestionAdmin(admin.ModelAdmin):
    ordering = ['date_created']
    search_fields = ['question_text']

class PersonAdmin(admin.ModelAdmin):
     list_display = ('first_name', 'last_name')

# Register your models here.
