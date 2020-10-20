from tkinter import *
from string import *
from tkinter import messagebox
from random import random

ref1=ascii_lowercase+ascii_uppercase
ref2=digits+ref1
ref3=ref2+"!@#$%^&*()_+=-{]|[}<>?/"

# Executed when there is error generating password
def message():
	messagebox.showinfo("Error","Error generating the desired security password.Try Again!")

# Function generating the password
def generate(reference_list="",password=""):
	global passwd_len_value

	if passwd_strength.get()==1: # A weak password (only alphabets)
		reference_list=ref1
	elif passwd_strength.get()==2: # Medium security password (alphabets + digits)
		reference_list=ref2
	else:     # A strong password (Alphabets + digits + special symbols)
		reference_list=ref3  # A strong password will be generated by Default
  	
	try:
		length=int(passwd_len_value.get())  
		if(length<8):   # An average password should have at least 8 characters
			raise

	except ValueError as Error:  # Exception catching value error
 		messagebox.showinfo("Value Error",str(Error))

	except: # Exception shown when password length is less than 8
	 	messagebox.showinfo("Check password length","Minimum password length should be 8 characters.")
	
	else: # Password generation
	 	
	 	# random() generates a value b/w 0 and 1, then it is multiplied by 100 and casted to integer
	 	# The integer, when divided by the length of reference_list, gives a valid index b/w 0 and length(reference_list)-1
	 	for i in range(0,length):
	 		password+=reference_list[(int(random()*100))%(len(reference_list))]
	 	count1=count2=count3=count4=0

		# Validating a weak password	 	
	 	if reference_list==ref1:
	 		for i in password:
	 			if(i in ascii_uppercase):
	 				count1+=1
	 			else:
	 				count2+=1
	 		# Checking if both lowercase and uppercase alphabets are present
	 		if(count1<1 or count2<1): 
	 			message()
	 		else:
	 			successfully_generated(password)
	 		
		# Validating a medium security password 		
 		elif reference_list==ref2:
 			for i in password:
 				if(i in ascii_uppercase):
 					count1+=1
 				elif(i in ascii_lowercase):
 					count2+=1
 				else:
 					count3+=1
 			
 			# Checking if lowercase alphabets,uppercase alphabets and digits are present
 			if(count1<1 or count2<1 or count3<1):
 				message()
 			else:
 				successfully_generated(password)

		# Validating a strong password 	 		
 		else:
 			for i in password:
 				if(i in ascii_uppercase):
 					count1+=1
 				elif(i in ascii_lowercase):
 					count2+=1
 				elif(i in digits):
 					count3+=1
 				else:
 					count4+=1

 			# Checking if lowercase alphabets,uppercase alphabets, digits and special characters are present 			
 			if(count1<1 or count2<1 or count3<1 or count4<1):
 				message()
 			else:
 				successfully_generated(password)

# Function specifying that password is successfully generated
def successfully_generated(password):
	messagebox.showinfo("Your password is:",password)
	root.clipboard_clear() # Clearing the clipboard
	root.clipboard_append(password) # Automatically copying the generated password


# Creating a tkinter window
root=Tk() # Creating the Tk() object
root.title("Random Password Generator") # title of root window
root.geometry("1400x480") # length*height of the root window
root.configure(bg="black") # background colour of the window

# Adding a background image (Make sure you give the absolute path of the image you want to use if the image is not in the same directory as the file)
bg_image= PhotoImage(file="screenshot1.png") # Background image, you may use the provided image but you may also use your own.
bg_image_label= Label(root,image=bg_image,height=500,width=1400)
bg_image_label.pack()

# Creating a canvas area and setting its geometry
canvas=Canvas(root,bg='light blue',height=180, width=300)
canvas.pack()
canvas.place(x=470,y=150) # Placing the canvas using x,y coordinate system

# Asking the user about the password length
passwd_len=Label(root,text="Enter the length of password to be generated:",font="arial 10")
passwd_len.pack(side=LEFT)
passwd_len.place(x=490,y=170)

# The entered passwd length goes here
passwd_len_value=Entry(root)
passwd_len_value.pack(side=LEFT)
passwd_len_value.place(x=565,y=195)

# Asking user to select the password strength
strength=Label(root,text="Select the strength of the password to be generated:",font="dosis 10",fg="Green")
strength.pack(side=LEFT)
strength.place(x=485,y=220)

# Weak password
passwd_strength=IntVar()
R1=Radiobutton(root,text="Weak",variable=passwd_strength,value=1) # Radiobutton
R1.pack()
R1.place(x=485,y=250)

# Medium security password
R2 = Radiobutton(root,text="Medium",variable=passwd_strength,value=2) # Radiobutton
R2.pack()
R2.place(x=585,y=250)

# Strong password
R3 = Radiobutton(root,text="Strong",variable=passwd_strength,value=3) # Radiobutton
R3.pack()
R3.place(x=700,y=250)

# Button to generate password
b1=Button(root,text="Generate Password",bg="Black",fg="yellow",relief="raised",command=generate,font="arialblack 9",cursor='pirate')
b1.pack(side=BOTTOM)
b1.place(x=564,y=280)

root.mainloop()
