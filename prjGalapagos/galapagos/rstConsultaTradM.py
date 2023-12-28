import pandas as pd
# from openpyxl import load_workbook
from flask import Flask, jsonify

print("## 1 - Inicia servidor wbserver")  
print("## --------------------------------------------")
print("##                             ")


# :: INSTANCIA VARIAVEL DE API
# ============================================
app = Flask(__name__)


# :: FUNÇÃO DE LETURA EXCEL
# ============================================
@app.route('/cgccon/<string:cgc>',methods=['GET'])
def cgccon(cgc):
  tabela = pd.read_excel('limites.xlsx')
  tabela_df = pd.DataFrame(tabela)
  # result_tb = tabela_df.loc[tabela_df['CNPJ'] == cgc]
  result_tb = tabela_df.loc[tabela_df['CNPJ'] == cgc,['CNPJ','Cliente','Limite Trademaster','Limite Utilizado','Limite Disponível','Prazo (dias)']]
  data = result_tb.to_dict()
  return jsonify(data)

# :: HOMEPAGE 
# ============================================
@app.route('/')
def home():
  return 'no ar'

# :: SUBIR O SERVIÇO API 
# ============================================
#def upServer():
#  return 
app.run(host="0.0.0.0")
