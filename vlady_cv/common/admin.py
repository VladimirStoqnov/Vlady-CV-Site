from django.contrib import admin

# Register your models here.
from vlady_cv.common.models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass