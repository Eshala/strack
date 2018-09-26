from django.contrib import admin

# Register your models here.
from group.models import Group, Shift

admin.site.register(Group)
admin.site.register(Shift)