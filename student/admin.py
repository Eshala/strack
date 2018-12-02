from django.contrib import admin

# Register your models here.
from student.models import Student, Pay


class PayAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        print(obj.user)
        super().save_model(request, obj, form, change)

admin.site.register(Student)
admin.site.register(Pay, PayAdmin)
