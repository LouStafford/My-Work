# This program is to test why 111 * 555 doesn't run when specified as answer = 111 * 555
# Author : Louise Stafford
# This is part of the lab work 2.2 sheet

# it didn't work as 111 * 555 only, as I haven't asked the computer to Output ~ I need to ask it to Print

# print (111 * 555) was needed

# Next I tried if I can ask it to input a multiplication scenario and print answer 
# BUT we always need to specify inputs/output
# it didn't work as I don't know yet how to output the query if specified like below.. as it prob shouldn't be
#  input worked but not output ** checking and playing
#             query = input ("Please enter a simple multiplication problem : ")
#             print ('multiplication question entered is:' +str(query) )

# Next I tried the following but after many errors of trying to multiply Strs
#  I realised I need an Int or Float!
Value1 = int (input( "please enter value #1 multiplier: "))
Value2 = int (input ("please enter value #2 multiplier: "))
answer = int(Value1 * Value2)
print (answer)
# Something to look into is error handling & parameter allowances
# my code above allows me to enter my name and not just an Int so I get an error:
# ValueError: invalid literal for int() with base 10: 'Louise'
# So it's not tight in testing as my code fails to deny non numerical entries and doesn't request 
# appropiate data only