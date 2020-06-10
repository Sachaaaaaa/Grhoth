import requests, json, getpass, hashlib, os
W = "\033[37;1m"
R = "\033[31;1m"
print W
def load_token():
	global token
	global name
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token='+token)
		a = json.loads(r.text)
		name = a['name']
		print 'connect with = '+token
	except:
		token = "no_token"
		name = "no_token"
	main()  

def main():   
	print '\n'                            
	ask = raw_input(name+W+"["+R+"="+W+"]")
	if ask == "help":
		help()
	elif ask == "token":
		id()
	elif ask == "show_token":
		showtoken()
	elif ask == "delete_token":
		deletetoken()
	elif ask == "add_token":
		addtoken()
	elif ask == "load_token":
		print '\n'
		load_token()
	elif ask == "exit":
		os._exit(0)
	elif token == "no_token":
		print '\n'   
		print "you don't have any token"
		main()
	elif ask == "get_phone":
		phone(0)
	elif ask == "get_phone1":
		phone(1)
	elif ask == "get_phone2":
		phone(2)
	elif ask == "get_mail":
		mail(0)
	elif ask == "get_mail1":
		mail(1)
	elif ask == "get_mail2":
		mail(2)
	elif ask == "get_all":
		all()
	elif ask == "get_search":
		search()
	else:
		main()

def mainj():
	print '''
 ______     ______     __  __     ______     ______   __  __    
/\  ___\   /\  == \   /\ \_\ \   /\  __ \   /\__  _\ /\ \_\ \   
\ \ \__ \  \ \  __<   \ \  __ \  \ \ \/\ \  \/_/\ \/ \ \  __ \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\    \ \_\  \ \_\ \_\ 
  \/_____/   \/_/ /_/   \/_/\/_/   \/_____/     \/_/   \/_/\/_/ 

by sweex
type help to show help                                                    
'''   
	load_token()
 
def get(data):
	print W+"["+R+"..."+W+"]"+"Token generation"

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print W+"["+R+"!"+W+"]"+"The token has been successfully generated"
		print W+"["+R+"!"+W+"]"+"The token is stored in cookie/token.log"
		load_token()
	except KeyError:
		print W+"["+R+"!!!!"+W+"]"+"Error"
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print W+"["+R+"!!!"+W+"]"+"Error"
		os.remove('cookie/token.log')
		main()
def id():
	print '\n' 
	open("cookie/token.log", "w").close()
	print W+"["+R+"..."+W+"]"+"Connection to your facebook account"
	id = raw_input(W+"["+R+"?"+W+"]"+"Mail : ")
	pwd = getpass.getpass(W+"["+R+"?"+W+"]"+"Password : ")
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
	x.update(sig)
	data.update({'sig':x.hexdigest()})
	get(data)

def all():
	print '\n'
	r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	a = json.loads(r.text)
	for i in a['data']:
		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		z = json.loads(x.text)
		try:
			phone = str(z['mobile_phone'])
		except KeyError:	
			phone = "?"
		try:
			email = str(z['email'])
		except KeyError:
			email = "?"		
		try:
			location= str(z['location'])
		except KeyError:		
			location = "?"
		finally:
			print "name = " + z['name'] + " " + "id = " + z['id'] +   " " + "phone = " + phone + " " + "mail = " + email + " " + "location = " + location
	main()

def phone(only):
	print '\n'
	r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	a = json.loads(r.text)
	for i in a['data']:
		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		z = json.loads(x.text)
		try:
			phone = str(z['mobile_phone'])
			try:
				email = str(z['email'])
			except KeyError:
				email = "?"
			try:
				location= str(z['location'])
			except KeyError:
				location = "?"
			if int(only) == 1:
				print "name = " + z['name'] + " " + "id = " + z['id'] + " " + "phone = " + phone
			elif int(only) == 2:
				print phone
			else:
				print "name = " + z['name'] + " " + "id = " + z['id'] +   " " + "phone = " + phone + " " + "mail = " + email + " " + "location = " + location
		except KeyError:
			pass
	main()

def mail(only):
	print '\n'
	r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	a = json.loads(r.text)
	for i in a['data']:
		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		z = json.loads(x.text)
		try:
			email = str(z['email'])
			try:
				phone = str(z['phone'])
			except KeyError:
				phone = "?"
			try:
				location= str(z['location'])
			except KeyError:
				location = "?"
			if int(only) == 1:
				print "name = " + z['name'] + " " + "id = " + z['id'] + " " + "mail = " + email
			elif int(only) == 2:
				print email
			else:
				print "name = " + z['name'] + " " + "id = " + z['id'] +   " " + "phone = " + phone + " " + "mail = " + email + " " + "location = " + location
		except KeyError:
			pass
	main()

def search():
	print '\n'
	r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	a = json.loads(r.text)
	tar = raw_input(W+"["+R+"?"+W+"]"+"Id/Name : ")
	for i in a['data']:
		if tar in i['name'] or tar in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)
			try:
				phone = str(z['mobile_phone'])
			except KeyError:	
				phone = "?"
			try:
				email = str(z['email'])
			except KeyError:
				email = "?"		
			try:
				location= str(z['location'])
			except KeyError:		
				location = "?"
			finally:
				print "name = " + z['name']
				print "id = " + z['id']
				print "phone = " + phone
				print "mail = " + email 
				print "location = " + location
		else:
			pass
	main()


def deletetoken():
	print '\n' 
	try:
		os.remove('cookie/token.log')
		print W+"["+R+"!"+W+"]"+"Token successfully removed"
		load_token()
	except:
		print W+"["+R+"!!!"+W+"]"+"Error"
		main()

def showtoken():
	print '\n' 
	try:
		print W+"["+R+"!"+W+"]"+"token = "+token
		print W+"["+R+"!"+W+"]"+name
	except:
		print W+"["+R+"!"+W+"]"+"No token detected"
	main()   

def addtoken():
	print '\n'
	token = raw_input(W+"["+R+"?"+W+"]"+"Token : ")	
	b = open('cookie/token.log','w') 
	b.write(token)
	b.close()
	load_token()
 
def help():
	print '''
-------------------------------------------------------------------------------------
                                  HELP
-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
get_phone 
-------------------------------------------------------------------------------------
get_phone : retrieves the following information: "name, id, phone number, mail address and location" of all your friends with at least one telephone number
the information will be displayed in the form: "name" + "id" + "phone number" + "mail address" + "location"

get_phone1 : retrieves the following information: "name" + "id" + "phone number" + "location" of all your friends with at least one telephone number
the information will be displayed in the form: "name" + "id" + "phone number" + "location"

get_phone2 : retrieves the following information: "name" + "id" + "phone number" of all your friends with at least one telephone number
the information will be displayed in the form: "name" + "id" + "phone number"

-------------------------------------------------------------------------------------
get_mail 
-------------------------------------------------------------------------------------
get_mail : retrieves the following information: "name, id, phone number, mail address and location" of all your friends with at least an email address
the information will be displayed in the form: "name" + "id" + "phone number" + "mail address + "location"

get_mail1 : retrieves the following information: "name" + "id" + "mail address" + "location" of all your friends with at least an email address
the information will be displayed in the form: "name" + "id" + "mail address" + "location"

get_mail2 : retrieves the following information: "name" + "id" + "mail address" of all your friends with at least an email address
the information will be displayed in the form: "name" + "id" + "mail address"

-------------------------------------------------------------------------------------
get_all 
-------------------------------------------------------------------------------------
get_all : retrieves the following information: "name, id, phone number, mail address and location" of all your friends
the information will be displayed in the form: "name" + "id" + "phone number" + "mail address" + "location"

-------------------------------------------------------------------------------------
get_search
-------------------------------------------------------------------------------------
get_search : retrieves the following information: "name, id, phone number, mail address and location" from the specified friend
the information will be displayed in the form:
"name ="
"id ="
"mail =" 
"phone =" 
"location ="

-------------------------------------------------------------------------------------
token
-------------------------------------------------------------------------------------
token : create a new token and delete the old token
show_token : shows the used token
delete_token : delete the used token
load_token : refresh the token
add_token : add a token

-------------------------------------------------------------------------------------
help
-------------------------------------------------------------------------------------
help : show help

-------------------------------------------------------------------------------------
exit
-------------------------------------------------------------------------------------
exit : exit the programm
'''
	main()

mainj()
