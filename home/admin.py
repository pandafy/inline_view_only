from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Device, DeviceLocation, FloorPlan, Location


class DeviceLocationAdminForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Location Name', required=False)

    class Meta:
        model = DeviceLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance:
            kwargs['initial'] = {'name': instance.location.name}
        super().__init__(*args, **kwargs)


class DeviceLocationAdmin(GenericStackedInline):
    model = DeviceLocation
    form = DeviceLocationAdminForm
    extra = 0
    raw_id_fields = ('location',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    inlines = [DeviceLocationAdmin]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    pass
