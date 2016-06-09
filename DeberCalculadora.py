from tkinter import*
def suma():
	total=int(entrada1.get()) + int(entrada2.get())
	Label(root, text=total).pack()
	
	

def resta():
	total=int(entrada1.get()) - int(entrada2.get())
	Label(root,text=total).pack()

root=Tk()
root.title("CALCULADORA BASICA")
root.title("SUMA")
root.title("RESTA")

num1=IntVar()
num2=IntVar()
entrada1=Entry(root, textvariable=num1)
entrada1.pack()
entrada2=Entry(root, textvariable=num2)
entrada2.pack()
#suma
suma=Button(root, text="SUMA", command=suma)
resta= Button(root, text="RESTA", command=resta)
suma.pack()
resta.pack()
root.mainloop()
