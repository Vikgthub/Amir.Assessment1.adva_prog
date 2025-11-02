
#import tkinter and random 
import tkinter as tk
import random


#create a file path 
FILE_PATH = 'randomJokes-copy.txt'

#create a function to open the file and read it
def openFile():
    #use try-except to handle errors
    try:
        #open the file in read mode ('r')
        #here, the 'with' ensures the file is automatically closed even if an error happens
        with open(FILE_PATH, 'r') as file_handler:
            #read every single line from the file and removes any extra spaces or newlines 
            #and put all the jokes into a list named lines 
            lines = [line.strip() for line in file_handler if line.strip()]

        #check if the file is empty after stripping and wheather if there are any jokes
        if not lines:
            joke = "File Empty"
        else:
            #if there is a joke, pick one line randomly from the list
            joke = random.choice(lines)
            
        #clear any old text in the text area, starting from line 1, all the way to the end
        txtarea.delete("1.0", tk.END) 
        #insert a random joke into the text area
        txtarea.insert(tk.END, joke)
        

    #if the code cannot find the file at the file path then display an error in the text area
    except FileNotFoundError:
        txtarea.delete("1.0", tk.END)
        txtarea.insert(tk.END, f"Error: File not found at {FILE_PATH}")
        print(f"Error: File not found at {FILE_PATH}")


    #check for other type of error and report the specific error (e) that occurrs
    except Exception as e:
        txtarea.delete("1.0", tk.END)
        txtarea.insert(tk.END, f"An error occurred: {e}")
        print(f"An error occurred: {e}")
    
    #note: it is not necessary to habe the try-except error handler, but its good to have it in case of error and still keep on running the program rather than stoping it in the middle of a found error


#create the user interface 

#fix the window
main = tk.Tk() 
main.title("Alexa's Jokes")
main.geometry("300x300")

#create a rext area to display the jokes from the txt file
txtarea = tk.Text(main, width=40, height=10, wrap=tk.WORD)
txtarea.place(x=20, y=40, height=100, width=250)

# create a button to let the user get the jokes
button = tk.Button( main, text="Alexa, Tell me a Joke!",command=openFile )
button.place(x=20, y=200, height=25, width=250)

main.mainloop()

