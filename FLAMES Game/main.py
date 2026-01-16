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