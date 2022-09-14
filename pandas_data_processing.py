import pandas as pd
import numpy as np
from datetime import datetime

encoding = 'utf-8-sig'

pd.set_option('display.max_columns', None)

allUsers = pd.read_csv('allUsers.csv', encoding=encoding, engine='python', sep=",")
a1 = pd.read_csv("HojaDeInformacinDelP_DATA_2022-08-12_1148.csv", encoding=encoding, engine='python',sep=";")
a1.drop('record_id', axis=1, inplace=True)
b1 =pd.read_csv("FormularioDeRecogida_DATA_2022-08-12_1148.csv", encoding=encoding, engine='python', sep=";")
b1.drop('record_id', axis=1, inplace=True)
b3 =pd.read_csv("MemoryFailuresOfEver_DATA_2022-08-12_1147.csv", encoding=encoding, engine='python', sep=";")
b3.drop('record_id', axis=1, inplace=True)
c1=pd.read_csv("CuestionarioDeSaludG_DATA_2022-08-12_1150.csv", encoding=encoding,  engine='python', sep=";")
c1.drop('record_id', axis=1, inplace=True)
c2=pd.read_csv("EscalaESTEIIAnexoC2_DATA_2022-08-12_1149.csv", encoding=encoding,  engine='python', sep=";")
c2.drop('record_id', axis=1, inplace=True)
b2=pd.read_csv("CuestionarioDeAcepta_DATA_2022-08-12_1147.csv", encoding=encoding,  engine='python', sep=";")
b2.drop('record_id', axis=1, inplace=True)

c3=pd.read_csv("SUSCuestionarioDeExp_DATA_2022-08-12_1147.csv", encoding=encoding,  engine='python', sep=";")
c3.drop('record_id', axis=1, inplace=True)
c4=pd.read_csv("CuestionarioFinalPil_DATA_2022-08-12_1148.csv", encoding=encoding,  engine='python', sep=";")
c4.drop('record_id', axis=1, inplace=True)


output1 = pd.merge(allUsers, a1, on="redcap_survey_identifier", how="left")
output1 = pd.merge(output1, b1, on="redcap_survey_identifier", how="left")
output1 = pd.merge(output1, b3, on="redcap_survey_identifier", how="left")
output1 = pd.merge(output1, c1, on="redcap_survey_identifier", how="left")
output1 = pd.merge(output1, c2, on="redcap_survey_identifier", how="left")
output1 = pd.merge(output1, b2, on="redcap_survey_identifier", how="left")

output1.round(0)


prueba25 = pd.read_csv("prueba_25_initial_evaluation.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")
prueba26 = pd.read_csv("prueba_26_initial_evaluation.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")
prueba27 = pd.read_csv("prueba_27_initial_evaluation.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")
prueba28 = pd.read_csv("prueba_28_initial_evaluation.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")
prueba29 = pd.read_csv("prueba_29_initial_evaluation.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")
prueba30 = pd.read_csv("prueba_30_initial_evaluation.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")
prueba25_post = pd.read_csv("prueba_25_initial_evaluation_post.csv", usecols=["nombre","id_user", "aciertos","fallos","tiempo", "fecha", "dificultad"], encoding=encoding, engine='python',sep=";")

prueba25["fecha"] = pd.to_datetime(prueba25["fecha"])
prueba26["fecha"] = pd.to_datetime(prueba26["fecha"])
prueba27["fecha"] = pd.to_datetime(prueba27["fecha"])
prueba28["fecha"] = pd.to_datetime(prueba28["fecha"])
prueba29["fecha"] = pd.to_datetime(prueba29["fecha"])
prueba30["fecha"] = pd.to_datetime(prueba30["fecha"])
prueba25_post["fecha"] = pd.to_datetime(prueba25_post["fecha"])

activityValues = pd.DataFrame(columns = ["nombre", 
                                         "PREVALORACION alfa o beta",
                                         "PREVALORACION tiempo total",  
                                         "Logogramas Pre Aciertos",
                                         "Logogramas Pre Fallos",
                                         "Logogramas Pre Tiempo",
                                         "Lista de palabras 1 Pre Aciertos", 
                                         "Lista de palabras 1 Pre Fallos", 
                                         "Lista de palabras 1 Pre Tiempo", 
                                         "Fichas Pre Aciertos",
                                         "Fichas Pre Fallos",
                                         "Fichas Pre Tiempo",
                                         "Escenas Pre Aciertos",
                                         "Escenas Pre Fallos",
                                         "Escenas Pre Tiempo",
                                         "Secuencias Pre Aciertos",
                                         "Secuencias Pre Fallos",
                                         "Secuencias Pre Tiempo",
                                         "Calculo Pre Aciertos",
                                         "Calculo Pre Fallos",
                                         "Calculo Pre Tiempo",
                                         "Lista de palabras 2 Pre Aciertos", 
                                         "Lista de palabras 2 Pre Fallos",
                                         "Lista de palabras 2 Pre Tiempo",
                                         "POSTVALORACION alfa o beta",
                                         "POSTVALORACION tiempo total",  
                                         "Logogramas POST Aciertos",
                                         "Logogramas POST Fallos",
                                         "Lista de palabras 1 POST Aciertos", 
                                         "Lista de palabras 1 POST Fallos", 
                                         "Lista de palabras 1 POST Tiempo", 
                                         "Fichas POST Aciertos",
                                         "Fichas POST Fallos",
                                         "Fichas POST Tiempo",
                                         "Escenas POST Aciertos",
                                         "Escenas POST Fallos",
                                         "Escenas POST Tiempo",
                                         "Secuencias POST Aciertos",
                                         "Secuencias POST Fallos",
                                         "Secuencias POST Tiempo",
                                         "Calculo POST Aciertos",
                                         "Calculo POST Fallos",
                                         "Calculo POST Tiempo",
                                         "Lista de palabras 2 POST Aciertos", 
                                         "Lista de palabras 2 POST Fallos",
                                         "Lista de palabras 2 POST Tiempo",
                                        ])
output1.to_csv('output.csv', encoding = encoding, sep=";")
for i, row in output1.iterrows():
    
    new_row = {"nombre": row["Id"]}
    
    currentPrueba25 = prueba25[prueba25['nombre'] == row["Id"]]
    currentPrueba26 = prueba26[prueba26['nombre'] == row["Id"]]
    currentPrueba27 = prueba27[prueba27['nombre'] == row["Id"]]
    currentPrueba28 = prueba28[prueba28['nombre'] == row["Id"]]
    currentPrueba29 = prueba29[prueba29['nombre'] == row["Id"]]
    currentPrueba30 = prueba30[prueba30['nombre'] == row["Id"]]
    currentPrueba25_post = prueba25_post[prueba25_post['nombre'] == row["Id"]]
    
    if len(currentPrueba25.index) == 0:
        continue

    currentPrueba25 = currentPrueba25.sort_values(by='fecha',ascending=True)
    
    #if len(currentPrueba25_post.index) == 0:
    #   continue
            
    currentPrueba25_post = currentPrueba25_post.sort_values(by='fecha',ascending=True)

    #print(currentPrueba25_post["fecha"][0]- currentPrueba25["fecha"][0])
    #PRE
    dateStartEvaluationPre = 0
    dateEndEvaluationPre = 0
    totalTimePre = 0

    if len(currentPrueba25.index) > 0:
        prueba25Pre = currentPrueba25.iloc[[0]]
    
        dateStartEvaluationPre = currentPrueba25.iloc[0]["fecha"] #pd.to_datetime(prueba25Pre["fecha"],format="%y-%m-%d %H:%M:%S")
        
        new_row["Lista de palabras 1 Pre Aciertos"] = prueba25Pre["aciertos"].head(1).item()
        new_row["Lista de palabras 1 Pre Fallos"] = prueba25Pre["fallos"].head(1).item()
        new_row["Lista de palabras 1 Pre Tiempo"] = prueba25Pre["tiempo"].head(1).item()
    else:
        new_row["Lista de palabras 1 Pre Aciertos"] = "-"
        new_row["Lista de palabras 1 Pre Fallos"] = "-"
        new_row["Lista de palabras 1 Pre Tiempo"] = "-"
            
        
    if len(currentPrueba26.index) > 0:
        prueba26Pre = currentPrueba26.iloc[[0]]

        new_row["Fichas Pre Aciertos"] = prueba26Pre["aciertos"].head(1).item()
        new_row["Fichas Pre Fallos"] = prueba26Pre["fallos"].head(1).item()
        new_row["Fichas Pre Tiempo"] = prueba26Pre["tiempo"].head(1).item()
    else:
        new_row["Fichas Pre Aciertos"] = "-"
        new_row["Fichas Pre Fallos"] = "-"
        new_row["Fichas Pre Tiempo"] = "-"
        
    if len(currentPrueba27.index) > 0:
        prueba27Pre = currentPrueba27.iloc[[0]]
    
        new_row["Logogramas Pre Aciertos"] = prueba27Pre["aciertos"].head(1).item()
        new_row["Logogramas Pre Fallos"] = prueba27Pre["fallos"].head(1).item()
        new_row["Logogramas Pre Tiempo"] = prueba27Pre["tiempo"].head(1).item()   
    else:
        new_row["Logogramas Pre Aciertos"] = "-"
        new_row["Logogramas Pre Fallos"] = "-"
        new_row["Logogramas Pre Tiempo"] = "-"
    
    if len(currentPrueba28.index) > 0:
        prueba28Pre = currentPrueba28.iloc[[0]]
    
        new_row["Secuencias Pre Aciertos"] = prueba28Pre["aciertos"].head(1).item()
        new_row["Secuencias Pre Fallos"] = prueba28Pre["fallos"].head(1).item()
        new_row["Secuencias Pre Tiempo"] = prueba28Pre["tiempo"].head(1).item()  
    else:
        new_row["Secuencias Pre Aciertos"] = "-"
        new_row["Secuencias Pre Fallos"] = "-"
        new_row["Secuencias Pre Tiempo"] = "-"
    
    if len(currentPrueba29.index) > 0:
        prueba29Pre = currentPrueba29.iloc[[0]]
    
        new_row["Calculo Pre Aciertos"] = prueba29Pre["aciertos"].head(1).item()
        new_row["Calculo Pre Fallos"] = prueba29Pre["fallos"].head(1).item()
        new_row["Calculo Pre Tiempo"] = prueba29Pre["tiempo"].head(1).item()    
    else:
        new_row["Calculo Pre Aciertos"] = "-"
        new_row["Calculo Pre Fallos"] = "-"
        new_row["Calculo Pre Tiempo"] = "-"
    
    if len(currentPrueba30.index) > 0:
        prueba30Pre = currentPrueba30.iloc[[0]]
    
        new_row["Escenas Pre Aciertos"] = prueba30Pre["aciertos"].head(1).item()
        new_row["Escenas Pre Fallos"] = prueba30Pre["fallos"].head(1).item()
        new_row["Escenas Pre Tiempo"] = prueba30Pre["tiempo"].head(1).item()    
    else:
        new_row["Escenas Pre Aciertos"] = "-"
        new_row["Escenas Pre Fallos"] = "-"
        new_row["Escenas Pre Tiempo"] = "-"
        
    if len(currentPrueba25_post.index) > 0:
        prueba25Pre_post = currentPrueba25_post.iloc[[0]]
        dateEndEvaluationPre =currentPrueba25_post.iloc[0]["fecha"] #pd.to_datetime(prueba25Pre_post["fecha"],format="%y-%m-%d %H:%M:%S")
        new_row["Lista de palabras 2 Pre Aciertos"] = prueba25Pre_post["aciertos"].head(1).item()
        new_row["Lista de palabras 2 Pre Fallos"] = prueba25Pre_post["fallos"].head(1).item()
        new_row["Lista de palabras 2 Pre Tiempo"] = prueba25Pre_post["tiempo"].head(1).item()
        
        totalTimePre = dateEndEvaluationPre - dateStartEvaluationPre
    else:
        new_row["Lista de palabras 2 Pre Aciertos"] = "-"
        new_row["Lista de palabras 2 Pre Fallos"] = "-"
        new_row["Lista de palabras 2 Pre Tiempo"] = "-"
     
    new_row["PREVALORACION alfa o beta"] = "alfa" if prueba25Pre["dificultad"].loc[currentPrueba25.index[0]] == "Nivel 1" else "beta"
    new_row["PREVALORACION tiempo total"] = totalTimePre
    
    #POST
    dateStartEvaluationPost = 0
    dateEndEvaluationPost = 0
    totalTimePost = 0

    if len(currentPrueba25.index) > 1:
        prueba25Pre = currentPrueba25.iloc[[1]]
        
        dateStartEvaluationPost = currentPrueba25.iloc[1]["fecha"]
        
        new_row["Lista de palabras 1 POST Aciertos"] = prueba25Pre["aciertos"].head(1).item()
        new_row["Lista de palabras 1 POST Fallos"] = prueba25Pre["fallos"].head(1).item()
        new_row["Lista de palabras 1 POST Tiempo"] = prueba25Pre["tiempo"].head(1).item()
        
        new_row["POSTVALORACION alfa o beta"] = "alfa" if prueba25Pre["dificultad"].loc[currentPrueba25.index[1]] == "Nivel 1" else "beta"
    
    if len(currentPrueba26.index) > 1:
        prueba26Pre = currentPrueba26.iloc[[1]]

        new_row["Fichas POST Aciertos"] = prueba26Pre["aciertos"].head(1).item()
        new_row["Fichas POST Fallos"] = prueba26Pre["fallos"].head(1).item()
        new_row["Fichas POST Tiempo"] = prueba26Pre["tiempo"].head(1).item()    
    
    if len(currentPrueba27.index) > 1:
        prueba27Pre = currentPrueba27.iloc[[1]]
    
        new_row["Logogramas POST Aciertos"] = prueba27Pre["aciertos"].head(1).item()
        new_row["Logogramas POST Fallos"] = prueba27Pre["fallos"].head(1).item()
        new_row["Logogramas POST Tiempo"] = prueba27Pre["tiempo"].head(1).item()       
    
    if len(currentPrueba28.index) > 1:
        prueba28Pre = currentPrueba28.iloc[[1]]
    
        new_row["Secuencias POST Aciertos"] = prueba28Pre["aciertos"].head(1).item()
        new_row["Secuencias POST Fallos"] = prueba28Pre["fallos"].head(1).item()
        new_row["Secuencias POST Tiempo"] = prueba28Pre["tiempo"].head(1).item()   
    
    if len(currentPrueba29.index) > 1:
        prueba29Pre = currentPrueba29.iloc[[1]]
    
        new_row["Calculo POST Aciertos"] = prueba29Pre["aciertos"].head(1).item()
        new_row["Calculo POST Fallos"] = prueba29Pre["fallos"].head(1).item()
        new_row["Calculo POST Tiempo"] = prueba29Pre["tiempo"].head(1).item()     
    
    if len(currentPrueba30.index) > 1:
        prueba30Pre = currentPrueba30.iloc[[1]]
    
        new_row["Escenas POST Aciertos"] = prueba30Pre["aciertos"].head(1).item()
        new_row["Escenas POST Fallos"] = prueba30Pre["fallos"].head(1).item()
        new_row["Escenas POST Tiempo"] = prueba30Pre["tiempo"].head(1).item()      
        
        
    if len(currentPrueba25_post.index) > 1:
        prueba25Pre_post = currentPrueba25_post.iloc[[1]]
        dateEndEvaluationPost = currentPrueba25_post.iloc[1]["fecha"]
        
        new_row["Lista de palabras 2 POST Aciertos"] = prueba25Pre_post["aciertos"].head(1).item()
        new_row["Lista de palabras 2 POST Fallos"] = prueba25Pre_post["fallos"].head(1).item()
        new_row["Lista de palabras 2 POST Tiempo"] = prueba25Pre_post["tiempo"].head(1).item()
        #new_row["POSTVALORACION tiempo total"] = prueba25Pre["dificultad"].loc[currentPrueba25.index[1]]
        
        totalTimePost = dateEndEvaluationPost - dateStartEvaluationPost
        
        new_row["POSTVALORACION alfa o beta"] = "alfa" if prueba25Pre["dificultad"].loc[currentPrueba25.index[1]] == "Nivel 1" else "beta"
        new_row["POSTVALORACION tiempo total"] = totalTimePost
    
    activityValues = activityValues.append(new_row,ignore_index=True)

    # print(new_row)
    
output1 = pd.merge(output1, activityValues, left_on="Id", right_on="nombre", how="left")
output1 = pd.merge(output1, c3, on="redcap_survey_identifier", how="left")
output1 = pd.merge(output1, c4, on="redcap_survey_identifier", how="left")
  
output1.to_csv('output.csv', encoding = encoding, sep=";", float_format='%.0f')