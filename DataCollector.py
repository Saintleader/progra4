import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)


def consultar_casos(limit_registros, departamento, municipio, cultivo):
    results = client.get("ch4u-f3i5", limit=limit_registros, departamento=departamento,
                         municipio=municipio, cultivo=cultivo)
    results_df = pd.DataFrame.from_records(results)
    return results_df

def filtrar(consultado):
    datos_filtrados = consultado[['departamento', 'municipio', 'cultivo', 'topografia',
                                  'ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg',
                                  'potasio_k_intercambiable_cmol_kg']]
    return datos_filtrados

'''
def medias(filtrados):
    medias_filtradas = filtrados.mean()
    return medias_filtradas
'''
