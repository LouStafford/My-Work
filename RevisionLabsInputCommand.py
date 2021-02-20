# This is for my own practice only and revision by following Andrews lectures re input prompts 
# & to practice push/pull/commit on Github (also commands) without having to refer to notes from inital lessons
# Here we will ~ Read in a Name/Age & print it out
#  Author Louise Stafford
# input('Please enter your name: ')
# input needs to be stored as variable
name = input('Please enter your name: ')
# Line 5 is only requesting input so at this point when I run, there is no output - I need a print function
print ('Hello ' + name)
# read in age as well as name
# input ('Ok to say your age too?: ')
# I need to add a variable to age so moving line 10 to a comment and 12 to correct format
age = input('Ok to say your age too?: ')
# Now need to also output age
print('Happy days you are only ' + str(age) )
print ('Many more days to enjoy so!:)')
# something I noticed from this excersise is that if I enter text along with my age integer, it repeats the string 
# so I need to look at that e.g I said in one run 'Yes I am 40' and it gave back all - so probably need to 
# use foramt brackets? will check out. I'm pulling string and not identifying number only