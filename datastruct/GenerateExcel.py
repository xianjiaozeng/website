#coding:utf-8
import xlwt
from django.conf import settings
import os
TitleName   =   ["评分项", "评分子项", "计量单位","评分标准（1/3/5）", "权重(1/3/5)", "单项最高分", "最高总分", "内容"]
Item        =   []
Detail      =   ["目标", "实际结果", "差率", "最近6个月内满足要求的月份数"]
Month       =   ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Year        =   3
Width       =   len(Detail)
Length      =   len(TitleName)


def GetFormWidthAndFormLenth():
    global Item
    FormWidth   =   0
    FormLength  =   0
    for i in range(len(Item[0])):
        FormWidth+=len(Item[1][i])*Width
    FormWidth+=1
    FormLength=Length
    return FormWidth,FormLength

def Add(st):
    global TitleName,Item,Detail,Month,Year,Width,Length
    ItemSt  =   0
    ItemEd  =   1

#    题头
    for i in range(Length):
        st.write_merge(ItemSt,ItemEd-1,i,i,TitleName[i])
    for i in range(12*Year):
        st.write_merge(ItemSt,ItemEd-1,i+Length,i+Length,Month[i%12])

#    内容
    for i in range(len(Item[0])):
        ItemSt      =   ItemEd
        ItemEd      =   ItemSt + Width * len(Item[1][i])
        st.write_merge(ItemSt,ItemEd-1,0,0,Item[0][i])
        for j in range(len(Item[1][i])):
            for k in range(1,6):
                if k <3:
                    st.write_merge(ItemSt + j * Width,ItemSt + (j + 1) * Width-1,k,k,Item[k][i][j])
                else:
                    st.write_merge(ItemSt + j * Width,ItemSt + (j + 1) * Width-1,k+1,k+1,Item[k][i][j])
            for k in range(Width):
                st.write_merge(ItemSt + j * Width + k,ItemSt + j * Width + k,7,7,Detail[k])



def Create(queryset):
    global TitleName,Item,Detail,Month,Year,Width,Length,FormWidth,FormLength

    wb      =   xlwt.Workbook(encoding='utf-8')
    wbst    =   wb.add_sheet(sheetname="记分卡",cell_overwrite_ok=True)
    Item    =   []
    for a in queryset:
        if len(Item)==0:
            Item.append([a.ItemName])
            Item.append([[a.SubItemName]])
            Item.append([[a.UnitName]])
            Item.append([[a.Weight]])
            Item.append([[a.MaxSingle]])
            Item.append([[a.Weight*a.MaxSingle]])
        elif a.ItemName not in Item[0]:
            Item[0].append(a.ItemName)
            Item[1].append([a.SubItemName])
            Item[2].append([a.UnitName])
            Item[3].append([a.Weight])
            Item[4].append([a.MaxSingle])
            Item[5].append([a.Weight*a.MaxSingle])
        else:
            pos=Item[0].index(a.ItemName)
            Item[1][pos].append(a.SubItemName)
            Item[2][pos].append(a.UnitName)
            Item[3][pos].append(a.Weight)
            Item[4][pos].append(a.MaxSingle)
            Item[5][pos].append(a.Weight*a.MaxSingle)

    Add(wbst)
    wb.save(os.path.join(os.path.join(settings.MEDIA_ROOT,'common'),'a.xls'))

    pass
