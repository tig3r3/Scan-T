#!/usr/bin/env python
# encoding: utf-8

from spidertool import Sqldatatask,Sqldata,SQLTool
import spidertool.config as config

import time
# islocalwork=config.Config.islocalwork
def storedata(ip='',port='',hackinfo=None):

    sqlTool=Sqldatatask.getObject()
    localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
    insertdata=[]
#     if islocalwork==0:
#         work=[]
#         dic={"table":config.Config.iptable,"select_params": ['ip','vendor','osfamily','osgen','accurate','updatetime','hostname','state'],"insert_values": [(temphosts,tempvendor,temposfamily,temposgen,tempaccuracy,localtime,temphostname,tempstate)]}
#         tempdata={"func":'replaceinserttableinfo_byparams',"dic":dic}
#         jsondata=uploaditem.UploadData(url=self.webconfig.upload_ip_info,way='POST',params=tempdata)
#         work.append(jsondata)
#         self.uploadwork.add_work(work)
                     
#     else:
 
    hackinfo=SQLTool.escapewordby(str(hackinfo))
    extra=' on duplicate key update  disclosure=\''+hackinfo+'\' , timesearch=\''+localtime+'\''
              
    insertdata.append((str(ip),port,hackinfo,str(port)))
  
  
    sqldatawprk=[]
    dic={"table":config.Config.porttable,"select_params":['ip','port','disclosure','portnumber'],"insert_values":insertdata,"extra":extra}
                 
    tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
    sqldatawprk.append(tempwprk)
    sqlTool.add_work(sqldatawprk)
    print 'fuzz 转poc检测'
    from ..poc_file import pocsearchtask
    temp=pocsearchtask.getObject()
    temp.add_work([(None,None,ip,port,None,None,hackinfo,None)])
    print 'fuzz 数据存储调用'
    pass
 
     
     