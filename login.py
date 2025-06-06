import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
[sg.Text('Usuario'), sg.Input(key='usuario')],
[sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
 [sg.Checkbox('Salvar o login?')],
[sg.Button('Entrar')]
]

# Janela

janela =sg.Window('Login', layout)

#Ler ps eventos
while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'marcos' and valores['senha'] == '123456':
            sg.popup('Bem vindo, Marcos')
        else:
            sg.popup('Usuário ou senha inválidos')
            