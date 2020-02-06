# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



iconlst = ['0000000000','0000000000','0000011110','0011110010','1110010010','0110011110',
           '1111110010','0110010010','1110011110','0111100000']

scaleList = []

def scaledList():
    scale = input("Enter a factor to scale the image")
    
    for i in range(0,20):
        iconScale = int(scale) * 10
        tmpStr1 = iconlst[i]
        tmpChar = ""
        for b in range(0,iconScale):
            tmpChar = tmpChar + tmpStr1[i]
        scaleList.append(tmpChar)
    print(scaleList)

    for s in range(0,10):
        rowStr = iconlst[s]
        for z in range(0,int(usrScale)):
            scaleStr = scaleStr + rowStr[s]
        for j in range(0,iconScale):
            if scaleStr[i] == '0':
                print("  ", end=" ")
            else:
                print('@ ', end=' ')

        #for r in range(0,int(usrScale)):
            
        print('\r')          
        
        
scaledList()
'''
def main
for s in range(0,10):
            rowStr = iconlst[s]
            for z in range(0,int(usrScale)):
                scaleStr = scaleStr + rowStr[s]
        for j in range(0,iconScale):
            if scaleStr[i] == '0':
                print("  ", end=" ")
            else:
                print('@ ', end=' ')

        #for r in range(0,int(usrScale)):
            
        print('\r')          
        
        
        '''
        
        
        
        
        
'''
def newMaine():
    usrScale = input("Enter the a # to scale the image :: ")
    iconScale = int(usrScale) * 10
    rowStr = ""
    for i in range(0,iconScale):
        
        scaleStr = ""
        for s in range(0,10):
            rowStr = iconlst[s]
            for z in range(0,int(usrScale)):
                scaleStr = scaleStr + rowStr[s]
        for j in range(0,iconScale):
            if scaleStr[i] == '0':
                print("  ", end=" ")
            else:
                print('@ ', end=' ')

        #for r in range(0,int(usrScale)):
            
        print('\r')
        
newMaine()
'''