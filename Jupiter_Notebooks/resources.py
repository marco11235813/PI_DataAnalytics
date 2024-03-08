import os.path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime



# creamos una funcion que nos permite iterar sobre un archivo .xlsx que tenga mas de un libro/hoja
def readAllSheets(filename: str) -> dict|list:

    """
    Genera una serie de objetos donde se segmentan las hojas que contiene un archivo .xls como dataframes y una lista de 
    etiquetas referidas a estas

    Esta función toma un archivo excel y genera un objeto Excelfile que nos permite:

    * Crear un lista con las etiquetas de cada hoja
    * Crear un diccionario con pares de etiqueta:hoja, donde cada hoja es un objeto dataframe
    Parameters:
        filename (str): La ruta del archivo .xls.

    Returns:
        diccionario de dataframes, lista de nombres
    
    """

    # controlamos que el archivo pasado en 'filename' exista, sino devolvera None
    if not os.path.isfile(filename):
        return None
    
    # instanciamos el objeto
    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names  # obtenemos las etiquetas de cada hoja
    results = {}
    for sheet in sheets: # iteramos sobre las etiquetas
        results[sheet] = xls.parse(sheet) # mediante el metodo parse, iteramos sobre la hoja que tenga el valor de etiqueta 'sheet', a su vez la asignamos como llave:valor en nuestro diccionario 'results'
        
    xls.close()
    
    return results, sheets



# Creamos una funcion que realice un analisis de las caracteristicas basicas de un dataframe, con un formato de informe
def informe_dataframe(data: str|None= None) -> None:

    """
    esta funcion obtiene un dataframe, y realiza un informe analizando y explorando algunas caracteristicas del 
    dataframe centrandose principalmente en caracteristicas a nivel general de nuestro dataframe y realizando un procesamiento de 
    algunos datos obteniendo metricas e informacion

    devuelve un informe que contiene:

    -Dimensiones del DataFrame
    -Numero de datos
    -Filas y Columnas
    -Metricas Generales

    Parameters: data (pandas.DataFrame).

    Returns: None.

    """
    
    df = data

    print('INFORME PRELIMINAR SOBRE CARACTERISTICAS DEL DATASET:\n')
    print(f'--Dimensiones del DataFrame--\nFilas: {df.shape[0]}\nColumnas: {df.shape[1]}\n')
    print(f'--Numero de datos--\n{df[df.isna() == False].count().sum()}\n')
    print(f'--Filas y Columnas--\nFilas: muestra de indices-------> {list(df.index)[0:5]}  -----> Desde {list(df.index)[0]}  Hasta {list(df.index)[-1]}\nColumnas: {list(df.columns)}\n')
    print(f'--Estadisticos preliminares generales--\n{df.describe()}\n')

    return




# Creamos una funcion para realizar un analisis particular a una columna/feature
def informe_columna(df: None= None|str, columna: None= None|str) -> None:

    """
    esta funcion obtiene un dataframe y el nombre de una de sus columnas, y realiza un informe analizando y explorando algunas caracteristicas de
    la feature, centrandose principalmente en caracteristicas a nivel general y realizando un procesamiento de 
    algunos datos obteniendo metricas e informacion

    Dependiendo el tipo de dato contenido en la feature/columna, devolvera informacion ligeramente diferente:

    Para tipo object:

    -Numero de datos nulos
    -Cantidad de valores unicos en la columna
    -Valores unicos en la columna (Primeros 5 valores, en caso de exceder los 5, en caso contrario, devuelve todos los valores unicos)
    -Moda de la columna
    -Distribucion de frecuencias

    Para tipo datetime64[ns]:

    -Numero de datos nulos
    -Cantidad de valores unicos en la columna
    -Valores unicos en la columna (una muestra de 4 valores como ejemplo, y el rango que abarcan (desde que valor hasta que valor))
    -Moda de la columna
    -Distribucion de frecuencias
    -Valor maximo y minimo

    Para tipo numerico (int, float):

    -Numero de datos nulos
    -Valores unicos en la columna (una muestra de 5 valores como ejemplo, y el rango que abarcan (desde que valor hasta que valor))
    -Moda de la columna
    -Estadisticos Principales de la columna
    -Valores extremos
    -Distribucion de frecuencias
    -Valor maximo y minimo


    Parameters: data (pandas.DataFrame), columna (str).

    Returns: None.
    
    """

    data = df[columna]
    
    # print(f'Informe preliminar sobre la columna/feature {columna}:\n')
    print(f'INFORME PRELIMINAR SOBRE LA COLUMNAS/FEATURE {columna}:\n')
    if data.dtype == 'object':
        print(f'--Numero de datos nulos--\n{data.isna().sum()}\n')
        print(f'--Cantidad de valores unicos en la columna--\n{data.describe()[1]}\n')

        if len(data.unique()) > 5:
            print(f'--Valores unicos en la columna (Primeros 5 valores)--\n{data.unique()[0:5]}\n')
        else:
            print(f'--Valores unicos en la columna--\n{data.unique()}\n')
            
        print(f'--Moda de la columna especificada--\nValor modal -----> {data.describe()[2]}\nFrecuencia acumulada ------> {data.describe()[3]}\n')
        print(f'--Distribucion de frecuencias (primeros valores con mayor cantidad de frecuencias)--\n {data.value_counts().nlargest(3)}\n')
    elif data.dtype == 'datetime64[ns]':
        print(f'--Numero de datos nulos--\n{data.isna().sum()}\n')
        print(f'--Cantidad de valores unicos en la columna--\n{data.describe()[1]}\n')
        ## En el print siguinte, realizamos un formateo de los valores de la columna, ya que la salida predeterminada (el output) agrega otros valores que hacen la intrepretacion mas dificil e incomoda
        print(f'--Valores unicos en la columna--\nEj: {data.dt.strftime("%Y-%m-%d").unique()[0:3]}  -----> Desde {list(data.dt.strftime("%Y-%m-%d").unique())[0]}  Hasta {list(data.dt.strftime("%Y-%m-%d").unique())[-1]}\n')
        print(f'--Moda de la columna especificada--\nValor modal -----> {data.describe()[2]}\nFrecuencia acumulada ------> {data.describe()[3]}\n')
        print(f'--Distribucion de frecuencias (primeros valores con mayor cantidad de frecuencias)--\n {data.value_counts().nlargest(3)}\n')
        print(f'--Valor maximo y minimo--\nMaximo: {data.max()}\nMinimo: {data.min()}\n')
    else:
        print(f'--Numero de datos nulos--\n{data.isna().sum()}\n')
        print(f'--Valores unicos en la columna--\nEj: {data.unique()[0:5]}  -----> Desde {list(data.unique())[0]}  Hasta {list(data.unique())[-1]}\n')
        print(f'--Estadisticos Principales de la columna--\nMedia: {round(data.mean(),2)}\nDesviacion Estandar: {round(data.std(),2)}\nPrimer cuartil: {data.quantile(0.25)}\nMediana: {data.median()}\nTercer cuartil: {data.quantile(0.75)}\n')
        print(f'--Valores extremos--\nValor maximo: {data.max()}\nValor minimo: {data.min()}\n')
        print(f'--Distribucion de frecuencias (primeros valores con mayor cantidad de frecuencias)--\n {data.value_counts().nlargest(3)}\n')
        print(f'--Valor maximo y minimo--\nMaximo: {data.max()}\nMinimo: {data.min()}\n')
    return




def distribucion_anual_mensual(df, segmentacion: str):

    '''
    Crea gráficos de línea para la cantidad de víctimas de accidentes mensuales por año o para la cantidad de accidentes mensuales por año.

    Esta función toma un DataFrame que contiene datos de accidentes, extrae los años únicos
    presentes en la columna 'Año', y crea gráficos de línea para la cantidad de víctimas por mes
    para cada año o para la cantidad de accidentes por mes para cada año. 
    Los gráficos se organizan en una cuadrícula de subgráficos de 2x3.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes, con una columna 'Año'.
        segmentacion (str): la referencia que vamos a tomar..... si victimas(fallecidos) o accidentes(siniestros vehiculares)

    Returns:
        None
    '''

    # Se obtiene una lista de años únicos
    años = df['FECHA'].dt.year.unique()

    # Se define el número de filas y columnas para la cuadrícula de subgráficos
    n_filas = 3
    n_columnas = 2

    # Se crea una figura con subgráficos en una cuadrícula de 2x3
    fig, axes = plt.subplots(n_filas, n_columnas, figsize=(14, 8))

    # Se itera a través de los años y crea un gráfico por año
    for i, year in enumerate(años):
        fila = i // n_columnas
        columna = i % n_columnas
        
        if segmentacion.lower() == 'victimas': 
            # Se filtran los datos para el año actual y agrupa por mes
            data_mensual = (df[df['FECHA'].dt.year == year]
                            .groupby(df['FECHA'].dt.month)
                            .agg({'N_VICTIMAS':'sum'}))
        
            # Se configura el subgráfico actual
            ax = axes[fila, columna]
            data_mensual.plot(ax=ax, kind='line')
            ax.set_title('Año ' + str(year)) ; ax.set_xlabel('Mes') ; ax.set_ylabel('Cantidad_victimas')
            ax.legend_ = None

        elif segmentacion.lower() == 'accidentes': 
            # Se filtran los datos para el año actual y agrupa por mes
            data_mensual = (df[df['FECHA'].dt.year == year]
                            .groupby(df['FECHA'].dt.month)
                            .agg({'ID_hecho':'count'}))
        
            # Se configura el subgráfico actual
            ax = axes[fila, columna]
            data_mensual.plot(ax=ax, kind='line')
            ax.set_title('Año ' + str(year)) ; ax.set_xlabel('Mes') ; ax.set_ylabel('Cantidad_accidentes')
            ax.legend_ = None
        
    # Se muestra y acomoda el gráfico
    plt.tight_layout()
    plt.show()



def cantidad_victimas_mensuales(df):

    '''
    Crea un gráfico de barras que muestra la cantidad de víctimas de accidentes por mes.

    Esta función toma un DataFrame que contiene datos de accidentes, agrupa los datos por mes
    y calcula la cantidad total de víctimas por mes. Luego, crea un gráfico de barras que muestra
    la cantidad de víctimas para cada mes.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes con una columna 'Mes'.

    Returns:
        None
    '''

    # Se agrupa por la cantidad de víctimas por mes
    # data = df.groupby('FECHA').agg({'N_VICTIMAS':'sum'}).dt.month.reset_index()
    data = df.groupby(df['FECHA'].dt.month)['N_VICTIMAS'].sum().reset_index()
    
    # Se grafica
    plt.figure(figsize=(15,10))
    ax = sns.barplot(x= 'FECHA', y='N_VICTIMAS', data=data)
    ax.set_title('Cantidad de víctimas por Mes')
    ax.set_xlabel('Mes') ; ax.set_ylabel('Cantidad de Victimas')
    
    # Se imprime resumen
    print(f'El mes con menor cantidad de víctimas tiene {data.min()[1]} víctimas')
    print(f'El mes con mayor cantidad de víctimas tiene {data.max()[1]} víctimas')
    
    # Se muestra el gráfico
    plt.grid()
    plt.show()




def cantidad_victimas_por_dia_semana(df):

    '''
    Crea un gráfico de barras que muestra la cantidad de víctimas de accidentes por día de la semana.

    Esta función toma un DataFrame que contiene datos de accidentes, convierte la columna 'Fecha' a tipo de dato
    datetime si aún no lo es, extrae el día de la semana (0 = lunes, 6 = domingo), mapea el número del día
    de la semana a su nombre, cuenta la cantidad de accidentes por día de la semana y crea un gráfico de barras
    que muestra la cantidad de víctimas para cada día de la semana.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes con una columna 'Fecha'.

    Returns:
        None
    '''

    # # Se convierte la columna 'fecha' a tipo de dato datetime
    # df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Día semana'] = df['FECHA'].dt.dayofweek
    
    # Se mapea el número del día de la semana a su nombre
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    df['Nombre día'] = df['Día semana'].map(lambda x: dias_semana[x])
    
    # Se cuenta la cantidad de accidentes por día de la semana
    data = df.groupby('Nombre día').agg({'N_VICTIMAS':'sum'}).reset_index()
      
    # Se crea el gráfico de barras
    plt.figure(figsize=(15, 10))
    ax = sns.barplot(x='Nombre día', y='N_VICTIMAS', data=data, order=dias_semana)
    
    ax.set_title('Cantidad de Accidentes por Día de la Semana') ; ax.set_xlabel('Día de la Semana') ; ax.set_ylabel('Cantidad de Victimas')
    plt.xticks(rotation=45)
    
    # Se muestran datos resumen
    print(f'El día de la semana con menor cantidad de víctimas tiene {data.min()[1]} víctimas')
    print(f'El día de la semana con mayor cantidad de víctimas tiene {data.max()[1]} víctimas')
    print(f'La diferencia porcentual es de {round((data.max()[1] - data.min()[1]) / data.min()[1] * 100,2)}')
    
    # Se muestra el gráfico
    plt.grid()
    plt.show()




def crea_categoria_momento_dia(hora):
    
  """
  Devuelve la categoría de tiempo correspondiente a la hora proporcionada.

  Parameters:
    hora: La hora a clasificar.

  Returns:
    La categoría de tiempo correspondiente.
  """
  if hora >= 6 and hora <= 10:
    return "Mañana"
  elif hora >= 11 and hora <= 13:
    return "Medio día"
  elif hora >= 14 and hora <= 18:
    return "Tarde"
  elif hora >= 19 and hora <= 23:
    return "Noche"
  else:
    return "Madrugada"




def cantidad_accidentes_por_categoria_tiempo(df):

    '''
    Calcula la cantidad de accidentes por categoría de tiempo y muestra un gráfico de barras.

    Esta función toma un DataFrame que contiene una columna 'Hora' y utiliza la función
    'crea_categoria_momento_dia' para crear la columna 'Categoria tiempo'. Luego, cuenta
    la cantidad de accidentes por cada categoría de tiempo, calcula los porcentajes y
    genera un gráfico de barras que muestra la distribución de accidentes por categoría de tiempo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la información de los accidentes.

    Returns:
        None
    '''

    print('Franja horaria:\nMañana: de 6:00 am a 10:59 am\nMediodia: de 11 am a 13:59 pm\nTarde: de 14 a 18:59 pm\nNoche: de 19 pm a 23:59 pm\nMadrugada: de 0 am a 5:59 am')

    # Se aplica la función crea_categoria_momento_dia para crear la columna 'categoria_tiempo'
    df['Categoria tiempo'] = df['HORA_HECHO'].apply(crea_categoria_momento_dia)

    # Se cuenta la cantidad de accidentes por categoría de tiempo
    data = df['Categoria tiempo'].value_counts().reset_index()
    data.columns = ['Categoria tiempo', 'Cantidad accidentes']

    # Se calculan los porcentajes
    total_accidentes = data['Cantidad accidentes'].sum()
    data['Porcentaje'] = (data['Cantidad accidentes'] / total_accidentes) * 100
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(15, 10))
    ax = sns.barplot(x='Categoria tiempo', y='Cantidad accidentes', data=data)

    ax.set_title('Cantidad de Accidentes por Categoría de Tiempo') ; ax.set_xlabel('Categoría de Tiempo') ; ax.set_ylabel('Cantidad de Accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad accidentes"]}', (index, row["Cantidad accidentes"]), ha='center', va='bottom')

    # Se muestra el gráfico
    plt.show()


def distribucion_edad(df):

    '''
    Genera un gráfico con un histograma y un boxplot que muestran la distribución de la edad de los involucrados en los accidentes.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico con un histograma y un boxplot.
    '''

    # Se crea una figura con un solo eje x compartido
    fig, ax = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
    
    # Se grafica el histograma de la edad
    sns.histplot(df['EDAD'], kde=True, ax=ax[0])
    ax[0].set_title('Histograma de Edad') ; ax[0].set_ylabel('Frecuencia')
    
    # Se grafica el boxplot de la edad
    sns.boxplot(x=df['EDAD'], ax=ax[1])
    ax[1].set_title('Boxplot de Edad') ; ax[1].set_xlabel('Edad')
    
    # Se ajusta y muestra el gráfico
    plt.tight_layout()
    plt.show()




    
def distribucion_edad_por_anio(df):

    '''
    Genera un gráfico de boxplot que muestra la distribución de la edad de las víctimas de accidentes por año.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de boxplot.
    '''

    # Se crea el gráfico de boxplot
    plt.figure(figsize=(15, 10))
    sns.boxplot(x= df['FECHA'].dt.year, y='EDAD', data=df)
    
    plt.title('Boxplot de Edades de Víctimas por Año') ; plt.xlabel('Año') ; plt.ylabel('Edad de las Víctimas')
     
    # Se muestra el gráfico
    plt.show()




def cantidades_accidentes_por_anio_y_sexo(df):

    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por año y sexo.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de barras.
    '''

    data = df.groupby([df['FECHA'].dt.year, 'SEXO'])['ID_hecho'].count().reset_index()


    # Se crea el gráfico de barras
    plt.figure(figsize=(15, 10))
    sns.barplot(x= 'FECHA', y='ID_hecho', hue='SEXO', data=data)
    
    plt.title('Cantidad de Accidentes por Año y Sexo')
    plt.xlabel('Año') ; plt.ylabel('Cantidad de Accidentes') ; plt.legend(title='Sexo')
    
    # Se muestra el gráfico
    plt.show()




def edad_y_rol_victimas(df):

    '''
    Genera un gráfico de la distribución de la edad de las víctimas por rol.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''

    plt.figure(figsize=(15, 10))
    sns.boxplot(y='ROL', x='EDAD',data=df)
    plt.title('Edades por Condición')
    plt.show()
    



def distribucion_edad_por_victima(df):

    '''
    Genera un gráfico de la distribución de la edad de las víctimas por tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''

    # Se crea el gráfico de boxplot
    plt.figure(figsize=(15, 10))
    sns.boxplot(x='VICTIMA', y='EDAD', data=df)
    
    plt.title('Boxplot de Edades de Víctimas por tipo de vehículo que usaba') ; plt.xlabel('Tipo de vehiculo') ; plt.ylabel('Edad de las Víctimas')
     
    plt.show()
    



def cantidad_accidentes_sexo(df):

    '''
    Genera un resumen de la cantidad de accidentes por sexo de los conductores.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de accidentes por sexo de los conductores en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de accidentes por sexo de los conductores.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''

    # # Se convierte la columna 'fecha' a tipo de dato datetime
    # df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Dia semana'] = df['FECHA'].dt.dayofweek
    
    # Se crea una columna 'tipo_dia' para diferenciar entre semana y fin de semana
    df['Tipo de día'] = df['Dia semana'].apply(lambda x: 'Fin de Semana' if x >= 5 else 'Semana')
    
    # Se cuenta la cantidad de accidentes por tipo de día
    data = df['Tipo de día'].value_counts().reset_index()
    data.columns = ['Tipo de día', 'Cantidad de accidentes']
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Tipo de día', y='Cantidad de accidentes', data=data)
    
    ax.set_title('Cantidad de accidentes por tipo de día') ; ax.set_xlabel('Tipo de día') ; ax.set_ylabel('Cantidad de accidentes')
    
    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (index, row["Cantidad de accidentes"]), ha='center', va='bottom')
    
    # Se muestra el gráfico
    plt.show()




def cantidad_victimas_sexo_rol_victima(df):

    '''
    Genera un resumen de la cantidad de víctimas por sexo, rol y tipo de vehículo en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Gráficos de barras que muestran la cantidad de víctimas por sexo, rol y tipo de vehículo en orden descendente.
    * DataFrames que muestran la cantidad y el porcentaje de víctimas por sexo, rol y tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''

    # Se crea el gráfico
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Gráfico 1: Sexo
    sns.countplot(data=df, x='SEXO', ax=axes[0])
    axes[0].set_title('Cantidad de víctimas por sexo') ; axes[0].set_ylabel('Cantidad de víctimas')

    # Se define una paleta de colores personalizada (invierte los colores)
    colores_por_defecto = sns.color_palette()
    colores_invertidos = [colores_por_defecto[1], colores_por_defecto[0]]
    
    # Gráfico 2: Rol
    df_rol = df.groupby(['ROL', 'SEXO']).size().unstack(fill_value=0)
    df_rol.plot(kind='bar', stacked=True, ax=axes[1], color=colores_invertidos)
    axes[1].set_title('Cantidad de víctimas por rol') ; axes[1].set_ylabel('Cantidad de víctimas') ; axes[1].tick_params(axis='x', rotation=45)
    axes[1].legend().set_visible(False)
    
    # Gráfico 3: Tipo de vehículo
    df_victima = df.groupby(['VICTIMA', 'SEXO']).size().unstack(fill_value=0)
    df_victima.plot(kind='bar', stacked=True, ax=axes[2], color=colores_invertidos)
    axes[2].set_title('Cantidad de víctimas por tipo de vehículo') ; axes[2].set_ylabel('Cantidad de víctimas') ; axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend().set_visible(False)

    # Se muestran los gráficos
    plt.show()
    
    # # Se calcula la cantidad de víctimas por sexo
    # sexo_counts = df['Sexo'].value_counts().reset_index()
    # sexo_counts.columns = ['Sexo', 'Cantidad de víctimas']

    # # Se calcula el porcentaje de víctimas por sexo
    # total_victimas_sexo = sexo_counts['Cantidad de víctimas'].sum()
    # sexo_counts['Porcentaje de víctimas'] = (sexo_counts['Cantidad de víctimas'] / total_victimas_sexo) * 100

    # # Se crea el DataFrame para sexo
    # df_sexo = pd.DataFrame(sexo_counts)
    # print('Resumen para Sexo:')
    # print(df_sexo)
    
    # # Se calcula la cantidad de víctimas por rol y sexo
    # df_rol = df.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)

    # # Se calcula el porcentaje de víctimas por rol y sexo
    # total_victimas_rol = df_rol.sum(axis=1)
    # df_rol_porcentaje = df_rol.divide(total_victimas_rol, axis=0) * 100

    # # Se renombra las columnas para el DataFrame de porcentaje
    # df_rol_porcentaje.columns = [f"Porcentaje de víctimas {col}" for col in df_rol_porcentaje.columns]

    # # Se combinan los DataFrames de cantidad y porcentaje
    # df_rol = pd.concat([df_rol, df_rol_porcentaje], axis=1)
    # print('Resumen para Rol:')
    # print(df_rol)
    
    # # Se calcula la cantidad de víctimas por tipo de vehículo
    # tipo_vehiculo_counts = df['Víctima'].value_counts().reset_index()
    # tipo_vehiculo_counts.columns = ['Tipo de Vehículo', 'Cantidad de víctimas']

    # # Se calcula el porcentaje de víctimas por tipo de vehículo
    # total_victimas = tipo_vehiculo_counts['Cantidad de víctimas'].sum()
    # tipo_vehiculo_counts['Porcentaje de víctimas'] = round((tipo_vehiculo_counts['Cantidad de víctimas'] / total_victimas) * 100,2)

    # # Se crea un DataFrame con la cantidad y porcentaje de víctimas por tipo de vehículo
    # df_tipo_vehiculo = pd.DataFrame(tipo_vehiculo_counts)
    # print('Resumen para Tipo de vehículo:')
    # print(df_tipo_vehiculo)
    
    # # Se calcula la cantidad de víctimas por tipo de vehículo y sexo
    # tipo_vehiculo_sexo_counts = df.groupby(['Víctima', 'Sexo']).size().unstack(fill_value=0).reset_index()    
    # tipo_vehiculo_sexo_counts.columns = ['Tipo de Vehículo', 'Mujeres', 'Hombres']

    # # Se calcula la cantidad total de víctimas
    # total_victimas = tipo_vehiculo_sexo_counts[['Hombres', 'Mujeres']].sum(axis=1)

    # # se agregan las columnas de cantidad total y porcentaje
    # tipo_vehiculo_sexo_counts['Cantidad Total'] = total_victimas
    # tipo_vehiculo_sexo_counts['Porcentaje Hombres'] = (tipo_vehiculo_sexo_counts['Hombres'] / total_victimas) * 100
    # tipo_vehiculo_sexo_counts['Porcentaje Mujeres'] = (tipo_vehiculo_sexo_counts['Mujeres'] / total_victimas) * 100

    # # Se imprimen resumenes
    # print("Resumen de víctimas por tipo de vehículo y sexo:")
    # print(tipo_vehiculo_sexo_counts)





def cantidad_victimas_participantes(df):

    '''
    Genera un resumen de la cantidad de víctimas por número de participantes en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por número de participantes en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por número de participantes.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''

    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['PARTICIPANTES'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'PARTICIPANTES': 'count',
                                    'index': 'PARTICIPANTES'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 7))
    
    # Se crea el gráfico de barras
    ax = sns.barplot(data=ordenado, x='PARTICIPANTES', y='count', order=ordenado['PARTICIPANTES'])
    ax.set_title('Cantidad de víctimas por participantes')
    ax.set_ylabel('Cantidad de víctimas')
    # Rotar las etiquetas del eje x a 45 grados
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()
    
    # # Se calcula la cantidad de víctimas por participantes
    # participantes_counts = df['Participantes'].value_counts().reset_index()
    # participantes_counts.columns = ['Participantes', 'Cantidad de víctimas']

    # # Se calcula el porcentaje de víctimas por participantes
    # total_victimas = participantes_counts['Cantidad de víctimas'].sum()
    # participantes_counts['Porcentaje de víctimas'] = round((participantes_counts['Cantidad de víctimas'] / total_victimas) * 100,2)

    # # Se ordenan los datos por cantidad de víctimas en orden descendente
    # participantes_counts = participantes_counts.sort_values(by='Cantidad de víctimas', ascending=False)
    
    # # Se imprimen resumenes
    # print("Resumen de víctimas por participantes:")
    # print(participantes_counts)
    



def cantidad_acusados(df):

    '''
    Genera un resumen de la cantidad de acusados en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de acusados en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de acusados.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''

    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['ACUSADO'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'ACUSADO': 'count',
                                    'index': 'ACUSADO'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 10))
    
    # Crear el gráfico de barras
    ax = sns.barplot(data=ordenado, x='ACUSADO', y='count', order=ordenado['ACUSADO'])
    ax.set_title('Cantidad de acusados en los hechos') ; ax.set_ylabel('Cantidad de acusados') 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()
    
    # # Se calcula la cantidad de acusados
    # acusados_counts = df['Acusado'].value_counts().reset_index()
    # acusados_counts.columns = ['Acusado', 'Cantidad de acusados']

    # # Se calcula el porcentaje de acusados
    # total_acusados = acusados_counts['Cantidad de acusados'].sum()
    # acusados_counts['Porcentaje de acusados'] = round((acusados_counts['Cantidad de acusados'] / total_acusados) * 100,2)

    # # Se ordenan los datos por cantidad de acusados en orden descendente
    # acusados_counts = acusados_counts.sort_values(by='Cantidad de acusados', ascending=False)
    # # Se imprimen resumen
    # print("Resumen de acusados:")
    # print(acusados_counts)





def accidentes_tipo_de_calle(df):

    '''
    Genera un resumen de los accidentes de tráfico por tipo de calle y cruce.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por tipo de calle.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por tipo de calle.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    
    # Se crea el gráfico
    fig, axes = plt.subplots(figsize=(15, 7))

    sns.countplot(data=df, x='TIPO_DE_CALLE', ax=axes)
    axes.set_title('Cantidad de víctimas por tipo de calle') ; axes.set_ylabel('Cantidad de víctimas')

    # sns.countplot(data=df, x='Cruce', ax=axes[1])
    # axes[1].set_title('Cantidad de víctimas en cruces') ; axes[1].set_ylabel('Cantidad de víctimas')
    
    # Mostramos los gráficos
    plt.show()
    
    # # Se calcula la cantidad de víctimas por tipo de calle
    # tipo_calle_counts = df['Tipo de calle'].value_counts().reset_index()
    # tipo_calle_counts.columns = ['Tipo de calle', 'Cantidad de víctimas']

    # # Se calcula el porcentaje de víctimas por tipo de calle
    # tipo_calle_counts['Porcentaje de víctimas'] = round((tipo_calle_counts['Cantidad de víctimas'] / tipo_calle_counts['Cantidad de víctimas'].sum()) * 100,2)

    # # Se calcula la cantidad de víctimas por cruce
    # cruce_counts = df['Cruce'].value_counts().reset_index()
    # cruce_counts.columns = ['Cruce', 'Cantidad de víctimas']

    # # Se calcula el porcentaje de víctimas por cruce
    # cruce_counts['Porcentaje de víctimas'] = round((cruce_counts['Cantidad de víctimas'] / cruce_counts['Cantidad de víctimas'].sum()) * 100,2)

    # # Se crean DataFrames para tipo de calle y cruce
    # df_tipo_calle = pd.DataFrame(tipo_calle_counts)
    # df_cruce = pd.DataFrame(cruce_counts)

    # #  Se muestran los DataFrames resultantes
    # print("Resumen por Tipo de Calle:")
    # print(df_tipo_calle)
    # print("\nResumen por Cruce:")
    # print(df_cruce)





def main():
    return



if __name__ == '__main__':
    main()