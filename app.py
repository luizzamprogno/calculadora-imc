import PySimpleGUI as sg

def calculate_imc(weight, height):

    weight = float(weight)
    height = float(height)

    imc = round(weight / (height**2),2)
    return imc

def get_imc_category(imc):

    if imc is None:
        return ''
    if imc <= 17:
       return 'Muito abaixo do peso'
    elif imc > 17 and imc <= 18.5:
        return 'Abaixo do peso'
    elif imc >18.5 and imc <= 24.9:
        return 'Peso normal'
    elif imc >24.9 and imc <= 29.9:
        return 'Acima do peso'
    elif imc >29.9 and imc <= 34.9:
        return 'Obesidade I'
    elif imc >34.9 and imc <= 39.9:
        return 'Obesidade II (severa)'
    else:
        return 'Obesidade III (mórbida)'

def main():

    # Tema
    sg.theme('LightGrey6')

    # Layout
    layout = [
        [sg.Text('Calcule o seu IMC')],
        [sg.Text('Seu peso (kg): '), sg.Input(key='peso')],
        [sg.Text('Altura (m): '), sg.Input(key='altura')],
        [sg.Button(button_text='CALCULAR')],
        [sg.Text('', key='resultado')],
        [sg.Text('', key='resposta')]
    ]
    # Janela
    window = sg.Window('Calculadora de IMC', layout=layout)

    # Leitura de eventos e valores
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'CALCULAR':
            peso = values['peso']
            altura = values['altura']
            imc = calculate_imc(peso, altura)
            if imc is not None:
                window['resultado'].update(f'Seu IMC: {imc}')
                window['resposta'].update(get_imc_category(imc))

if __name__ == '__main__':
    main()