from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz clic', on_click=lambda: ui.notify('Hiciste clic...'))
with ui.row():
    ui.checkbox('Acepto los términos...', on_change=show)
    ui.switch('Activado/Desactivado', on_change=show)
ui.radio(['Mapache', 'Gato', 'Perro'], value='Mapache', on_change=show).props('inline')
with ui.row():
    ui.input('Escribe tu nombre...', on_change=show)
    ui.select(['ISC', 'IGE', 'Ingenieria Mecánica', 'ITIC'], value='ISC', on_change=show)
ui.link('Para más información...', '/documentation').classes('mt-8')

ui.run()