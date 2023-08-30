from API import DataCollector
from UI import UserInterface

UserInterface.inicio()
departamento, municipio, cultivo, limite_de_registros = UserInterface.ingreso_de_datos()
almacenar_datos = DataCollector.consultar_casos(limite_de_registros, departamento, municipio, cultivo)
almacenar_datos_filtrados = DataCollector.filtrar(almacenar_datos)
UserInterface.tabla_de_datos(almacenar_datos_filtrados)

'''
UserInterface.tabla_medias(almacenar_medias)
almacenar_medias = DataCollector.medias(almacenar_datos_filtrados)
'''