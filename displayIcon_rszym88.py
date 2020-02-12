# -*- coding: utf-8 -*-
"""
Spyder Editor
Process::
    -Create a list of the original 10x10 into a 'binary' style list 
        .each item in the list represents a single row, starting from left to right 1-10
    -Create a second list that process the scaling factor as input by the user
        .multiply each list items first variable by the scale factor
            :set a temp string to be set to each new character of the scaled list item
        .loop through each list item by the scaling factor of the 
    -ask user to input a scale factor (assume they are good users and will input a whole #)
    -print out each row which is each list item 
    -first variable in each list will correspond to a row6
This is a temporary script file.
"""


#Create Your Lists (Globas)
iconLst = ['0000000000','0000000000','0000011110','0011110010','1110010010','0110011110',
           '1111110010','0110010010','1110011110','0111100000']
scaleLst = []


def lstScaling():
    #Ask user for an integer input to scale the 
    scale = input("Enter an integer to scale the image by:: ")
    
    #loop through the items in the list
    for i in range(0,10):
        #create a temp variable to store list item in
        tmpItem = iconLst[i]
        #& create a new str to append as the new list item (row)
        scaledRow = ""
        #loop through each index item of the string the # of scaling input
        for x in range(0,int(scale)):
            scaledRow = scaledRow + iconLst[i]
        #Once the stringn reaches the scaled size, append the item to the list
        if i == 9:
            scaleLst.append(tmpItem)
    print(" :: SCALING SUCCESSFUL :: ")
    
def lstDislay():
    #Loop through each item/row/ to print out
    for i in range(0,len(iconLst)):
        #Create a master variable to reference
        rowMaster = iconLst[i]
        #loop through the master and add visual elements for better display
        for x in range(0,len(rowMaster)):
            if rowMaster[x] == '1':
                print("#",end=" ")
            else:
                print(" ", end=" ")
             #Prints characters for display
        #print a line return at the end of each cycle in the outter loop
        print("\r")
        
def codeMain():
    #Begin by calling the scaling function to get the inoput from the user/generate the scaled list
    lstScaling()
    print(scaleLst)
    #Once you've received the scale confirmation you may the run the second function to print the icon
    print("\r")
    print("\r")
    lstDislay()
    print("\r")
    print("\r")
    #inline author badging or watermark
    print("...*** :: Icon Display by @rszym88 :: ***...")
    
#Program Version v1.0
    
codeMain()