#coding:utf-8
from django.contrib import admin
from .models import Data
from .GenerateExcel import Create
from .CalculateExcel import Calculate
# Register your models here.

#class DataLine(admin.StackedInline):
#    model   =   Data
#    extra   =   1

def Generate(ModelAdmin,request,queryset):
    Create(queryset)
#    for a in queryset:
#        print isinstance(a.ItemName,unicode)
Generate.short_description  =   "生成"

class DataAdmin(admin.ModelAdmin):
    #显示字段
    list_display=   ('ItemName','SubItemName','UnitName','Weight','MaxSingle')
    #显示排序
    ordering    =   ['ItemName','SubItemName']
    #生成功能
    actions      =   [Generate]
#    inlines     =   [DataLine]
admin.site.register(Data,DataAdmin)
