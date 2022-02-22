from django.contrib import admin
from .models import Lawyer


class LawyerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Lawyer, LawyerAdmin)


