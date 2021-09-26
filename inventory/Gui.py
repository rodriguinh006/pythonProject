from tkinter import *
from tkinter import StringVar


class Gui:
    # Create window
    window = Tk()
    window.wm_tittle("Cadastro Cliente")

    # Data Storage
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()


    #Create Labels syde by camp
    lblnome = Label(window, text='Nome')
    lblsobrenome = Label(window, text='Sobrenome')
    lblemail = Label(window, text='Email')
    lblcpf = Label(window, text='CPF')

    #Input camp
    entNome = Entry(window, textvariable=txtNome)
    entSobrenome = Entry(window, textvariable=txtSobrenome)
    entEmail = Entry(window, textvariable=txtEmail)
    entCPF = Entry(window, textvariable=txtCPF)

    #Listbox
    listClientes = Listbox(window)

    #scroll
    scrollClientes = Scrollbar(window)

    #bottons in the interfce
    btnViewAll = Button(window, tex='Ver Todos')
    btnBuscar = Button(window, text='Buscar')
    btnInserir = Button(window, text='Inserir')
    btnUpdate = Button(window, text='Atualizar Selecionados')
    btnDel = Button(window, text='Deletar Selecionados')
    btnClose = Button(window, text='Fechar')

    #position oh the window whith grid
    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=9, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)


    #Associate scrollbar in Listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)

    scrollClientes.configure(command=listClientes.yview)

    #Swag elements
    x_pad = 5
    y_pad = 3
    width_entry = 30


    for child in window.winfo_children():
        widget_class = child.__class__.__nome__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')



