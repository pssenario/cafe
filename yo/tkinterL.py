from tkinter import *

def enviar():
        
        nombre = entrada.get()
        print("Hola", nombre)

ventana = Tk()
ventana.configure(bg="blue")

# texto 1
texto1 = Label(
        ventana, 
        text="Valor 1",
        font=('Cascadia Code', 10),
        fg='white',
        bg='blue'
)
texto1.pack(side=LEFT)

# texto 2
texto2 = Label(
        ventana, 
        text="Valor 1",
        font=('Cascadia Code', 10),
        fg='white',
        bg='blue'
)
texto2.pack(side=LEFT)

# entrada 1
entrada = Entry(
        
        ventana,
        font=('Cascadia Code', 10),
        fg='#ddb558',
        bg='#2d2a2e',
        width=60,
        
    )
entrada.pack(pady=20)

# entrada 2
entrada = Entry(
        
        ventana,                
        font=('Cascadia Code', 10),
        fg='#ddb558',
        bg='#2d2a2e',
        width=60,        
    )
entrada.pack(pady=1)

boton = Button(ventana, text="Enviar", command=enviar)
boton.pack()

ventana.mainloop()