from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('Ver/Ocultar', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=5).bind_value(demo, 'number')
    ui.toggle({1: 'POO', 2: 'Discretas', 3: 'Probabilidad', 4: 'Álgebra', 5: 'Química'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()