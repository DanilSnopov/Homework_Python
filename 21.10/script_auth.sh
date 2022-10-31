#!/bin/bash
read -p "Type your login: " log
exec 2>errors
flag=0
number=-3
for line in $(cat logins)
do
    number=$(($number+2))
    if [[ $line == $log ]]
    then
        flag=$((1))
        break
    fi
done
if [[ $flag == 1 ]]
then
    for line in $(cat passwords)
    do
        number=$(($number-1))
        if [[ $number == 0 ]]
        then
            for ((i=0;i<3;i++))
            do
                echo "Type your password$again: "
                read -t 7 -s password
                echo "{{$password}}" | md5sum >onepassword
                for passwordcut in $(cat onepassword)
                do
                    password=$passwordcut
                    echo _>onepassword
                    break
                done
                if [[ $line == $password ]]
                then
                    echo "
Authorization succesfull"
                    break
                elif [ $i -ne 2 ]
                then
                echo "
Wrong password" 
                again=" again"
                else
                echo "
Authorisation failed"
                echo "User $log authorisation failed">>fails
                fi
            done
        fi
    done
else
echo User $log not found
fi