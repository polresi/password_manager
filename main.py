from tkinter import *
from tkinter import messagebox
import functools
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import sys
import database


class App():
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Encrypt-It")
        self.icono=PhotoImage("images/candado.ico")
        self.root.iconbitmap(self.icono)
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.opcionesMenu=Menu(self.menubar, tearoff=0)
        self.opcionesMenu.add_separator()
        self.opcionesMenu.add_command(label="Salir", command=self.salirAplicacion)
        self.opcionesMenu.add_separator()
        self.ayudaMenu=Menu(self.menubar, tearoff=0)
        self.ayudaMenu.add_command(label="Acerda de", command=self.explicacionacercade)
        self.ayudaMenu.add_command(label="Funcionamiento", command=self.explicacionfuncionamiento)
        self.ayudaMenu.add_separator()
        self.ayudaMenu.add_command(label="Versión", command=self.infoAdicional)
        self.menubar.add_cascade(label="Opciones", menu=self.opcionesMenu)
        self.menubar.add_cascade(label="Ayuda", menu=self.ayudaMenu)

        self.frame = StartPage(self.root)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self.root)
        self.frame.pack()

    def infoAdicional(self):
        messagebox.showinfo(title="Versión", message="Versión 1.0.0")

    def salirAplicacion(self):
        valor = messagebox.askokcancel(title= "Salir", message = "¿Seguro que quieres salir?")
        if valor == True:
            self.root.quit()

    def explicacionacercade(self):
        messagebox.showinfo(title="Información relevante", message="Bienvenido a 'Encrypt-It', tu programa encriptador para mantener tus archivos seguros! Para más información haga clic en Funcionamiento")

    def explicacionfuncionamiento(self):
        messagebox.showinfo(title="Información relevante", message="Para saber cómo funciona esta aplicación, abra el archivo 'Funcionamiento.txt' que encuentra en el archivo de descarga de la aplicación.")

    def sequence(self,*functions):
        def func(*args, **kwargs):
            return_value = None
            for function in functions:
                return_value = function(*args, **kwargs)
            return return_value
        return func

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

class StartPage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        ttk.Style().configure("TButton", padding=2, relief="flat", background="#ccc")

        self.logo=PhotoImage(file="images/logo.png")
        self.config(bg="white")

        label_bienvenido = tk.Label(self, image=self.logo, justify="center", bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=20,padx=20, sticky="w")

        button_adelante=ttk.Button(self, command=self.siguiente_page, text='Adelante', cursor="hand2")
        button_adelante.grid(row=1, column=2, padx=10, pady=10, sticky="e")

    def siguiente_page(self):
        app.change(PageOne)

class PageOne(Frame):
    def __init__(self, root,):

        Frame.__init__(self, root)

        ttk.Style().configure("TButton", padding=2, relief="flat", background="#ccc")

        self.logopequeno=PhotoImage(file="images/logopequeño.png")

        self.config(bg="white")

        label_bienvenido = Label(self, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=2, row=0, column=0, pady=10,padx=10, sticky="w")

        label_texto= Label(self, text="Elija que prefiere hacer", bg="white", fg="#03989E")
        label_texto.grid(columnspan=2, row=1, column= 1, padx = 10, pady=10)
        label_texto.config(font=("Source Sans Pro",24, "bold"))

        button_iniciarsesion=ttk.Button(self, text='Iniciar Sesión', command=self.PageMainApplication, width=28, cursor="hand2")
        button_iniciarsesion.grid(columnspan=2, row=2, column=1, padx=10, pady=10, ipady=10, ipadx=10)

        button_registrarse=ttk.Button(self, text='Registrarse', command = self.PageRegistrarse, width=28, cursor="hand2")
        button_registrarse.grid(columnspan=2, row=3, column=1, padx=10, pady=10, ipady=10, ipadx=10)

        button_retroceder=ttk.Button(self, text='Cancel', command=self.startPage, cursor="hand2")
        button_retroceder.grid(row=4, column=2, padx=10, pady=10, sticky="e")

    def startPage(self):
        app.change(StartPage)

    def PageRegistrarse(self):
        app.change(PageRegistrarse)

    def PageMainApplication(self):
        app.change(PageMainApplication)

class PageRegistrarse(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)

        ttk.Style().configure("TButton", padding=2, relief="flat", background="#ccc")
        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.config(bg="white")

        label_bienvenido = Label(self, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

        label_texto= Label(self, text="Registrarse", bg="white", fg="#03989E")
        label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",20, "bold"))

        label_texto= Label(self, text="Nombre: ", bg="white",fg="black")
        label_texto.grid(row=2, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        label_texto= Label(self, text="Mail: ", bg="white", fg="black")
        label_texto.grid(row=3, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        label_texto= Label(self, text="Contraseña: ", bg="white", fg="black")
        label_texto.grid(row=6, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        label_texto= Label(self, text="Repetir contraseña: ", bg="white", fg="black")
        label_texto.grid(row=7, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        self.myEntryNombre=ttk.Entry(self)
        self.myEntryNombre.grid(row=2, column=1, padx=10)

        self.myEntryMail=ttk.Entry(self)
        self.myEntryMail.grid(row=3, column=1, padx=10)

        self.myEntryPasswordnormal=ttk.Entry(self)
        self.myEntryPasswordnormal.grid(row=6, column=1, padx=10)
        self.myEntryPasswordnormal.config(show="•")

        self.myEntryPasswordsecure=ttk.Entry(self)
        self.myEntryPasswordsecure.grid(row=7, column=1, padx=10)
        self.myEntryPasswordsecure.config(show="•")

        self.nombre = self.myEntryNombre.get()
        self.mail = self.myEntryMail.get()
        self.password = self.myEntryPasswordnormal.get()
        self.passwordsecure = self.myEntryPasswordsecure.get()

        button_retroceder=ttk.Button(self, text='Cancel', command = self.PageOne, cursor="hand2")
        button_retroceder.grid(row=11, column=1, padx=10, pady=10, sticky="e")

        button_registrarse=ttk.Button(self, text="Registrarse", command = self.LevelClave, cursor="hand2")
        button_registrarse.grid(row=10, columnspan=3, column=0, padx=10, pady=8, ipadx=20, ipady=8)

    def insert_data(self):

        self.nombre = self.myEntryNombre.get()
        self.mail = self.myEntryMail.get()
        self.password = self.myEntryPasswordnormal.get()
        self.passwordsecure = self.myEntryPasswordsecure.get()
        self.clave = self.myEntryClaveaa.get()
        self.clavesecure = self.myEntryClavebb.get()

        check_counter=0
        warn = ""

        if self.nombre == "":
            warn = "El campo de nombre es obligatorio."
        else:
            check_counter += 1

        if self.mail == "":
            warn = "El campo de correo electrónico es obligatorio."
        else:
            check_counter += 1

        if self.password == "":
            warn = "El campo de contraseña es obligatorio."
        else:
            check_counter += 1

        if self.passwordsecure == "":
            warn = "Debe de repetir la contraseña para comprobar que no se haya equivocado."
        else:
            check_counter += 1

        if self.password != self.passwordsecure:
            warn = "Las contraseñas no coinciden, vuelva a intentarlo."
        else:
            check_counter += 1

        if self.clave == "":
            warn = "El campo de clave es obligatorio."
        else:
            check_counter += 1

        if self.clavesecure == "":
            warn = "Debe de repetir la clave para comprobar que no se haya equivocado."
        else:
            check_counter += 1

        if self.clave != self.clavesecure:
            warn = "Las claves no coinciden, vuelva a intentarlo."
        else:
            check_counter += 1

        if check_counter == 8:
            try:
                database.createUser(self.mail, self.password, self.nombre, self.clave)
                messagebox.showinfo('Confrimación', 'Se ha registrado exitósamente! Ahora, inicie sesión para utilizar los servicios de Encrypt-it.')
                self.top.destroy()
                self.top.update()
                app.show()
                app.change(PageMainApplication)
            except Exception as ep:
                messagebox.showerror('', ep)
        else:
            messagebox.showerror('Error', warn)
    def PageOne(self):
        app.change(PageOne)

    def LevelClave(self):

        check_counter=0
        warn = ""

        self.nombre = self.myEntryNombre.get()
        self.mail = self.myEntryMail.get()
        self.password = self.myEntryPasswordnormal.get()
        self.passwordsecure = self.myEntryPasswordsecure.get()

        if self.nombre == "":
            warn = "El campo de nombre es obligatorio."
        else:
            check_counter += 1

        if self.mail == "":
            warn = "El campo de correo electrónico es obligatorio."
        else:
            check_counter += 1

        if self.password == "":
            warn = "El campo de contraseña es obligatorio."
        else:
            check_counter += 1

        if self.passwordsecure == "":
            warn = "Debe de repetir la contraseña para comprobar que no se haya equivocado."
        else:
            check_counter += 1

        if self.password != self.passwordsecure:
            warn = "Las contraseñas no coinciden, vuelva a intentarlo."
        else:
            check_counter += 1

        if any(i in "@" for i in self.mail):
            check_counter += 1
        else:
            warn = "Tiene que introducir un '@' en el mail."

        if check_counter == 6:
            app.hide()
            messagebox.showinfo('recordatorio de la clave', 'Le recordamos que la clave le será esencial a la hora de desencriptar sus elementos. Es una medida más de seguridad para esta aplicación.')
            def exit_btn():
                self.top.destroy()
                self.top.update()

            self.top = Toplevel()
            self.top.config(bg="white")
            self.top.resizable(0,0)
            self.top.title("Encrypt-It")

            self.top.title("Encrypt-It")
            icono=PhotoImage("images/candado.ico")
            self.top.iconbitmap(icono)

            label_bienvenido = Label(self.top, image=self.logopequeno, bg="white")
            label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

            label_texto = Label(self.top, text="Crear Clave", bg="white", fg="#03989E")
            label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",20, "bold"))

            label_texto= Label(self.top, text="Clave: ", bg="white", fg="black")
            label_texto.grid(row=8, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",12))

            label_texto= Label(self.top, text="Repetir Clave: ", bg="white", fg="black")
            label_texto.grid(row=9, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",12))

            self.myEntryClaveaa=ttk.Entry(self.top)
            self.myEntryClaveaa.grid(row=8, column=1, padx=10)
            self.myEntryClaveaa.config(show="•")

            self.myEntryClavebb=ttk.Entry(self.top)
            self.myEntryClavebb.grid(row=9, column=1, padx=10)
            self.myEntryClavebb.config(show="•")

            self.clave = self.myEntryClaveaa.get()
            self.clavesecure = self.myEntryClavebb.get()

            button_registrarse=ttk.Button(self.top, text="Guardar Clave", command = self.insert_data, cursor="hand2")
            button_registrarse.grid(row=10, columnspan=3, column=0, padx=10, pady=8, ipadx=20, ipady=8)

        else:
            messagebox.showerror('Error', warn)
            check_counter = 0

class PageMainApplication(Frame):

    def __init__(self, root):

        Frame.__init__(self, root)
        ttk.Style().configure("TButton", padding=2, relief="flat", background="#ccc")
        self.config(bg="white")

        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        label_bienvenido = Label(self, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

        self.label_texto= Label(self, text="Iniciar Sesión", bg="white", fg="#03989E")
        self.label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
        self.label_texto.config(font=("Source Sans Pro",20, "bold"))

        self.label_texto= Label(self, text="Mail: ", bg="white", fg="black")
        self.label_texto.grid(row=2, column= 0, padx = 10, pady=10, sticky="w")
        self.label_texto.config(font=("Source Sans Pro",12))

        self.label_texto= Label(self, text="Contraseña: ", bg="white", fg="black")
        self.label_texto.grid(row=3, column= 0, padx = 10, pady=10, sticky="w")
        self.label_texto.config(font=("Source Sans Pro",12))

        self.myEntryLoginmail= ttk.Entry(self)
        self.myEntryLoginmail.grid(row=2, column=1, padx=10)

        self.myEntryLoginpw= ttk.Entry(self)
        self.myEntryLoginpw.grid(row=3, column=1, padx=10)
        self.myEntryLoginpw.config(show="•")

        self.button_retroceder=ttk.Button(self, text='Cancel',command=self.SalirIniciarSesion, cursor="hand2")
        self.button_retroceder.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        self.button_registrarse=ttk.Button(self, text='Iniciar Sesión', command = self.Entrartoplevel, cursor="hand2")
        self.button_registrarse.grid(row=4, columnspan=2, column=0, padx=10, pady=8, ipadx=20, ipady=8)

        self.estado = 0

    def SalirIniciarSesion(self):
        app.change(PageOne)

    def Entrartoplevel(self):
        self.mail = self.myEntryLoginmail.get()
        self.password = self.myEntryLoginpw.get()

        check_counter=0
        warn = ""

        if self.mail == "":
            warn = "El campo de nombre es obligatorio."
        else:
            check_counter += 1

        if self.password == "":
            warn = "El campo de contraseña es obligatorio."
        else:
            check_counter += 1

        if check_counter == 2:

            try:
                value = database.loginUser(self.mail, self.password)
                if value == "yes":
                    messagebox.showinfo("Confirmación", "Has entrado exitosamente")
                    self.LevelLista()
                elif value == "no":
                    messagebox.showwarning("Contraseña incorrecta", "Contraseña incorrecta")
                else:
                    messagebox.showwarning("Usuario inexistente", "usuario inexistente")

            except Exception as ep:
                messagebox.showwarning('', ep)
        else:
            messagebox.showwarning('Error', warn)

    def LevelLista(self):
        app.hide()

        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.engra =PhotoImage(file = "images/engra.png")

        self.top = Toplevel()
        self.top.config(bg="white")
        self.top.resizable(0,0)
        self.top.title("Encrypt-It")

        icono=PhotoImage("images/candado.ico")
        self.top.iconbitmap(icono)

        label_bienvenido = Label(self.top, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

        self.engra=PhotoImage(file="images/engra.png")
        button_engra=Button(self.top, image= self.engra, cursor="hand2", activebackground="#D6DBDF", command=self.Levelcaractersuser, relief="flat", border=0, bg="white" )
        button_engra.grid(row=0, column=7, padx=10, pady=10, sticky="e")

        label_texto = Label(self.top, text="Lista de elementos", bg="white", fg="#03989E")
        label_texto.grid(row=6, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",20, "bold"))

        self.cols = ('Contraseña', 'Comentario', 'Tipo')

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview.Heading",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3"
            )
        self.style.map('Treeview', background=[('selected', 'blue')])
        tree_scroll = Scrollbar(self.top)
        tree_scroll.grid(row=7, column=2, sticky="nsew")

        self.my_tree = ttk.Treeview(self.top, yscrollcommand=tree_scroll.set, columns=self.cols, style="mystyle.Treeview")
        self.my_tree.grid(row=7, column=0, padx=(10,0), columnspan=2, rowspan=7)

        tree_scroll.config(command=self.my_tree.yview)

        self.my_tree.heading("#0", text="Nombre", anchor=CENTER)
        self.my_tree.heading("Contraseña", text="Contraseña", anchor=CENTER)
        self.my_tree.heading("Comentario", text="Comentario", anchor=CENTER)
        self.my_tree.heading("Tipo", text="Tipo", anchor=CENTER)

        self.my_tree.column("#0", width=150, stretch=NO)
        self.my_tree.column("Contraseña", anchor=CENTER, width=100)
        self.my_tree.column("Comentario", anchor=CENTER, width=140)
        self.my_tree.column("Tipo", anchor=CENTER, width=140)

        self.my_tree.bind("<Double-1>", self.ventanaclave)
        self.my_tree.bind("<BackSpace>", self.deleterow)
        self.my_tree.bind("<Delete>", self.deleterow)

        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        self.passwordTabler()

        self.remove_one_button = ttk.Button(self.top, text="Crear un nuevo elemento", command=self.Levelanadirelemento, cursor="hand2")
        self.remove_one_button.grid(row= 7,column=6, padx=5, pady=5, sticky="wnse")

        self.remove_one_button = ttk.Button(self.top, text="Ver contraseña", command=self.desencriptar, cursor="hand2")
        self.remove_one_button.grid(row= 8,column=6, padx=5, pady=5, sticky="wnse")

        self.remove_one_button = ttk.Button(self.top, text="Eliminar", command=self.remove_one, cursor="hand2")
        self.remove_one_button.grid(row= 9,column=6, padx=5, pady=5, sticky="wnse")

        self.remove_one_button = ttk.Button(self.top, text="Subir", command=self.up, cursor="hand2")
        self.remove_one_button.grid(row= 10,column=6, padx=5, pady=5, sticky="wnse")

        self.remove_one_button = ttk.Button(self.top, text="Bajar", command=self.down, cursor="hand2")
        self.remove_one_button.grid(row= 11,column=6, padx=5, pady=5, sticky="wnse")

        self.remove_one_button = ttk.Button(self.top, text="Eliminar todo", command=self.remove_all, cursor="hand2")
        self.remove_one_button.grid(row= 12,column=6, padx=5, pady=5, sticky="wnse")

        self.remove_one_button = ttk.Button(self.top, text="Ordenar", command=self.ordenar, cursor="hand2")
        self.remove_one_button.grid(row= 13,column=6, padx=5, pady=5, sticky="wnse")

        self.exitbutton = ttk.Button(self.top, text = "Salir", command = self.exit_btn, cursor="hand2")
        self.exitbutton.grid(row = 14, column = 7, padx = 5, pady = 5, sticky = "wnse")

    def desencriptar(self):
        name = self.my_tree.item(self.my_tree.selection(), "text")
        self.ventanaclave(name)

    def Levelanadirelemento(self):
        self.top.destroy()
        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.engra =PhotoImage(file = "images/engra.png")

        self.topanadir = Toplevel()
        self.topanadir.config(bg="white")
        self.topanadir.resizable(0,0)
        self.topanadir.title("Encrypt-It")

        icono=PhotoImage("images/candado.ico")
        self.topanadir.iconbitmap(icono)

        label_bienvenido = Label(self.topanadir, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

        label_texto = Label(self.topanadir, text="Añadir elemento", bg="white", fg="#03989E")
        label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",20, "bold"))

        label_texto= Label(self.topanadir, text="Nombre/Usuario: ", bg="white", fg="black")
        label_texto.grid(row=2, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        label_texto= Label(self.topanadir, text="Contraseña: ", bg="white", fg="black")
        label_texto.grid(row=3, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        label_texto= Label(self.topanadir, text="Comentario: ", bg="white", fg="black")
        label_texto.grid(row=4, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        label_texto= Label(self.topanadir, text="Tipo de elemento: ", bg="white", fg="black")
        label_texto.grid(row=5, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        self.comboex = ttk.Combobox(self.topanadir,
                            values=[
                                    "Correo electrónico",
                                    "Compras online",
                                    "Redes sociales",
                                    "Entretenimiento",
                                    "Otros"],
                            state = "readonly")

        self.comboex.grid(row = 5, column = 1)
        self.comboex.current(1)

        self.myEntrynombrelevel=ttk.Entry(self.topanadir)
        self.myEntrynombrelevel.grid(row=2, column=1, padx=10)

        self.myEntrycontrasenalevel=ttk.Entry(self.topanadir)
        self.myEntrycontrasenalevel.grid(row=3, column=1, padx=10)

        self.newPasswordList = self.myEntrycontrasenalevel.get()
        self.newNameList = self.myEntrynombrelevel.get()
        self.newcombo = self.comboex.get()

        self.noteText = tk.Text(self.topanadir, width=20,height=3)
        self.noteText.grid(row=4, column=1)
        self.scrollVertNoteText = ttk.Scrollbar(self.topanadir, command=self.noteText.yview)
        self.scrollVertNoteText.grid(row=4, column=2, sticky="nsew")
        self.noteText.config(yscrollcommand=self.scrollVertNoteText.set)

        self.exitbutton = ttk.Button(self.topanadir, text = "Cancel", command = self.salirdeltoplevel, cursor="hand2")
        self.exitbutton.grid(row = 7, column = 4, padx = 5, pady = 5, sticky = "wnse")

        self.exitbutton = ttk.Button(self.topanadir, text = "Guardar", command = self.insertNewPasswordlevel, cursor="hand2")
        self.exitbutton.grid(row = 6, column = 0, columnspan= 5,  padx = 70, pady = 10, sticky = "wnse")

    def remove_one(self):
        total = len(self.my_tree.get_children())
        if (total > 0):
            self.mail = self.myEntryLoginmail.get()
            name = self.my_tree.item(self.my_tree.selection(), "text")
            answerr = messagebox.askquestion("Eliminar contraseña", "Está seguro que quiere eliminar la contraseña?")
            row_selected = self.my_tree.selection()
            try:
                if answerr == "yes":
                    database.deletePassword(self.mail, name)
                    self.my_tree.delete(row_selected)
            except IndexError:
                messagebox.showwarning("Error", "Seleccione el nombre que quiere eliminar. También lo puede eliminar con el botón Suprimir.")
        else:
            messagebox.showwarning("Error", "Tiene que haber como mínimo un elemento para poder eliminarlos.")

    def up(self):
        try:
            rows = self.my_tree.selection()
            for row in rows:
                self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)-1)
        except IndexError:
            messagebox.showwarning("Error", "Seleccione el nombre que quiere eliminar. También lo puede eliminar con el botón Suprimir.")

    def down(self):
        try:
            rows = self.my_tree.selection()
            for row in reversed(rows):
                self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)+1)
        except IndexError:
            messagebox.showwarning("Error", "Seleccione el nombre que quiere eliminar. También lo puede eliminar con el botón Suprimir.")

    def remove_all(self):
        total = len(self.my_tree.get_children())
        if (total > 2):
            self.mail = self.myEntryLoginmail.get()
            a = messagebox.askquestion('Eliminar todo','¿Está seguro que quiere eliminar todo?', icon = 'warning')
            if a == 'yes':
                database.deleteallPassword(self.mail)
                for record in self.my_tree.get_children():
                    # self.my_tree.delete(row_selected)
                    self.my_tree.delete(*self.my_tree.get_children())
        else:
            messagebox.showwarning("Error", "Tienen que haber como mínimo dos elementos para poder eliminarlos todos")

    def ordenar(self):
        total = len(self.my_tree.get_children())
        if (total > 1):
            self.my_tree.delete(*self.my_tree.get_children())
            self.mail = self.myEntryLoginmail.get()
            self.tempList = database.readPasswords2(self.mail)
            nombres = database.seleccionarnombre(self.mail)

            for  i in range(len(nombres)):
                aux = i
                for j in range(i+1, len(nombres)):
                    if nombres[aux] > nombres[j]:
                        aux = j
                nombres[i], nombres[aux] = nombres[aux], nombres[i]

            for i, (password, notes, tipo) in enumerate(self.tempList, start=1):
                decoded_pass = "••••••••"
                self.my_tree.insert("", "end", text=nombres[i-1], values=(decoded_pass, notes.partition('\n')[0], tipo))
        else:
            messagebox.showwarning("Error", "Para ordenar por nombre los elementos tienen que haber como mínimo 2.")

    def exit_btn(self):
        self.top.destroy()
        self.top.update()
        self.mail = ""
        self.myEntryLoginmail.delete(0, 'end')
        self.password = ""
        self.myEntryLoginpw.delete(0, 'end')
        app.change(PageOne)
        app.show()

    def passwordTabler(self):
        if self.estado == 0:
            self.mail = self.myEntryLoginmail.get()
            self.tempList = database.readPasswords(self.mail)

            for i, (name, password, notes, tipo) in enumerate(self.tempList, start=1):
                decoded_pass = "••••••••"
                self.my_tree.insert("", "end", text=name, values=(decoded_pass, notes.partition('\n')[0], tipo))
        else:
            self.mail = self.myEntryLoginmail.get()
            self.tempList = database.readPasswords(self.mail)

            for i, (name, password, notes, tipo) in enumerate(self.tempList, start=1):
                decoded_pass = database.cipher_suite.decrypt(password)
                decoded_pass = decoded_pass.decode("utf-8")
                self.my_tree.insert("", "end", text=name, values=(decoded_pass, notes.partition('\n')[0]))

    def insertNewPassword(self):
        self.mail = self.myEntryLoginmail.get()
        self.newNameList = self.myEntrynombrelevel.get()
        self.newPasswordList = self.myEntrycontrasenalevel.get()
        self.newcombo = self.comboex.get()

        if self.newPasswordList.isspace() or self.newPasswordList == "" or self.newNameList.isspace() or self.newNameList == "":
            messagebox.showwarning("Warning!", "El nombre o contraseña no pueden estar vacíos.")
        else:
            # database.insertPasswordData(self.mail, self.newNameList, self.newPasswordList, self.noteText.get("1.0", 'end-1c'))
            database.insertPasswordData(self.mail, self.newNameList, self.newPasswordList, self.noteText.get("1.0", 'end-1c'), self.newcombo)
            self.myEntrynombrelevel.delete(0, END)
            self.myEntrycontrasenalevel.delete(0, END)
            self.noteText.delete(1.0, tk.END)
            messagebox.showinfo("Felicidades!", "Nueva contraseña añadida exitosamente!")
            self.my_tree.delete(*self.my_tree.get_children())
            self.passwordTabler()

    def insertNewPasswordlevel(self):
        # Add new password to the storage
        self.mail = self.myEntryLoginmail.get()
        self.newNameList = self.myEntrynombrelevel.get()
        self.newPasswordList = self.myEntrycontrasenalevel.get()
        self.newcombo = self.comboex.get()

        if self.newPasswordList.isspace() or self.newPasswordList == "" or self.newNameList.isspace() or self.newNameList == "":
            messagebox.showwarning("Warning!", "El nombre o contraseña no pueden estar vacíos.")
        else:
            database.insertPasswordData(self.mail, self.newNameList, self.newPasswordList, self.noteText.get("1.0", 'end-1c'), self.newcombo)
            self.myEntrynombrelevel.delete(0, END)
            self.myEntrycontrasenalevel.delete(0, END)
            self.noteText.delete(1.0, tk.END)
            messagebox.showinfo("Felicidades!", "Nueva contraseña añadida exitosamente!")
            self.LevelLista()
            self.topanadir.destroy()

    def deleterow(self, event):
        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.mail = self.myEntryLoginmail.get()

        """Delete a password after press the backspace key or delete key from the keyboard"""
        name = self.my_tree.item(self.my_tree.selection(), "text")
        row_selected = self.my_tree.selection()

        answer = messagebox.askquestion("Eliminar contraseña", "Está seguro que quiere eliminar "+name+" la contraseña?")
        if answer == "yes":
            database.deletePassword(self.mail, name)
            self.my_tree.delete(row_selected)

    def salirdeltoplevel(self):
        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.topanadir.destroy()
        self.LevelLista()

    def Levelcaractersuser(self):
        self.top.destroy()
        self.logopequeno=PhotoImage(file="imamges/logopequeño.png")

        self.engra =PhotoImage(file = "imamges/engra.png")
        self.topcaracter = Toplevel()
        self.topcaracter.config(bg="white")
        self.topcaracter.resizable(0,0)
        self.topcaracter.title("Encrypt-It")

        icono=PhotoImage("imamges/candado.ico")
        self.topcaracter.iconbitmap(icono)

        label_bienvenido = Label(self.topcaracter, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

        label_texto = Label(self.topcaracter, text="Mi perfil", bg="white", fg="#03989E")
        label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",20, "bold"))

        label_texto = Label(self.topcaracter, text="Nombre: ", bg="white", fg="black")
        label_texto.grid(row=2, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        nombre = database.readnombre(self.mail)

        label_texto = Label(self.topcaracter, text=nombre[0][0], bg="white", fg="black")
        label_texto.grid(row=2, column= 1, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))


        label_texto = Label(self.topcaracter, text="Mail: ", bg="white", fg="black")
        label_texto.grid(row=3, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        mail = database.readmail(self.mail)

        label_texto = Label(self.topcaracter, text=nombre[0][0], bg="white", fg="black")
        label_texto.grid(row=3, column= 1, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        exitbutton = ttk.Button(self.topcaracter, text = "Salir", command = self.salirdelcaracter, cursor="hand2")
        exitbutton.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "wnse")

    def salirdelcaracter(self):
        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.topcaracter.destroy()
        self.LevelLista()

    def ventanaemergente(self):
        self.logopequeno=PhotoImage(file="images/logopequeño.png")
        self.topclave.destroy()
        name = self.my_tree.item(self.my_tree.selection(), "text")

        notes = database.readNotes(self.mail, name)
        nombre = database.readName(self.mail, name)
        contra = database.readContradesencriptada(self.mail, name)

        contra = database.cipher_suite.decrypt(contra[0][0])

        if not notes:
            pass
        else:
            self.logopequeno=PhotoImage(file = "images/ogopequeño.png")
            self.venemer = Toplevel()
            self.venemer.config(bg="white")
            self.venemer.resizable(0,0)
            self.venemer.title("Encrypt-It")

            icono=PhotoImage("images/candado.ico")
            self.venemer.iconbitmap(icono)

            label_texto = Label(self.venemer, image=self.logopequeno, bg="white", fg="#03989E")
            label_texto.grid(row=0, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",20, "bold"))

            label_texto = Label(self.top, image=self.logopequeno, bg="white", fg="#03989E")
            label_texto.grid(row=0, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",20, "bold"))

            label_nombre = tk.Label(self.venemer, text=notes[0][0], bg="white")
            label_nombre.grid(row=3, column = 1, padx = 10, pady=10, sticky="w")
            label_nombre.config(font=("Source Sans Pro",12))

            label_texto= Label(self.venemer, text="Comentario: ", bg="white", fg="black")
            label_texto.grid(row=3, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",12))

            label_nombre = tk.Label(self.venemer, text=nombre[0][0], bg="white")
            label_nombre.grid(row=2, column = 1, padx = 10, pady=10, sticky="w")
            label_nombre.config(font=("Source Sans Pro",12))

            label_texto= Label(self.venemer, text="Nombre: ", bg="white", fg="black")
            label_texto.grid(row=2, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",12))

            label_nombre = tk.Label(self.venemer, text=contra, bg="white")
            label_nombre.grid(row=1, column = 1, padx = 10, pady=10, sticky="w")
            label_nombre.config(font=("Source Sans Pro",12))

            label_texto= Label(self.venemer, text="Contraseña: ", bg="white", fg="black")
            label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
            label_texto.config(font=("Source Sans Pro",12, "bold"))

    def ventanaclave(self, event):
        self.logopequeno=PhotoImage(file="images/logopequeño.png")

        self.topclave = Toplevel()
        self.topclave.config(bg="white")
        self.topclave.resizable(0,0)
        self.topclave.title("Encrypt-It")

        icono=PhotoImage("images/candado.ico")
        self.topclave.iconbitmap(icono)

        label_bienvenido = Label(self.topclave, image=self.logopequeno, bg="white")
        label_bienvenido.grid(columnspan=3, row=0, column=0, pady=10,padx=10, sticky="w")

        label_texto = Label(self.top, image=self.logopequeno, bg="white", fg="#03989E")
        label_texto.grid(row=0, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",20, "bold"))

        label_texto = Label(self.topclave, text="Introduzca la clave", bg="white", fg="#03989E")
        label_texto.grid(row=1, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",20, "bold"))

        label_texto= Label(self.topclave, text="Clave: ", bg="white", fg="black")
        label_texto.grid(row=2, column= 0, padx = 10, pady=10, sticky="w")
        label_texto.config(font=("Source Sans Pro",12))

        self.EntryClaveven=ttk.Entry(self.topclave)
        self.EntryClaveven.grid(row=2, column=1, padx=10)

        self.entryclaveven = self.EntryClaveven.get()

        self.exitbutton = ttk.Button(self.topclave, text = "Ok", command = self.gotovenemer, cursor="hand2")
        self.exitbutton.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "wnse")

    def gotovenemer(self):
        check_counter=0
        warn = ""
        self.entryclaveven = self.EntryClaveven.get()

        if self.entryclaveven == "":
            warn = "El campo de clave es obligatorio."
        else:
            check_counter += 1

        if check_counter == 1:
            try:
                valuee = database.loginClave(self.mail , self.entryclaveven)
                if valuee == "yes":
                    self.ventanaemergente()
                else:
                    messagebox.showwarning("Clave incorrecta", "Clave incorrecta")

            except Exception as ep:
                messagebox.showwarning('', ep)
        else:
            messagebox.showwarning('Error', warn)

if __name__ == "__main__":
    database.crearBD()
    app = App()
    app.root.mainloop()
