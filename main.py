import tkinter as tk

#Crear la ventana principal
root = tk.Tk()
root.title('Calculadora')

#Configurar el tamaño de la ventana
root.geometry('400x600')

#Crear la pantalla de entrada
screen = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief='solid')
screen.grid(row=0, column=0, columnspan=4)

#Definir los botones de la calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

#Crear los botones y colocarlos en la cuadricula
current_row = 1
current_column = 0


for button in buttons:
    tk.Button(screen, text=button, font=('Arial', 18), command=lambda b=button: click_button(b)).grid(
        row=current_row, column=current_column, sticky='nsew')
    current_column += 1 
    if current_column > 3:
        current_column = 0
        current_row += 1

#Configurar la expansion de la cuadricula para que los botones se ajusten al tamaño de la ventana
for i in range(4):
    screen.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    screen.grid_rowconfigure(i, weight=1)

#Funcion para manejar los eventos de los botones 
def click_button(value):
    current = eval(screen.get())
    screen.delete(0, tk.END)
    screen.insert(0,current + value )

#Funcion para calcular el resultado
def click_equal():
    try:
        result = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(0, str(result))
    except:
        screen.delete(0, tk.END)
        screen.insert(0, 'Error')

#Funcion para limpiar la pantalla
def click_clean():
    screen.delete(0, tk.END)

screen.mainloop()