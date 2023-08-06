# string are the immutable data type in Python
#They are sequenntial data-type(iterables)
#creating an empty string
a=""
b=''
c=""" 
"""#docstring or triple quoted string
d='''
'''  ##docstring or triple quoted string
e=str()


# Quote characters
message= "i'm learning python" #double quote outside and single quote inside
# message='I'm learning python' This rasies error
message='He said,"Pyhton is awsome"' #single quote outside and double quote inside
# message="He said,'Python is ausome," this raises error
#But we have the feature of escape sequence in pyhton if we want to use single quote both isnisde and outside
message='I\'m learning pyhton' #here\'is escape sequence
message="He said,\'Python is awsome\'" #here\' is escape sequence

#Escape sequence supress the usual meaning of character and gives new meaning
print("hello\nworld")
print("hello\tworld")




###### Triple quoted strings####

# Triple quoted strings can be used as docstring. We can write docs for function and classes using
#triple quoted strings. sometimes  they are also used as multiline comments.
# They can be stored in a variable like regular string

def addition(a,b):
    """
    This is a function to add two integer
    :param a: First integer input
    :param b: Second integer input
    :return: sum of a and b"""
    return a+b
print(help(addition))


message="""asalshgcdlsaghdfhjdsfhsdjfhsdkfjhsdjfhdslfgsxcvbdsfcfk ldhsfn
ncdsajcbdsabcfadskfjbsdnvbsdfbdksnvbsdkfbsdkfsdjfnskdj
cfbsdkalfbldsakfjhbsdjfhjsdfncs.djfn.sadjfc.sdjf"""
# this is a long string example