import flet as ft
def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 400
    def cambiar_texto(e):
        texto.value = "¡Has hecho clic en el botón!"
        page.update()
    texto = ft.Text("¡Hola, Flet!")
    boton = ft.Button("Click me!", on_click=cambiar_texto)
    page.add(texto, boton)
ft.run(main)
