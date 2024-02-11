import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x400")
etiqueta = tkinter.Label(ventana, text="vamos!!!")
etiqueta.pack(side=tkinter.BOTTOM)

ventana.mainloop()
