# Grhoth
 ______     ______     __  __     ______     ______   __  __    
/\  ___\   /\  == \   /\ \_\ \   /\  __ \   /\__  _\ /\ \_\ \   
\ \ \__ \  \ \  __<   \ \  __ \  \ \ \/\ \  \/_/\ \/ \ \  __ \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\    \ \_\  \ \_\ \_\ 
  \/_____/   \/_/ /_/   \/_/\/_/   \/_____/     \/_/   \/_/\/_/ 
  
Grhoth it is an osint tool which is used to extract information from your facebook friends like email address, phone number or many other things

#Installation
clone https://github.com/Sachaaaaaa/Grhoth.git
cd OSIF

#Setup
pip2 install -r requirements.txt

#Running
python2 Grhoth.py

/!\ (Your VPN can bug the program)/!\ 
/!\ (if you use this program too many times your facebook account can be blocked so don't overuse it )/!\ 

#HOW TO USE IT [ENG]
Grhoth is a tool that requires a token to function correctly
(to generate a token tape "token, to add an already existing tape "add_token")
now the "hardest" part is done
(if the token didn't generate correctly, type "show_token" to display the token, "delete_toke" to delete the token 
or "load_token" to update the token)
now all you have to do is execute the commands :)
(to see the commands list type "help" or look at the list below)

#HOW TO USE IT [FR]
Grhoth est un outils qui nécessite un token pour fonctionner 
(pour en générer un token tape "token", pour en ajouter un dejà existant tape "add_token") 
une fois ce token généré le plus dure est fait 
(si le token ne s'est pas généré correctement tape "show_token" pour afficher le token, "delete_toke" pour supprimer le token 
ou "load_token" pour actualisé le token)
il ne vous reste plus qu'a executer les commandes :)
(pour voir la liste des commandes tape "help" ou regarde la liste ci dessous)

# HELP:
-------------------------------------------------------------------------------------
                                  HELP
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
get_phone 
-------------------------------------------------------------------------------------
get_phone : retrieves the following information: "name, id, phone number, mail address and location" of all your friends with at least one telephone number.
The information will be displayed in the form: "name" + "id" + "phone number" + "mail address" + "location".

-------------------------------------------------------------------------------------
get_phone1
-------------------------------------------------------------------------------------
get_phone1 : retrieves the following information: "name" + "id" + "phone number" + "location" of all your friends with at least one telephone number.
The information will be displayed in the form: "name" + "id" + "phone number" + "location".

-------------------------------------------------------------------------------------
get_phone2
-------------------------------------------------------------------------------------
get_phone2 : retrieves the following information: "name" + "id" + "phone number" of all your friends with at least one telephone number.
The information will be displayed in the form: "name" + "id" + "phone number".

-------------------------------------------------------------------------------------
get_mail 
-------------------------------------------------------------------------------------
get_mail : retrieves the following information: "name, id, phone number, mail address and location" of all your friends with at least an email address.
The information will be displayed in the form: "name" + "id" + "phone number" + "mail address + "location".

-------------------------------------------------------------------------------------
get_mail1
-------------------------------------------------------------------------------------
get_mail1 : retrieves the following information: "name" + "id" + "mail address" + "location" of all your friends with at least an email. address
The information will be displayed in the form: "name" + "id" + "mail address" + "location".

-------------------------------------------------------------------------------------
get_mail2
-------------------------------------------------------------------------------------
get_mail2 : retrieves the following information: "name" + "id" + "mail address" of all your friends with at least an email address.
The information will be displayed in the form: "name" + "id" + "mail address".

-------------------------------------------------------------------------------------
get_all 
-------------------------------------------------------------------------------------
get_all : retrieves the following information: "name, id, phone number, mail address and location" of all your friends.
The information will be displayed in the form: "name" + "id" + "phone number" + "mail address" + "location".

-------------------------------------------------------------------------------------
get_search
-------------------------------------------------------------------------------------
get_search : retrieves the following information: "name, id, phone number, mail address and location" from the specified friend.
The information will be displayed in the form:
"name ="
"id ="
"mail =" 
"phone =" 
"location ="

-------------------------------------------------------------------------------------
token
-------------------------------------------------------------------------------------
token : create a new token and delete the old token.
show_token : shows the used token.
delete_token : delete the used token.
load_token : refresh the token.
add_token : add a token.

-------------------------------------------------------------------------------------
help
-------------------------------------------------------------------------------------
help : show help.

-------------------------------------------------------------------------------------
exit
-------------------------------------------------------------------------------------
exit : exit the programm.
