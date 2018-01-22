#################################################
#File creation and modification
#Generate UTI
#Generate Portfolio IDs
#Auto Configure Body Parameter for Jmeter
#################################################

import openpyxl
import sys
import os
import glob
import time
from itertools import cycle
import ConfigParser

#recording total time for the execution of python script
timelog=open('time.log','a')
start_time=time.time()

#Collect argv from config file
config = ConfigParser.RawConfigParser()
config.read('test.cfg')
argv1=config.getint('config','threads')
argv2=config.getint('config','rampup')
argv3=config.getint('config','loop')
argv4=config.getint('config','transactions')
argv5=config.get('config','portfolioIDs')
argv6=config.get('config','filename')


#define arguments
Plist=argv5.split(",")
count=0
tcount=str(argv1)
thread=int(argv1)
rampup=str(argv2)
loop=str(argv3)
rowcount=int(argv4)

#Configure BodyData for portfolioids
PortfolioIDs_BD="{\"ids\":["
for items in Plist:
	PortfolioIDs_BD=PortfolioIDs_BD+'"'+items+'"'+","
BPortfolioIDs_BD=PortfolioIDs_BD.rstrip(',')
PortfolioIDs_BD=PortfolioIDs_BD+"]}"

#write portfolio IDs
portfolio_txt=open("portfolioids.txt","w")
portfolio_txt.write(PortfolioIDs_BD)
portfolio_txt.close()

#portfolio ID list
pool = cycle(Plist)

#While loop for file creation
while count<thread:
    count=count+1
    f1=openpyxl.load_workbook(argv6)
    s1=f1.get_sheet_by_name('IRS-Cleared')
    s2=f1.get_sheet_by_name('FRA-Cleared')
    s3=f1.get_sheet_by_name('OIS-Cleared')
    s4=f1.get_sheet_by_name('IRS-Bilateral')
    s5=f1.get_sheet_by_name('FXSwap-Bilateral')
    s6=f1.get_sheet_by_name('ZCS-Cleared')
   
   #Loop for file modification(UTI, portfolio IDs)
    row = 1
    transaction=0
    while row<=rowcount:
        row=row+1
        transaction=transaction+1

        ID=pool.next()
        
        #UTI cell number
        rowD='D'+str(row)

        #Portfolio cell number
        tab1='AX'+str(row)
        tab2='AK'+str(row)
        tab3='AY'+str(row)
        tab4='AQ'+str(row)
        tab5='AI'+str(row)
        tab6='AY'+str(row)

        #Excel file modification
        #Portfolio Modification
        s1[tab1]=str(ID)
        s2[tab2]=str(ID)
        s3[tab3]=str(ID)
        s4[tab4]=str(ID)
        s5[tab5]=str(ID)
        s6[tab6]=str(ID)

        #UTI Number Generation
        val1=str(count)+'1'+str(transaction)
        val2=str(count)+'2'+str(transaction)
        val3=str(count)+'3'+str(transaction)
        val4=str(count)+'4'+str(transaction)
        val5=str(count)+'5'+str(transaction)
        val6=str(count)+'6'+str(transaction)

        #UTI Modification
        s1[rowD]=int(val1)
        s2[rowD]=int(val2)
        s3[rowD]=int(val3)
        s4[rowD]=int(val4)
        s5[rowD]=int(val5)
        s6[rowD]=int(val6)

    f1.save('load%d.xlsx' % count)

#Execution of load test through Jmeter
#os.system("Jmeter -n -t UploadValuation.jmx -l result.csv -J user.count=%s -J user.rampup=%s -J user.loop=%s" %(tcount,rampup,loop))


end_time=time.time()
total=end_time-start_time
timelog.write('Start Time : '+str(start_time)+'\t'+'End Time : '+str(end_time)+'\t'+'Total Time : '+str(total)+'sec'+'\n')
timelog.close()

#Deletion of files.
#for name in glob.glob('load*.xlsx'):
#	os.remove(name)