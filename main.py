import random
import os

from tkinter import *

from tkinter import messagebox
from tkinter import simpledialog 
def close_window():
    gui.destroy()

tasks_list = []
weights=[]
counter = 1

answer = simpledialog.askstring("Path", "Write the name of the path! \n Don't forget about whitespaces...")
if os.path.exists(answer):
	with open(answer) as f:
		lines = f.readlines()
else:
	messagebox.showerror("Path Error","Path doesn't exist")
	close_window()

def inputError():
	if lines == "":
		messagebox.showerror("Input Error","Nothing to read in file")
		close_window()
		return 0
	return 1

def insertTask():

	global counter

	value = inputError()

	if value == 0:
		return

	for key in lines:
		for i in key.split(" "):
			arr=i.split("-")
			j=0
			while j < len(arr):
				content = arr[j]

				tasks_list.append(content)
				weights.append(float(arr[j+1]))

				TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content + " - "+arr[j+1]+"%\n")

				counter += 1
				j+=2


def delete() :
	
	global counter
	

	if len(tasks_list) == 0 :
		messagebox.showerror("No task","Nothing to delete")
		return

	number = taskNumberField.get(1.0, END)

	if number == "\n" or int(number)>counter :
		messagebox.showerror("Input error","You are trying to delete more than you have")
		return
	
	else :
		task_no = int(number)

	tasks_list.pop(task_no - 1)
	weights.pop(task_no - 1)

	counter -= 1
	
	TextArea.delete(1.0, END)

	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i+1) + " ] " + tasks_list[i] + " - "+str(weights[i])[:-2]+"%\n")
	
def randish() :
	sum=0
	for i in weights:
		sum+=i
	if sum>100:
		messagebox.showerror("Preset error","Common chance greater then 100%!")
		close_window()
	RandArea.insert('end -1 chars',random.choices(tasks_list, weights)[0]+"\n")


if __name__ == "__main__" :


	gui = Tk()

	gui.configure(background = "#738678")

	gui.title("Random roulette")

	gui.geometry("575x450")

	Submit = Button(gui, text = "Load preset", fg = "White", bg = "#007f5c", command = insertTask)

	TextArea = Text(gui, height = 5, width = 60, font = "lucida 13")
	RandArea = Text(gui, height = 5, width = 60, font = "lucida 13")	

	
	taskNumber = Label(gui, text = "Delete element\n--------------\nLoad preset with whitespaces between elements and '-' between element and chance", fg = "White", bg = "#40826d")
	
	taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")

	delete = Button(gui, text = "Delete", fg = "White", bg = "#007f5c", command = delete)
	rand = Button(gui, text = "Random!", fg = "White", bg = "#007f5c", command = randish)

	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
	
	Submit.grid(row = 2, column = 2)
	
	TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
	
	taskNumber.grid(row = 4, column = 2, pady = 5)
	
	taskNumberField.grid(row = 5, column = 2)

	delete.grid(row = 6, column = 2, pady = 5)
	rand.grid(row=7,column=2,pady=5)
	
	RandArea.grid(row = 8, column = 2, padx = 10, sticky = W)
	Exit.grid(row = 9, column = 2)

	gui.mainloop()
