from nicegui import ui

# .classes() to make stylistic changes
# go to website tailwind.build/classes to see what classes you can add
with ui.row().classes("mx-auto"): # mx-auto = automatically apply equal margins on the left and right side of this object
    with ui.card():
        input_field = ui.input(
            on_change=lambda e: result.set_text(e.value.lower()))
        result = ui.label()

ui.run()