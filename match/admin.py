from django.contrib import admin
from .models import University
from .models import Student

# Register your models here.
admin.site.register(University)
admin.site.register(Student)