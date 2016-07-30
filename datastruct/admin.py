#coding:utf-8
from django.contrib import admin
from .models import func1_data1,func1_data2
from .GenerateExcel import func1_create
from .CalculateExcel import func1_calculate
# Register your models here.


#class DataLine(admin.StackedInline):
#    model   =   Data
#    extra   =   1

def func1_generate(ModelAdmin,request,queryset):
    func1_create()
#    func1_calculate('common','user.xls')

class func1_admin_data1(admin.ModelAdmin):
    #显示字段
    list_display=   ('ItemName','SubItemName','UnitName','Weight','MaxSingle')
    #显示排序
    ordering    =   ['ItemName','SubItemName']

    #生成功能
    actions      =   [func1_generate]
#    inlines     =   [DataLine]
class func1_admin_data2(admin.ModelAdmin):
    #显示字段
    list_display=   ('ItemName','Serial','SubItemName','Weight','MaxSingle')
    #显示排序
    ordering    =   ['ItemName','Serial']

    #生成功能
    actions      =   [func1_generate]
#    inlines     =   [DataLine]

admin.site.register(func1_data1,func1_admin_data1)
admin.site.register(func1_data2,func1_admin_data2)
func1_generate.short_description    =   "生成"
