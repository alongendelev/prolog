# prolog
there are 2 files in here,
1) a .exe file that can be ran from cmd directly in the command format (showen below) (you need to navigate to the folder you saved it in first)
2) a text file containing the code writen in python

unfortunatly i had a problem that cmd couldnt interpret the signs ( ) as part of the argumant, 
in my understanding because they are special characters in the shell language that cmd uses

for that reason i changed the commands format to be: prolog "<argumant>(<param>)" "<argumant>(<param>)"...
example: prolog "write_to(newfile.prolog)" "from_file(log.txt)" "byLevel(WARN)"
