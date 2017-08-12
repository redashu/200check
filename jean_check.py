#!/usr/bin/python2

# To check a user with specific user id
# we are using  subprocess for access userbased shell
import  subprocess,time
from subprocess import PIPE

# user_check function will check username with their userid 
def  user_check():

#  calling subprocess call module to check username 
	user=subprocess.call(['useradd','jean'],stderr=PIPE)

#  checking user id 
	uid=subprocess.check_output(['su','-','jean','-c','id -u']).split()[0]
#  checking  group id
	gid=subprocess.check_output(['su','-','jean','-c','id -g']).split()[0]

#  check for  100%  correct answer 

	if user !=  0 and uid == '4332' and gid == '4332' : 
		print  " Question done  "
#  user not created 
	else :
		print   "Not Correct !!"
#  calling  moduler style function 
if __name__ == "__main__" :
	user_check()


