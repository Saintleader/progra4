from tabulate import tabulate


def inicio():
    print("\n                      CONSULTA DE       \n"
          " CULTIVOS PRIORITARIOS POR DEPARTAMENTO, MUNICIPIO Y CULTIVO\n"
          "------------------------------------------"
          )


def ingreso_de_datos():
    limite_de_registros = (int(input("Ingresar el Número de Registros que se desea consultar: ")))
    departamento = str(input("Ingresar el departamento: ").upper())
    municipio = str(input("Ingresar el municipio: ").upper())
    cultivo = str(input("Ingresar el cultivo: ").capitalize())
    return [departamento, municipio, cultivo, limite_de_registros]


def tabla_de_datos(filtracion):
    print(tabulate(filtracion,
                   headers=['Número', 'Departamento', 'Municipio', 'Cultivo', 'Topologia', 'Ph', 'Potasio',
                            'Fósforo'], tablefmt='grid'))


def tabla_medianas(medias):
    print(f'las medianas de cada fila son:\n{medias}')
