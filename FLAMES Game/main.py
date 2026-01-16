from tkinter import *

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
             
             if list1[i]==list2[j]:   #checks the common character
                 c= list1[i]

                 #removing the common character from both lists
                 list1.remove(c)
                 list2.remove(c)

                 list3= list1 + ["*"] + list2  #combining both lists with a separator
                 return [list3, True]
             
    list3= list1+["*"]+list2
    return [list3, False]

def tell_status():

    #take player names from the entry box
    p1= player1_field.get()
    p1= p1.lower()
    
    #replace any space with empty string
    p1= p1.replace(" ", "")
    p1_list= list(p1)  #convert string to list

    p2= player2_field.get()
    p2= p2.lower()
    p2= p2.replace(" ", "")
    p2_list= list(p2)  #convert string to list

    #taking a flag as True initially
    proceed = True

    #keep calling until common char found
    while(proceed):

        #call the function to remove common characters
        ret_list= remove_match_char(p1_list, p2_list)

        #take out concatenated list from return list
        con_list= ret_list[0]

        #take out flag value from return list
        proceed= ret_list[1]

        #find index of "*" / border mark
        star_index= con_list.index("*")

        #all characters before * stored in p1_list
        p1_list= con_list[ : star_index]

        #all characters after * stored in p2_list
        p2_list= con_list[star_index + 1 : ]
    
    #count total remaining characters
    count= len(p1_list) + len(p2_list)

    #list of FLAMES acronyms
    result= ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

    #kepp looping till 1 item is left in the list
    while len(result) > 1:
        split_index= (count % len(result)) - 1
        if split_index >= 0:
            right= result[split_index + 1 : ]
            left= result[ : split_index]
            result= right + left
        else:
            result= result[ : len(result) - 1]
    
    #inserting the value in text entry box
    status_field.insert(10, result[0])


if __name__ == "__main__":
    root= Tk() #creating a GUI window
    root.configure(background= 'light green') #background color
    root.geometry("350x125") #configuration of window
    root.title("Flames Game") #name of tkinter GUI window

    #create player 1 name: label
    label1= Label(root, text= "Player 1 Name: ", fg= "black", bg= "light green")

    #create player 2 name: label
    label2= Label(root, text= "Player 2 Name: ", fg= "black", bg= "dark green")

    #create a relation status: label
    label3= Label(root, text= "Relationship Status: ", fg= "black", bg= "red")

    label1.grid(row=1, column=0, sticky= "E")
    label2.grid(row=2, column=0, sticky= "E")
    label3.grid(row=4, column=0, sticky= "E")

    #create text entry box
    player1_field= Entry(root)
    player2_field= Entry(root)
    status_field= Entry(root)

    player1_field.grid(row=1, column=1, ipadx= "50")
    player2_field.grid(row=2, column=1, ipadx= "50")
    status_field.grid(row=4, column=1, ipadx= "50")


    #create a submit button
    button1= Button(root, text= "Submit", bg= "red", fg= "black", command= tell_status)

    #create a clear button
    button2= Button(root, text= "Clear", bg= "red", fg= "black", command= clear_all)

    button1.grid(row=3, column=1)
    button2.grid(row=5, column=1)

    #start the GUI
    root.mainloop()