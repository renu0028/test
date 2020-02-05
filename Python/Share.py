import os
source=input("Enter the path for the file which you want to share: ")
user=input("Enter the user to whom you want to share the file: ")
ipd=input("Enter the ip address of the destination: ")
dest=input("Enter the path where you want to send the file on other system: ")
os.system("scp {} {}@{}:{}".format(source,user,ipd,dest))
print("{} file successfully sent to {}!!".format(source,user))
