import io
import re
import os 


word_first = 'Panel' #искомое слово
word_succes = 'Succes' # дополнительный параметр
file = 'Authentication.log'

#удачные попытки авторизации кто удачно авторизовался на принтере.
with io.open(file) as f:
    for line in f:
        if word_succes in line:
            print (line, end = "")
            

#Все кто был авторизован на принтере хоть раз

with io.open(file) as f:
    for line in f:
        if word_first in line:
            #print (line, end="")
            print (re.findall('[a-z]{5,}', line))
