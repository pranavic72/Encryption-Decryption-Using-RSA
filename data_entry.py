import pandas as pd
import PySimpleGUI as sg

EXCEL_FILE = 'data_entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please fill the form:')],
    [sg.Text('Name:',size=(15,1)),sg.InputText(key='Name')],
    [sg.Text('Email:',size=(15,1)),sg.InputText(key='Email')],
    [sg.Text('Phone:',size=(15,1)),sg.InputText(key='Phone')],
    [sg.Text('Address:',size=(15,1)),sg.InputText(key='Address')],
    [sg.Text('Aadhar Card No:',size=(15,1)),sg.InputText(key='Aadhar')],
    [sg.Submit(),sg.Button('Clear')]
]

window = sg.Window('Simple data entry form',layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
window.close()