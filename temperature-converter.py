from nicegui import ui

ui.colors(
      primary='#889fc2',
      secondary='#7d7d7d',
      accent='#997dff',
      positive='#85ed9d',
      negative='#c93244',
      info='#a5e5f2',
      warning='#f29b38'
)

ui.query("body").classes("bg-gradient-to-br from-sky-300 to-violet-500")

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: Sets the text color to the hex code defined for positive
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: Sets the text color to the hex code defined for negative

def convertSlider():
    try: 
        temp = float(slider.value)
        if slider_conversion_type.value == "Celsius to Fahrenheit":
            slider_result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            slider_result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        slider_result_label.classes("text-lg font-semibold text-positive mt-4")
    except ValueError:
        slider_result_label.set_text("Please enter a valid number.")
        slider_result_label.classes("text-lg font-semibold text-negative mt-4")


with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Adds padding of 6 on all sides of the element
        # shadow-xl: Adds an extra large outer box shadow
        # mx-auto: Sets the inline (horizontal) margin to auto (equal on each side)
        # mt-10: Adds a margin of 10 to the top
        # rounded-xl: Applies an extra large border radius size (12px)
        ui.label("Temperature Input").classes("text-2xl font-bold text-accent mb-4 px-1 uppercase")
        # text-2xl: Sets the font size to be 2XL (24px)
        # font-bold: Sets the font weight to 700
        # text-accent: Sets the text color to the hex code defined for accent
        # mb-4: Adds a margin of 4 to the bottom
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded border-violet-400 font-mono")
        # w-full: Set element width to 100% (of the screen)
        # border: Sets border width to 1px for all sides of the element
        # rounded: Applies a small border radius to the element
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-3")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold px-4 rounded mx-auto shadow-lg italic")
        # text-white: Sets the text color to white
        # py-2: Adds vertical padding of 2
        # px-4: Adds horizontal padding of 4
        result_label = ui.label("").classes("text-lg mt-4")

    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        ui.label("Temperature Slider").classes("text-2xl font-bold text-accent mb-4 uppercase")
        slider = ui.slider(min=-1000, max=1000, value=0).props('label-always').classes("py-7").on('update:model-value', convertSlider)
        slider_conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("pt-1 mb-4 pb-12")
        slider_result_label = ui.label("").classes("text-lg mt-4")

ui.run()

# Additional Tailwind styles added
# 1. background gradient (bg-gradient-to-br from-sky-300 to-violet-500)
# 2. border color on enter temperature box (border-violet-400)
# 3. centering convert button (mx-auto)
# 4. shadow on convert button (shadow-lg)
# 5. italic text on convert button (italic)
# 6. uppercase temperature converter text (uppercase)
# 7. mono font for enter temperature (font-mono)