# -*- coding: utf-8 -*-

import time
from comtypes.client import GetActiveObject

app = GetActiveObject("FeatureCAM.Application")
docs = app.Documents

doc = app.ActiveDocument
print(doc.curves.Count)


# ipart = (doc.PartDocumentation)
# print(ipart.Comments)
# print(dir(ipart))

#  # ?取当前文件的操作
#  # for item in  doc.Operations:
    #  
# print(item.Name)
#  # 3D模?
#  # doc.Sim3D()
#  # 刀?操作
#  # basic = doc.ToolCribs.Item("tools")
#  # orig_em = basic.EndMills.Item("endmillBM0600:4reg")
#  # print(dir(orig_em))
#  # print(orig_em.Name)
#  # print(orig_em)
#  # for item in dir(orig_em):
    #  
# print(item, orig_em.__getattribute__(item))

#  # ?入从xml文件刀具

#  currentCrib = doc.ToolCribs.AddToolCrib("test")
#  # currentCrib.AddTool2(orig_em)
#  # currentCrib.SaveCrib()

#  # currentCrib.ImportTools('./test.xml',True)
#  # 刀具?度?更
#  # temp_em = currentCrib.EndMills.Item("endmillBM0600:4reg")
#  # temp_em.ExposedLength=34
#  # new_em = temp_em.CopyTool("emBM0800:4reg")
#  # temp_em.ExposedLength=54
#  # new_em2 = temp_em.CopyTool("emBM1000:4reg")
#  # temp_em.ExposedLength=44
#  # new_em3 = temp_em.CopyTool("emBM1200:4reg")

#  # currentCrib.AddTool2(new_em) 
#  # currentCrib.AddTool2(new_em2)
#  # currentCrib.AddTool2(new_em3)

#  # currentCrib.DeleteTool(temp_em)
#  # currentCrib.SaveCrib()

#  # cribs = doc.ToolCribs
#  # for crib in cribs:
    #  
# print(crib.Name)

#  # print(currentCrib.Name)
#  # ?入刀柄

#  # spindle2 = currentCrib.Spindles.Item("CAT 40, Spindle (2)")
#  spindle = currentCrib.ActiveSpindle
#  print(spindle.Name)
#  holders = currentCrib.ToolHolders
#  print(holders)
#  for holder in holders:
    #  purint(holder.Name)
#  print(dir(currentCrib))
#  iEndMills = currentCrib.EndMills
#  for i in range(1,iEndMills.Count):
    #  print(iEndMills.Item(i).Name)
#  iActiveToolCrib = doc.ActiveToolCrib
#  iActiveEndMills = iActiveToolCrib.EndMills

#  for i in range(1, iActiveEndMills.Count):
    #  print(iActiveEndMills.Item(i).Name)
#  # print(doc.PartDocumentation)
#  # ?入?出切削用量参数
#  # iDatabase = app.FSDatabase
#  # iDatabase.Export("iData",True)
#  # iDatabase.Import("iData",True)
#  # app.LoadCNC("5_Axis.cnc")
#  app.Configurations.Import("D:\\Users\\00596\\Desktop\\itest.cdb")
#  iConfigs = app.Configurations
#  print(dir(iConfigs))
#  for i in range(1,iConfigs.Count):
    #  kprint(iConfigs.Item(i).Name)
#  iConfig = iConfigs.Item(2)
#  iConfig.DefaultConfiguration()
#  print(iConfig.Name)
#  doc.SimToolpath()

#  # doc.PrintFM(4)


