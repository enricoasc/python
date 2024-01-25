# Para instalar o virtualenv, digite a linha decomando pip install virtualenv?

# Para começar a utilizar o ambiente, digiteo comando: python3 –m venv venv

# Agora, seu projeto tem seu próprio ambientevirtual. Geralmente, antes de
# começar a usá-lo,você primeiro ativará o ambiente executandoum script que
# acompanha a instalação: $ source venv/bin/activate(venv)

# Para instalar pacotes externos do Python com pip, utilize o comando padrão:
# (venv) $ python -m pip install <nome do pacote>

# Quando terminar de trabalhar com esse ambiente virtual, você pode desativá-lo utilizando o comando:
# (venv) $ deactivate
# $

# Exemplo :
# $ mkdir cliente-1
# $ cd cliente-1
# $ python3 -m venv venv --prompt="cliente-1"
# $ source venv/bin/activate
# (cliente-1) $ python -m pip install django==2.2.26
# (cliente-1) $ python -m pip list
#   Package Version
#   ---------- -------
#   Django 2.2.26
#   pip 22.0.4
#   pytz 2022.1
#   setuptools 58.1.0
#   sqlparse 0.4.2
# (cliente-1) $ deactivate
# $ cd ..
# $ mkdir cliente-2
# $ cd cliente-2
# $ python3 -m venv venv --prompt="cliente-2"
# $ source venv/bin/activate
# (cliente-2) $ python -m pip install django==4.0.3
# (cliente-2) $ python -m pip list
#   Package Version
#   ---------- -------
#   asgiref 3.5.0
#   Django 4.0.3
#   pip 22.0.4
#   setuptools 58.1.0
#   sqlparse 0.4.2
#   (cliente-2) $ deactivate
#   -------------------------------------

lista=[8,9]
print(lista)
lista.append(10)
print(lista)
lista.append('palavra')
print(lista)
lista.append(True)
print(lista)


