#coding:utf-8
import xlwt
from django.conf import settings
from .models import func1_data1,func1_data2
import os


#第一个功能
#
def func1_create():
    wb_user     =   xlwt.Workbook(encoding='utf-8')
    wb_user_st1 =   wb_user.add_sheet(sheetname="记分卡评估",cell_overwrite_ok=True)
    wb_user_st2 =   wb_user.add_sheet(sheetname="成熟度评估",cell_overwrite_ok=True)


    Title       =   ["评分项", "评分子项", "计量单位", "内容"]
    Detail      =   ["目标", "实际结果"]
    Month       =   ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    Year        =   3

#    题头
    for i,a in enumerate(Title+Month*Year):
        wb_user_st1.write(0,i,a)

#    内容
    for i,a in enumerate(func1_data1.objects.all().order_by('ItemName','SubItemName')):
        wb_user_st1.write_merge(i*2+1,i*2+2,0,0,a.ItemName)
        wb_user_st1.write_merge(i*2+1,i*2+2,1,1,a.SubItemName)
        wb_user_st1.write_merge(i*2+1,i*2+2,2,2,a.UnitName)
        for j,b in enumerate(Detail):
            wb_user_st1.write(i*2+j+1,3,b)

    Title       =   ["评估项", "序列号", "评估子项","评估内容及打分标准"]

#    题头
    for i,a in enumerate(Title):
        wb_user_st2.write(0,i,a)
#    内容
    for i,a in enumerate(func1_data2.objects.all().order_by('ItemName','Serial')):
        wb_user_st2.write(i+1,0,a.ItemName)
        wb_user_st2.write(i+1,1,a.Serial)
        wb_user_st2.write(i+1,2,a.SubItemName)

    wb_user.save(os.path.join(os.path.join(settings.MEDIA_ROOT,'common/func1'),'user.xls'))
