#!/bin/bash
USERS=$(wc -l /etc/passwd)
GRO=$(wc -l /etc/group)
U=$(cat /etc/passwd|cut -d: -f 1)
G=$(cat /etc/group|cut -d: -f 1)
echo -en '\n'
echo "Names of all users=" $U
echo -en '\n'
echo  "Names of all groups= " $G
echo -en "\n"
echo "No. of users =" $USERS
echo -en "\n"
echo "No. of groups =" $GRO
echo -en '\n'
