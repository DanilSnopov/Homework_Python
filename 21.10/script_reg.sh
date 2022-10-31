#!/bin/bash
read -p "Type your login: " log 
exec 2>errors
flag=0
if [[ -f logins ]]
then
$5
else
echo "#logins_list">logins
fi
for line in $(cat logins)
    do
    if [[ $line == $log ]]
    then
        flag=$((1))
        break
    fi
done
if [[ $flag == 0 ]]
then
    echo "Type your password: "
    read -s password
    echo $log >> logins
    echo "{{$password}}" | md5sum >>passwords
    echo "
Registered succesfully"
else
    echo "
User $log already exists"
fi
