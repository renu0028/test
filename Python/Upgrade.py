import os
import subprocess as sp
print("\nYour current OS details are:\n")
os.system('uname -a')
print("---------------------------------------------------------------------------------------")
print("Checking for updates...")
os.system('yum check-update')
print("---------------------------------------------------------------------------------------")
#else:
n=input("\nDo you want to update specific package  or upgrade your OS?Enter 'p' for package or 'o' for OS\n").strip().lower()
if(n=='o'):
  sp.getoutput('yum update>f1')
  f1=sp.getoutput('cat f1|tail -n +8')
  f2="No packages marked for update"
  if(f1==f2):
   print("Already updated!!")
  else:
   os.system('yum -y update')
   print("\nUpdated version:")
   os.system('uname -r')
   print("---------------------------------------------------------------------------------------")
   s=input("\nWould you like to reboot your system for the updates to be effective? \n").strip().lower()
   if (s=='y'):
    print("\nRebooting your system\n")
    os.system('init 6') #reboot
if (n=='p'):
  pac=input("\nEnter package name:\n")
  os.system('yum -y update {}'.format(pac))
