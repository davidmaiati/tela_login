from PySimpleGUI import PySimpleGUI as sg

def usuario(x):
    return x

def senha(y):
    return y

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janelas
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
            print('Bem vindo ao mundo de David!')


