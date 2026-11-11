from tkinter import *
import tkinter as tk
from tkinter import ttk

class Ventanacli(tk.Toplevel):

    def __init__(self, master=None):
        super().__init__()
        self.title("SYSFI - Clientes")
        self.geometry("1000x380")
        self.crearwidget()

    def crearwidget(self):
        # Obtener el año actual
        self.var = tk.StringVar()
        self.var1 = tk.StringVar()

        # ********* Imagenes de los botones *************
        #self.imgTitulo = tk.PhotoImage(file="img/temple.png")
        self.imgNuevo = tk.PhotoImage(file="img/nuevo.png")
        self.imgEditar = tk.PhotoImage(file="img/editar.png")
        self.imgGuardar = tk.PhotoImage(file="img/guardar.png")
        self.imgEliminar = tk.PhotoImage(file="img/eliminar.png")
        self.imgCancelar = tk.PhotoImage(file="img/cancelar.png")
        self.imgSalir = tk.PhotoImage(file="img/salir.png")

        frmEnca = tk.Frame(self,bg="#2A6483")
        frmEnca.place(x=5,y=5,width=990,height=60)
        lblTitu = tk.Label(frmEnca,text="Clientes",bg="#2A6483",fg='white', font=("arial 18"))
        lblTitu.pack(pady=7)

        frmLizq = tk.Frame(self,bg="#2A6483")
        frmLizq.place(x=5,y=70,width=280,height=250)
        self.lblIdenti = tk.Label(frmLizq,text="Identificación",bg="#2A6483",fg='white', font=("arial 12"))
        self.lblIdenti.place(x=10,y=10)
        self.txtIdenti = tk.Entry(frmLizq,font=("arial 12"))
        self.txtIdenti.place(x=110,y=10,width=155)

        self.lblNombre = tk.Label(frmLizq,text="Nombre",bg="#2A6483",fg='white', font=("arial 12"))
        self.lblNombre.place(x=10,y=50)
        self.txtNombre = tk.Entry(frmLizq,font=("arial 12"),textvariable=self.var1)
        self.txtNombre.place(x=85,y=50,width=180)

        self.lblApellido = tk.Label(frmLizq,text="Apellido",bg="#2A6483",fg='white', font=("arial 12"))
        self.lblApellido.place(x=10,y=90)
        self.txtApellido = tk.Entry(frmLizq,font=("arial 12"),textvariable=self.var)
        self.txtApellido.place(x=85,y=90,width=180)
        
        self.lblDireccion = tk.Label(frmLizq,text="Dirección",bg="#2A6483",fg='white', font=("arial 12"))
        self.lblDireccion.place(x=10,y=130)
        self.txtDireccion = tk.Entry(frmLizq,font=("arial 12"),textvariable=self.var)
        self.txtDireccion.place(x=85,y=130,width=180)

        self.lblCelular = tk.Label(frmLizq,text="Celular",bg="#2A6483",fg='white', font=("arial 12"))
        self.lblCelular.place(x=10,y=170)
        self.txtCelular = tk.Entry(frmLizq,font=("arial 12"),textvariable=self.var)
        self.txtCelular.place(x=85,y=170,width=180)

        self.lblSexo = tk.Label(frmLizq,text="Sexo",bg="#2A6483",fg='white', font=("arial 12"))
        self.lblSexo.place(x=10,y=210)
        self.txtSexo = ttk.Combobox(frmLizq,font=("arial 12"),values=("Femenino","Masculino", "Prefiero no decir"), state="readonly")
        self.txtSexo.place(x=85,y=210,width=180)

        

        frmLder = tk.Frame(self,bg="#2A6483")
        frmLder.place(x=290,y=70,width=695,height=250)
        self.tabla = ttk.Treeview(frmLder,columns=("c1", "c2","c3", "c4","c5"))
        self.tabla.column("#0",width=80,anchor='w')
        self.tabla.column("c1",width=100,anchor='w')
        self.tabla.column("c2",width=100,anchor='center')
        self.tabla.column("c3",width=250,anchor='w')
        self.tabla.column("c4",width=80,anchor='w')
        self.tabla.column("c5",width=70,anchor='w')

        self.tabla.heading("#0", text="Identificación", anchor='center')
        self.tabla.heading("c1", text="Nombre", anchor='center')
        self.tabla.heading("c2", text="Apellido", anchor='center')
        self.tabla.heading("c3", text="Dirección", anchor='center')
        self.tabla.heading("c4", text="Celular", anchor='center')
        self.tabla.heading("c5", text="Sexo", anchor='center')

        #self.tabla.pack(fill='both',expand=True)
        self.tabla.pack(side=LEFT,fill = Y)
        sb = Scrollbar(frmLder, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        
        self.tabla.config(yscrollcommand=sb.set)
        sb.config(command=self.tabla.yview)

        frmPie = tk.Frame(self,bg="#2A6483")
        frmPie.place(x=5,y=325,width=990,height=50)
        self.btnNuevo = tk.Button(frmPie,bg="#2A6483", text=" Nuevo  ", image=self.imgNuevo,compound='left')
        self.btnNuevo.pack(padx=10, pady=5, side='left')
        self.btnEditar = tk.Button(frmPie, text=" Editar  ", image=self.imgEditar,compound='left')
        self.btnEditar.pack(padx=10, pady=5, side='left')
        self.btnEliminar = tk.Button(frmPie, text=" Eliminar  ", image=self.imgEliminar,compound='left')
        self.btnEliminar.pack(padx=10, pady=5, side='left')
        self.btnGuardar = tk.Button(frmPie, text=" Guardar  ", image=self.imgGuardar,compound='left')
        self.btnGuardar.pack(padx=10, pady=5, side='left')
        self.btnCancelar = tk.Button(frmPie, text=" Cancelar  ", image=self.imgCancelar,compound='left')
        self.btnCancelar.pack(padx=10, pady=5, side='left')
        self.btnSalir = tk.Button(frmPie, text=" Salir  ", image=self.imgSalir,compound='left')
        self.btnSalir.pack(padx=100, pady=5, side='left')
        
        
def funcliente():
    vencli = Ventanacli()
    vencli.mainloop() 
    

