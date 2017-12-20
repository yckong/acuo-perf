import openpyxl
import sys
import os
import glob
import time

#recording total time for the execution of python script
f=open('time.log','a')
start_time=time.time()

count=0
tcount=str(sys.argv[1])
thread=int(sys.argv[1])
rampup=str(sys.argv[2])
loop=str(sys.argv[3])
rowcount=int(sys.argv[4])

#While loop for file creation
while count<thread:
    count=count+1
    f1=openpyxl.load_workbook('demo.xlsx')
    s1=f1.get_sheet_by_name('IRS-Cleared')
    s2=f1.get_sheet_by_name('FRA-Cleared')
    s3=f1.get_sheet_by_name('OIS-Cleared')
    s4=f1.get_sheet_by_name('IRS-Bilateral')
    s5=f1.get_sheet_by_name('FXSwap-Bilateral')
    s6=f1.get_sheet_by_name('ZCS-Cleared')
   

   #While loop for creation of new UTI value depend of row count 
    row = 1
    transaction=0
    while row<=rowcount:
        row=row+1
        transaction=transaction+1
        rowD='D'+str(row)

        val1=str(count)+'1'+str(transaction)
        val2=str(count)+'2'+str(transaction)
        val3=str(count)+'3'+str(transaction)
        val4=str(count)+'4'+str(transaction)
        val5=str(count)+'5'+str(transaction)
        val6=str(count)+'6'+str(transaction)


        s1[rowD]=int(val1)
        s2[rowD]=int(val2)
        s3[rowD]=int(val3)
        s4[rowD]=int(val4)
        s5[rowD]=int(val5)
        s6[rowD]=int(val6)

    f1.save('load%d.xlsx' % count)

#Execution of load test through Jmeter
os.system("Jmeter -n -t portfolioUpload.jmx -l result.csv -J user.count=%s -J user.rampup=%s -J user.loop=%s" %(tcount,rampup,loop))

end_time=time.time()
total=end_time-start_time
f.write('Start Time : '+str(start_time)+'\t'+'End Time : '+str(end_time)+'\t'+'Total Time : '+str(total)+'sec'+'\n')
f.close()

#Deletion of files.
for name in glob.glob('load*.xlsx'):
	os.remove(name)