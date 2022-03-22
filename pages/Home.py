from tkinter import *


class Home:

    def __init__(self, window=None):
        self.window = janela

        self.window.title("Supermercado")
        self.window.geometry('500x500')

        # self.container = Frame(window)
        # self.container.grid(row=0, column=0)

        # self.clientsContainer = Frame(self.window, bg='lightgray')

        # self.clientsPhoto = PhotoImage(
        #     file="assets/icons/people-icon.png")
        # self.button = Button(
        #     self.clientsContainer, text='Have a Nice Day !', image=self.clientsPhoto)
        # self.button.grid(row=0, column=0)
        # self.clientsContainer.grid(row=0, column=0)

        self.clientsPhoto = PhotoImage(
            file="assets/icons/people-icon.png", width=50, height=50)
        self.l3 = Label(self.window, image=self.clientsPhoto)
        self.l3.image = self.clientsPhoto
        self.l3.grid(
            column=0, row=0)

# self.clientsText = Button(
#     self.clientsContainer, text="Clientes", image=self.clientsPhoto)
# self.clientsText.grid(row=2, column=2)
# self.clientsContainer.grid(row=1, column=0)

# self.inventoryButton = Label(
#     self.window, text="Estoque", background='lightgray')
# self.inventoryButton.grid(row=1, column=2)

# self.employeesButton = Label(
#     self.window, text="Funcionários", background='lightgray')
# self.employeesButton.grid(row=1, column=3)


janela = Tk()
Home(janela)
janela.mainloop()
