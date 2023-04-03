import PySimpleGUI as sg
import qrcode

layout = [[sg.Text('Enter text:'), sg.InputText(key= 'input')],
          [sg.Button('Create', key = 'create'), sg.Button('Exit', key = 'exit')]]


window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'exit':
        break
    
    if event == 'create':
        text = values['input']


qr = qrcode.QRCode(version=2, box_size=12, border=4)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.show()


try:
    img.show()
except:
    sg.popup_error("Error: Unable to generate QR code.")
finally:
    print('QR code generated successfully')

window.close()