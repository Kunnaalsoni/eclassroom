from django.contrib import admin
from .models import ClassContent, Subjects, Classrooms
# Register your models here.
admin.site.register(ClassContent)
admin.site.register(Subjects)
admin.site.register(Classrooms)