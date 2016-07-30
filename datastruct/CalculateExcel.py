#coding:utf-8
from django.conf import settings
from .models import func1_data1,func1_data2
import os
import xlwt
import xlrd

def func1_calculate(username,filename):
    wb_user     =   xlwt.Workbook(encoding='utf-8')
    wb_user_st1 =   wb_user.add_sheet(sheetname="输出1",cell_overwrite_ok=True)
    wb_user_st2 =   wb_user.add_sheet(sheetname="输出2",cell_overwrite_ok=True)

    rb          =   xlrd.open_workbook(os.path.join(os.path.join(settings.MEDIA_ROOT,username+'/func1'),filename),on_demand=True)
    rb_user_st1 =   rb.sheet_by_index(sheetx=0)
    rb_user_st2 =   rb.sheet_by_index(sheetx=1)

    Score       =   [1,1,1,3,3,5,5]

#    行数i，列数j
    Effectiveness   =   [0,0]
    for i,a in enumerate(func1_data1.objects.all().order_by('ItemName','SubItemName')):
        LatestScore =   0
        TmpScore    =   0
        for j in range(5,rb_user_st1.ncols):
            targ    =   rb_user_st1.cell(i*2+1,j)
            real    =   rb_user_st1.cell(i*2+2,j)
            if targ.ctype == 2 and real.ctype == 2:
                if targ.value<=real.value:
                    TmpScore = ((TmpScore << 1) & 0b111111) | 1
                else:
                    TmpScore = ((TmpScore << 1) & 0b111111) | 0
        while TmpScore != 0:
            LatestScore = LatestScore + (TmpScore & 1)
            TmpScore    = TmpScore >> 1

        Effectiveness[0] = Effectiveness[0] + a.Weight * Score[LatestScore]
        Effectiveness[1] = Effectiveness[1] + a.Weight * a.MaxSingle


    Title       =   ["评估项", "评估结果"]
    Maturity    =   []
    TotalMaturity   =   ["评估总分",0,0]
    for i,a in enumerate(Title):
        wb_user_st1.write(i,0,a)

    for i,a in enumerate(func1_data2.objects.all().order_by('ItemName','Serial')):
        if len(Maturity)==0 or Maturity[-1][0]!=a.ItemName:
            Maturity.append([a.ItemName,0,0])
        Maturity[-1][1] = Maturity[-1][1] + a.Weight * rb_user_st2.cell(i+1,3).value
        Maturity[-1][2] = Maturity[-1][2] + a.Weight * a.MaxSingle
    for i,a in enumerate(Maturity):
        wb_user_st1.write(i+1,0,a[0])
        wb_user_st1.write(i+1,1,a[1]/float(a[2]))
        TotalMaturity[1]=TotalMaturity[1]+a[1]
        TotalMaturity[2]=TotalMaturity[2]+a[2]
    wb_user_st1.write(len(Maturity)+1,0,TotalMaturity[0])
    wb_user_st1.write(len(Maturity)+1,1,TotalMaturity[1]/float(TotalMaturity[2]))

    wb_user_st2.write(0,0,'Effectiveness')
    wb_user_st2.write(1,0,Effectiveness[0]/float(Effectiveness[1]))
    wb_user_st2.write(0,1,'Maturity')
    wb_user_st2.write(1,1,TotalMaturity[1]/float(TotalMaturity[2]))

    wb_user.save(os.path.join(os.path.join(settings.MEDIA_ROOT,username+'/func1/result'),'result.xls'))
