#coding:utf-8
from django.conf import settings
import os
import xlwt
import xlrd
from .GenerateExcel import Add,Year,Width,GetFormWidthAndFormLenth
Score   =   [1,1,1,3,3,5,5]
def Calculate(username,filename):
    wb      =   xlwt.Workbook(encoding='utf-8')
    wbst    =   wb.add_sheet(sheetname='记分卡',cell_overwrite_ok=True)
    Add(wbst)
    rb      =   xlrd.open_workbook(os.path.join(os.path.join(settings.MEDIA_ROOT,username),filename))
    rbst    =   rb.sheet_by_index(sheetx=0)
    FormWidth,FormLength    =   GetFormWidthAndFormLenth()
#    行数i，列数j

    for i in range(1,rbst.nrows,Width):
        LatestScore =   0
        for j in range(FormLength,rbst.ncols):
            targ    =   rbst.cell(i,j)
            real    =   rbst.cell(i+1,j)
            wbst.write(i,j,targ.value)
            wbst.write(i+1,j,real.value)
            if targ.ctype == 2 and real.ctype == 2:
                if targ.value != 0:
                    wbst.write(i+2,j,(real.value-targ.value)/targ.value,style=xlwt.Style.easyxf(num_format_str="0.00%"))
                    TmpCnt  =   0
                    for k in range(6):
                        if j - k < FormLength:
                            break
                        if rbst.cell(i,j-k).value<=rbst.cell(i+1,j-k).value:
                            TmpCnt+=1
                    wbst.write(i+3,j,TmpCnt)
                    LatestScore=TmpCnt
        wbst.write_merge(i,i+Width-1,3,3,Score[LatestScore])


#    wbst.write(4,8,xlwt.Formula("A1"))
    wb.save(os.path.join(os.path.join(os.path.join(settings.MEDIA_ROOT,username),'result'),filename))
