# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    print('hello world with anaconda')
    print('I like... strawberries')
    
    listadecosas={'element1':'nada', 'element2':'nadaOtraVez'}
    b=iter(listadecosas)
    for x in b :
        print("imprime tipo b : variable for loop",type(b))
        print("print type x: vairable la other",type(x))
        print("print el dictionario itself", type(listadecosas))
        print(x)


if __name__ == '__main__':
    main()