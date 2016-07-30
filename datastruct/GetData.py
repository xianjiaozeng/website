#coding:utf-8
from django.conf import settings
import os
import xlrd

def func1_get(username,filename):
    rb          =   xlrd.open_workbook(os.path.join(os.path.join(settings.MEDIA_ROOT,username+'/func1/result'),filename),on_demand=True)
    rb_user_st1 =   rb.sheet_by_index(sheetx=0)
    rb_user_st2 =   rb.sheet_by_index(sheetx=1)

    ret1    =   []
    ret2    =   [rb_user_st2.cell(1,0).value,rb_user_st2.cell(1,1).value,1.4,1.55,1.70]
    for i in range(rb_user_st1.nrows):
        ret1.append([])
        for j in range(rb_user_st1.ncols):
            ret1[i].append(rb_user_st1.cell(i,j).value)

    return ret1,ret2
