import os
import csv
os.system('top -b -n1|tail -n +7>Top.csv') #-b for batch mode(non-interactive mode) and# -n1 for iterating the command 1 time, tail -n 7 for appending output of top command  #from 7th line
filename="Top.csv"
rows=[]
with open(filename,'r') as csvfile:
 csvreader=csv.reader(csvfile)
 for i in csvreader:
  rows.append(i)
count=1
for i in rows[:100]:
 if(count==1):
  print("\nFields are: ",end='')
  i=i[0].split()
  i=",".join(i)
  print(i)
  print("\n")
  count+=1
 elif(count==2):
  print("Details of top 100 processes are: \n")
  count+=1
 else:
  i=i[0].split()
  i=",".join(i)
  print(i)
