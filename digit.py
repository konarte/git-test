import sys
import time
 
zero  = [" *** ", 
         "*   *", 
         "*   *", 
         "*   *",
         "*   *",
         "*   *",
         " *** "]
one   = [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]
two   = [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]
 
digits = [zero, one, two, three, four, five, six, seven, eight, nine]

string=str(input('введите число: '))

for simbol in string:
	#print(simbol)
	try:
		for line in digits[int(simbol)]:
			print(line)
	except ValueError as err:
		print('Ошибка! ', err )
	



time.sleep(50)