import PySimpleGUI as sg

feet_label = sg.Text("Enter Feet:")
feet_input_box = sg.InputText(key="feet", tooltip="Enter a Feet Value")

inches_label = sg.Text("Enter Inches")
inches_input_box = sg.InputText(key="inches", tooltip="Enter an Inches Value")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Imperial to Metric Converter", 
                   layout=[[feet_label, feet_input_box], 
                           [inches_label, inches_input_box], 
                           [convert_button, output_label]])

while True:
    try:
        event, values = window.read()
        print(event, values)

        feet = int(values["feet"])
        inches = int(values["inches"])

        meters_result = feet * .3048 + inches * .0254
        window["output"].update(value=f"Your result is {meters_result} meters!")
    
    except TypeError:
        break # Exit() would terminate the program entirely, skipping the below lines.


window.close()