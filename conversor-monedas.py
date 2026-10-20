import flet as ft
def main(page: ft.Page):
    page.title = "Conversor de monedas"
    imagen = ft.Image(src="/logo.png", width=200, height=200)

    cantidad = ft.TextField(label="Cantidad", value="0")
    moneda_origen = ft.Dropdown(
        label="Moneda de origen",
        options=[
            ft.dropdown.Option("Dólares"),
            ft.dropdown.Option("Pesos")
        ]
    )
    moneda_destino = ft.Dropdown(
        label="Moneda de destino",
        options=[
            ft.dropdown.Option("Dólares"),
            ft.dropdown.Option("Pesos")
        ]
    )
    resultado = ft.Text("Resultado: 0")

    def convertir(e):
        try:
            cantidad_valor = float(cantidad.value)
            origen = moneda_origen.value
            destino = moneda_destino.value

            if origen == "Dólares" and destino == "Pesos":
                conversion = cantidad_valor * 1500
            elif origen == "Pesos" and destino == "Dólares":
                conversion = cantidad_valor / 1500
            else:
                conversion = cantidad_valor 

            resultado.value = f"Resultado: {conversion:.2f} {destino}"
        except ValueError:
            resultado.value = "Ingresa una cantidad válida."
        page.update()

    boton_convertir = ft.Button("Convertir", on_click=convertir)

    page.add(
        imagen,
        cantidad,
        moneda_origen,
        moneda_destino,
        boton_convertir,
        resultado
    )
ft.run(main,assets_dir="assets")