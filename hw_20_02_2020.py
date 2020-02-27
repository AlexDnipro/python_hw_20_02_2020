#https://www.codewars.com/kata/grasshopper-summation/train/python
#Grasshopper - Summation
def summation(num):
    return sum([i for i in range(1,num + 1)])

#https://www.codewars.com/kata/fix-the-loop/train/python
#Fix the loop
def list_animals(animals):
    stroka = ''
    for i in range(len(animals)):
        stroka += str(i+1) + '. ' + animals[i] + '\n'
    
    return stroka

#https://www.codewars.com/kata/double-char/train/python
#Double Char
def double_char(s):
    return "".join([ch * 2 for ch in list(s)])