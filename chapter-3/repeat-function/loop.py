def repeat(string, integer):
   for _ in range(integer):
       print(string)

def repeat_2(string, integer):
    print(string * integer)

def repeat_3(string, integer):
    print((string + '\n') * integer, end='')