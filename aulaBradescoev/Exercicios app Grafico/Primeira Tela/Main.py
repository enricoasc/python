'O Kivy tem muitas dependências, portanto, é recomendável instalá-lo em um ambiente virtual Python (venv).'
'Você pode usar a biblioteca interna do Python ou o pacote “virtualenv”.'
# Observe abaixo, como deve executar o virtualenv via linha de comando:
#
# python3 -m venv kivy_project

# Ele copiará seu executável do Python 3 em uma pasta chamada my_kivy_projecte e adicionará algumas outras subpastas a esse diretório.
#
# Para usar seu ambiente virtual, é necessário ativá-lo. No Mac e no Linux, você pode fazer isso executando o seguinte comando dentro da pasta kivy_project:
#
# source  bin/activate
# O comando para Windows é semelhante, mas o local do script de ativação está dentro da pasta Scripts, em vez de bin.
#
# Agora que você tem um ambiente virtual Python ativado, pode executar pip para instalar o Kivy. No Linux e no Mac, para isso execute o seguinte comando:
#
# python -m pip install kivy'

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='Fala Galera!!',size_hint=(.5,.5),pos_hint = {'center_x':.5,'center_y':.5})

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
