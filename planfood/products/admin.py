from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Product


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('item_number', 'name', 'unit', 'unit_price')

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('item_number', 'name', 'unit', 'unit_price')
    resource_class = ProductResource
