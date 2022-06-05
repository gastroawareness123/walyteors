from django.contrib import admin
from .models import *
from django.forms import Form
from django.db.models import Sum
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field

@admin.register(DoctorHits)
class DoctorHitsAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'hit_count', 'village_or_city', 'state']
    list_filter = (
        ('doctor', admin.RelatedOnlyFieldListFilter),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        models = DoctorHits

class DoctorResource(resources.ModelResource):
    is_qr_code_generated = Field()
    total_hits_count = Field()

    headers_map = {
        'id':'ID',
        'name':'Doctor Name',
        'category':'Category',
        'sales_officer':'Sales Officer',
        'is_qr_code_generated':'Is QR CODE generated?',
        'total_hits_count':'Total Hits Count'
    }


    class Meta:
        model = Doctor
        exclude = ('qr_code')
        export_order = ('id', 'name', 'sales_officer', 'category', 'is_qr_code_generated', 'total_hits_count')

    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            headers[i] = self.headers_map[h]

        return headers

    def dehydrate_is_qr_code_generated(self, obj):
        if obj.qr_code:
            return 'Yes'
        return 'No'
    # is_qr_code_generated.short_description = 'Is QR CODE Generated ?'

    def dehydrate_total_hits_count(self, obj):
        total_hits_count = DoctorHits.objects.select_related('doctor').filter(doctor=obj).aggregate(Sum('hit_count'))
        return total_hits_count.get('hit_count__sum') or 0
    # total_hits_count.short_description = 'Total Hits Count'


@admin.register(Doctor)
class DoctorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'sales_officer', 'category',
                    'is_qr_code_generated', 'total_hits_count']
    resource_class = DoctorResource

    def get_readonly_fields(self, request, obj=None):
        return ['qr_code']

    def is_qr_code_generated(self, obj):
        if obj.qr_code:
            return 'Yes'
        return 'No'
    is_qr_code_generated.short_description = 'Is QR CODE Generated ?'

    def total_hits_count(self, obj):
        total_hits_count = DoctorHits.objects.select_related('doctor').filter(doctor=obj).aggregate(Sum('hit_count'))
        return total_hits_count.get('hit_count__sum') or 0
    total_hits_count.short_description = 'Total Hits Count'

    class Meta:
        model = Doctor

@admin.register(SalesOfficer)
class SalesOfficerAdmin(admin.ModelAdmin):
    list_display = ['name', 'region',]
    class Meta:
        model = SalesOfficer

@admin.register(SalesOfficerRegion)
class SalesOfficerRegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = SalesOfficerRegion

@admin.register(DoctorCategory)
class DoctorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = DoctorCategory