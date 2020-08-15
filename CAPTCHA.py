# CAPTCHA


from tkinter import *
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
import os
from PIL import ImageTk,Image
import cv2



image_captcha = ""
isClicked = False

def generate_captcha():
	data_set = list(string.ascii_letters+string.digits)
	s = ""
	for i in range(6):
		a = random.choice(data_set)
		s = s+a
		data_set.remove(a)

	global image_captcha
	image_captcha = s
	return s



def generate_image_captcha():
	os.startfile('cap.png')



def generate_first_image():
	img = ImageCaptcha()

	s = generate_captcha()

	value = img.generate(s)
	img.write(s,"cap.png")




def get_image():
	return image_captcha



def check_image_captcha():
	if ans.get() == get_image():
		tkinter.messagebox.showinfo("Success!","CAPTCHA code Matched.")
		ans.set("")
	else:
		tkinter.messagebox.showinfo("Wrong!","CAPTCHA code does not Match.")
		ans.set("")


def regenerate_image_captcha():
	global isClicked
	isClicked = True

	img = ImageCaptcha()

	s = generate_captcha()

	value = img.generate(s)
	img.write(s,"cap.png")
	os.startfile('cap.png')





root = Tk()
root.title("GUI : CAPTCHA Generation")

root.configure(background = '#ffd9db')
Tops = Frame(pady = 1, width = 550, height = 50, relief = "ridge", background = '#ffd9db')
Tops.grid(row = 0, column = 0)



ans = StringVar()

generate_first_image()

# MainFrame = Frame(root, pady = 2, width = 1350, height = 100, relief = "ridge", background = '#ffd9db')

# MainFrame.grid(row = 1, column = 0)


Label_Heading = Label(font = ('lato black', 15, 'bold',), text = "Verify Captcha", background = '#ffd9db')
Label_Heading.grid(row = 1, column = 0)

generate_image_captcha()

#Label_show = Button(font = ('arial', 20, 'bold'), text = "Show", padx = 2, pady = 2, bg = "white", command = generate_image_captcha)
#Label_show.grid(row = 2, column = 0)



img = cv2.imread('cap.png')
im = Image.fromarray(img)

imgtk = ImageTk.PhotoImage(image = im)

tkinter.Label(root, image = imgtk).grid(row = 2, column = 0)





Enter_captcha = Entry(font = ('arial', 20, 'bold'), bd = 2, fg = "black", textvariable = ans, width = 14).grid(row = 3, column = 0)


Label_Check_Captcha = Button(font = ('arial', 20, 'bold'), text = "Check", padx = 2, pady = 2, bg = "white", command = check_image_captcha)
Label_Check_Captcha.grid(row = 4, column = 0)

Label_regenerate_Captcha = Button(font = ('arial', 20, 'bold'), text = "Regenerate", padx = 2, pady = 2, bg = "white", command = regenerate_image_captcha)
Label_regenerate_Captcha.grid(row = 5, column = 0)




if Label_regenerate_Captcha == True:
	img = cv2.imread('cap.png')
	im = Image.fromarray(img)

	imgtk = ImageTk.PhotoImage(image = im)

	tkinter.Label(root, image = imgtk).grid(row = 6, column = 0)



root.mainloop()