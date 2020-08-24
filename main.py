import io
import re
import os 


word_first = 'Panel' #искомое слово
word_succes = 'Succes' # дополнительный параметр
file = 'Authentication.log'

def main():
    R = input('режим работы программы : ')
    if R == 'succes':
        succes_auto()
    elif R == 'users':
        users()


#удачные попытки авторизации кто удачно авторизовался на принтере.
def succes_auto():
    with io.open(file) as f:
        for line in f:
            if word_succes in line:
                print (line, end = "")
            

#Все кто был авторизован на принтере хоть раз
def users():
    with io.open(file) as f:
        for line in f:
            if word_first in line:
                #print (line, end="")
                print (re.findall('[a-z]{5,}', line))

if __name__ == "__main__":
    main()
