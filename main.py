# ejemplo de un cuadro de texto, un botón y un saludo
import flet as ft
def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 400

    def cambiar_texto(e):
        if txt_nombre.value.strip() == "":
            mensaje.value = "¡Por favor, ingresa tu nombre!"
        else:
            mensaje.value = f"¡Hola, {txt_nombre.value}!"
        page.update()

    mensaje = ft.Text("¡Hola, Flet!")
    txt_nombre = ft.TextField(label="Ingresa tu nombre")    
    btn_boton = ft.Button("Click me!", on_click=cambiar_texto)

    page.add(txt_nombre, btn_boton, mensaje)
ft.run(main)