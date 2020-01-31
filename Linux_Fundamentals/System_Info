#!/bin/bash
echo -en '\n'
echo "Choose an option from the below listed to view System Information"
echo -en '\n'
select i in System_Name Hostname Kernel_Version Kernel_Release Hardware_Information CPU_Information Block_Device_Information File_System_Information Exit 
do
case $i in
System_Name) a=$(uname)
echo $a
echo -en '\n'
esac
case $i in
Hostname) b=$(uname -n)
echo $b
echo -en '\n' 
esac
case $i in
Kernel_Version) c=$(uname -v)
echo $c
echo -en '\n' 
esac
case $i in
Kernel_Release) d=$(uname -r)
echo $d
echo -en '\n' 
esac
case $i in
Hardware_Information) e=$(lshw |less)
echo "$e"
echo -en '\n' 
esac
case $i in
CPU_Information) f=$(lscpu|less)
echo "$f"
echo -en '\n' 
esac
case $i in
Block_Device_Information) g=$(lsblk)
echo "$g"
echo -en '\n' 
esac
case $i in
File_System_Information) h=$(fdisk -l|less)
echo "$h"
echo -en '\n' 
esac
case $i in 
Exit)break
esac
done
