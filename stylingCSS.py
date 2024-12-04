from nicegui import ui

ui.icon('thumb_up', color='#d11111').classes('text-6xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Reyna').style('color: #0e0775; font-weight: bold; font-family: "Times New Roman"; font-size: 24px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()