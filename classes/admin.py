

from django.contrib import admin

from management.models import Course, Student, Room

# Register your models here.
admin.site.register(Student)

admin.site.register(Course)

admin.site.register(Room)