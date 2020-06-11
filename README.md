# Grhoth

#Description
-------------------------------------------------------------------------------------
Grhoth it is an osint tool which is used to extract information from your facebook friends like email address, phone number or many other things

#Installation
-------------------------------------------------------------------------------------
clone https://github.com/Sachaaaaaa/Grhoth.git <br/>
cd OSIF

#Setup
-------------------------------------------------------------------------------------
pip2 install -r requirements.txt

#Running
-------------------------------------------------------------------------------------
python2 Grhoth.py<br/>

/!\ (Your VPN can bug the program)/!\ <br/>
/!\ (if you use this program too many times your facebook account can be blocked so don't overuse it )/!\ 

#HOW TO USE IT [ENG]
-------------------------------------------------------------------------------------
Grhoth is a tool that requires a token to function correctly<br/><br/>
(to generate a token tape "token, to add an already existing tape "add_token")<br/>
now the "hardest" part is done<br/>
(if the token didn't generate correctly, type "show_token" to display the token, "delete_toke" to delete the token<br/>
or "load_token" to update the token)<br/>
now all you have to do is execute the commands :)<br/>
(to see the commands list type "help" or look at the list below)

#HOW TO USE IT [FR]
-------------------------------------------------------------------------------------
Grhoth est un outils qui nécessite un token pour fonctionner<br/>
(pour en générer un token tape "token", pour en ajouter un dejà existant tape "add_token")<br/>
une fois ce token généré le plus dure est fait<br/> 
(si le token ne s'est pas généré correctement tape "show_token" pour afficher le token, "delete_toke" pour supprimer le token<br/> 
ou "load_token" pour actualisé le token)<br/>
il ne vous reste plus qu'a executer les commandes :)<br/>
(pour voir la liste des commandes tape "help" ou regarde la liste ci dessous)

-------------------------------------------------------------------------------------
                                  HELP
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
get_phone <br/>
-------------------------------------------------------------------------------------
get_phone : retrieves the following information: "name, id, phone number, mail address and location" of all your friends with at least one phone number.
<br/>
The information will be displayed in the form: "name" + "id" + "phone number" + "mail address" + "location".

-------------------------------------------------------------------------------------
get_phone1
-------------------------------------------------------------------------------------
get_phone1 : retrieves the following information: "name" + "id" + "phone number" + "location" of all your friends with at least one phone number.
<br/>
The information will be displayed in the form: "name" + "id" + "phone number" + "location".

-------------------------------------------------------------------------------------
get_phone2
-------------------------------------------------------------------------------------
get_phone2 : retrieves the following information: "name" + "id" + "phone number" of all your friends with at least one telephone number.<br/>
The information will be displayed in the form: "name" + "id" + "phone number".

-------------------------------------------------------------------------------------
get_mail 
-------------------------------------------------------------------------------------
get_mail : retrieves the following information: "name, id, phone number, mail address and location" of all your friends with at least an email address.
<br/>The information will be displayed in the form: "name" + "id" + "phone number" + "mail address + "location".

-------------------------------------------------------------------------------------
get_mail1
-------------------------------------------------------------------------------------
get_mail1 : retrieves the following information: "name" + "id" + "mail address" + "location" of all your friends with at least an email. address
<br/>The information will be displayed in the form: "name" + "id" + "mail address" + "location".

-------------------------------------------------------------------------------------
get_mail2
-------------------------------------------------------------------------------------
get_mail2 : retrieves the following information: "name" + "id" + "mail address" of all your friends with at least an email address.
<br/>The information will be displayed in the form: "name" + "id" + "mail address".

-------------------------------------------------------------------------------------
get_all 
-------------------------------------------------------------------------------------
get_all : retrieves the following information: "name, id, phone number, mail address and location" of all your friends.
<br/>The information will be displayed in the form: "name" + "id" + "phone number" + "mail address" + "location".

-------------------------------------------------------------------------------------
get_search
-------------------------------------------------------------------------------------
get_search : retrieves the following information: "name, id, phone number, mail address and location" from the specified friend.
<br/>The information will be displayed in the form:<br/>
"name ="<br/>
"id ="<br/>
"mail ="<br/>
"phone ="<br/>
"location ="<br/>

-------------------------------------------------------------------------------------
token
-------------------------------------------------------------------------------------
token : create a new token and delete the old token.<br/>
show_token : shows the used token.<br/>
delete_token : delete the used token.<br/>
load_token : refresh the token.<br/>
add_token : add a token.<br/>

-------------------------------------------------------------------------------------
help
-------------------------------------------------------------------------------------
help : show help.

-------------------------------------------------------------------------------------
exit
-------------------------------------------------------------------------------------
exit : exit the programm.
