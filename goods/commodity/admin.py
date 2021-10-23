from django.contrib import admin
from .models import *
# Register your models here.
from commodity.models import *
admin.sites.AdminSite.site_title='后台系统'
admin.sites.AdminSite.site_header='管理系统'
admin.sites.AdminSite.index_title='平台管理'

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display=['id','firsts','seconds']
    exclude = ['firsts']


@admin.register(CommodityInfos)
class CommodityInfosAdmin(admin.ModelAdmin):
    list_display = [x for x in list(CommodityInfos._meta._forward_fields_map.keys())]
    search_fields = ['name','types','sezes','price']
    list_filter = ['types']
    sortable_by = ['sold','id']
    list_per_page = 5
    list_editable = ['price']
    save_as = True

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name=='types':
            db_field.choices=[(x['seconds'],x['seconds']) for x in Types.objects.values('seconds')]
        return super(CommodityInfosAdmin, self).formfield_for_dbfield(db_field,request,**kwargs)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields=[]
        else:
            self.readonly_fields=['sezes']
        return self.readonly_fields