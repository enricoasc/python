import pandas as pd

disciplinas = { 'cursos' : ['estatistica', 'economia', 'calculo', 'geometria'],
              'créditos' : ['90','60','90','40'],
              'requisito' : [True, False, True, False]
             }
data = pd.DataFrame(disciplinas)

print(data)