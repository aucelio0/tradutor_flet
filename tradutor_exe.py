import flet as ft
from deep_translator import GoogleTranslator

def main(page: ft.Page):
    def acao(e):
        tradutor = GoogleTranslator(source='auto', target='pt')

        try:
            # Pega o texto do campo de entrada
            texto_original = texto.value
            # Traduz o texto
            texto_traduzido = tradutor.translate(texto_original)
            # Atualiza o campo de tradução
            traducao.value = texto_traduzido
        except Exception as ex:
            traducao.value = 'Não foi possível traduzir' + str(ex)
            
        page.update()
    
    page.title = 'Tradutor'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.DARK   
    
    texto = ft.TextField(label='Insira o texto', multiline=True,    width=400)
    traducao = ft.Text(size=30, color='red')
    
    page.add(
    ft.Row(
            [ft.Text('Tradutor Português', size=40, weight='bold', color='blue')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ft.Row(
            [texto],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ft.Row(
            [ft.ElevatedButton('Traduzir Texto', on_click=acao)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ft.Row(
            [traducao],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.update()
    
ft.app(target=main)