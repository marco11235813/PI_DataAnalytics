![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup-333333?style=flat&logo=beautifulsoup)
![PowerBI](https://img.shields.io/badge/-PowerBI-333333?style=flat&logo=powerbi)
![PowerQuery](https://img.shields.io/badge/-PowerQuery-333333?style=flat&logo=powerquery)

# Homicidios por siniestros viales en la Ciudad Autónoma de Buenos Aires, Argentina

## Introducción

En este proyecto se simula el rol de un Data Analyst que forma parte del equipo de analistas de datos de una empresa consultora a la cual el **Observatorio de Movilidad y Seguridad Vial (OMSV)**, que es un centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA), les solicitó la elaboración de un proyecto de análisis de datos. 

El fin de este proyecto es generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales ocurridos en CABA. Para ello, se pone a disposición un dataset sobre homicidios en siniestros viales acaecidos en la Ciudad de Buenos Aires durante el periodo 2016-2021.

Se espera como productos finales un reporte de las tareas realizadas, metodologías adoptadas y principales conclusiones y la presentación de un dashboard interactivo que facilite la interpretación de la información y su análisis.

## Contexto

Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y que pueden tener diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden tener consecuencias que van desde daños materiales hasta lesiones graves o fatales para los involucrados.

La Ciudad Autónoma de Buenos Aires, que se ubica en la provincia de Buenos Aires en Argentina, no es la excepción a esta problemática, sino que los siniestros viales son una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden tener un impacto significativo en la seguridad de los residentes y visitantes de la ciudad, así como en la infraestructura vial y los servicios de emergencia.

Actualmente, según el censo poblacional realizado en el año 2022, la población de CABA es de 3,120,612 de habitantes en una superficie de 200 $km^2$, lo que implica una densidad de aproximadamente 15,603 $hab/km^2$ ([Fuente](https://www.argentina.gob.ar/caba#:~:text=Poblaci%C3%B3n%3A%203.120.612%20habitantes%20(Censo%202022).)). Sumado a esto, en Julio de 2023 se registraron 12,437,735 de vehículos transitando por los peajes de las autopistas de acceso a CABA ([Fuente](https://www.estadisticaciudad.gob.ar/eyc/?p=41995)). Por lo que la prevención de siniestros viales y la implementación de políticas efectivas son esenciales para abordar este problema de manera adecuada.

## Datos

Para este proyecto se trabajó con la **Bases de Víctimas Fatales en Siniestros Viales** que se encuentra en formato de Excel y contiene dos pestañas de datos:

* **HECHOS**: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.
* **VICTIMAS**: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho.

Ponemos a disposicion un Diccionario de los datos [aqui](https://github.com/marco11235813/PI_DataAnalytics/blob/main/Diccionario_Datos.xlsx).


## Tecnologías utilizadas

Para la elaboración de este proyecto se utilizó Python y Pandas para los procesos de extracción, transformación y carga de los datos, como así también para el análisis exploratorio de los datos.

Luego, para la obtención complementaria de datos para el cálculo de la población en el año 2021 se realizó webscraping utilizando la librería BeautifulSoup (se puede ver el proceso de webscraping [aqui](https://github.com/marco11235813/PI_DataAnalytics/blob/main/Jupiter_Notebooks/ETL_poblacion.ipynb)).

En la construccion del dashboard, utilizamos Power BI en conjunto con Power Query. Se puede descargar el dashboard [aqui](https://github.com/marco11235813/PI_DataAnalytics/blob/main/Analisis%20Siniestros%20viales.pbix)


## ETL y EDA

En primer lugar, se realizó un proceso de extracción, transformación y carga de los datos (ETL), tanto de "HECHOS" como "VÍCTIMAS", donde se estandarizaron nombres de las variables, se analizaron nulos y duplicados de los registros, se eliminaron columnas redundantes o con muchos valores faltantes, entre otras tareas. Una vez finalizado este proceso para los dos conjuntos de datos de "Homicidios" se procedió a unir los dos conjuntos en uno solo denominado [df_unidos](https://github.com/marco11235813/PI_DataAnalytics/tree/main/data).

Se puede ver el proceso de ETL de los datos [aqui](https://github.com/marco11235813/PI_DataAnalytics/blob/main/Jupiter_Notebooks/ETL_homicidios.ipynb).

En segundo lugar, se procedió a realizar un análisis exploratorio exhaustivo (EDA), con la finalidad de encontrar patrones que permitan generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. Podemos verlo [aqui](https://github.com/marco11235813/PI_DataAnalytics/blob/main/Jupiter_Notebooks/EDA.ipynb).

Como dato extra, iniciamos un script llamado [resources.py](https://github.com/marco11235813/PI_DataAnalytics/blob/main/Jupiter_Notebooks/resources.py) en donde construimos diversas funciones como herramientas para el analisis y ploteo con su respectiva documentación. 

## Análisis de los Datos

Iniciamos el analisis de los datos con la variable temporal, para entender la distribución de los accidentes en distintas escalas temporales. La distribución anual de la cantidad de víctimas fatales es de alrededor del 60% para los primeros 3 años del conjunto de datos, con una disminucion en el año 2019, mucho mas para el 2020 como consecuencia de la cuarentena por COVID 19, y un ligero repunte en el año 2021 (aunque si tomamos como referencia la continuacion del año 2019, seguiriamos con la tendencia descendente). En lo referido al comportamiento a lo largo del año, es decir, la variación mensual, podemos ver ciertos puntos en donde se marca una tendencia recurrente:

* Desde el mes de diciembre a enero se observa una pendiente descendente en la cantidad de accidentes en la gran mayoria de los años
* Ocurre algo similar en el lapso enero-febrero
* Observamos que la gran mayoria de los años, entre el mes de julio-agosto existe un repunte de accidentes
* Tambien en TODOS LOS AÑOS, se presenta un repunte de casos en el mes de noviembre con respecto al mes de octubre

Luego, bajando en la escala temporal, se ve que el 70% de las victimas perdieron la vida en entre lunes y viernes, lo que haría pensar que se debe al traslado diario al trabajo, pero en la distribución semanal no se observan diferencias significativas entre los distintos días. Es decir, la cantidad de víctimas un sábado o un domingo, para todo el conjunto de datos, es aproximadamente el mismo.

Vemos de manera marcada una gran diferencia en la cantidad de accidentes segun el momento del dia, en la franja horaria de la mañana (de 6 am a 11:59 am) con mas del 26% del total de accidentes. Esto marca ciertos patrones en cuanto a las actividades diarias que inciden en la generacion de accidentes (por ejemplo podemos pensar en las reactivaciones en los distintos estratos sociales y etareos de actividades que se producen en ella (horario comercial, laboral, de instituciones educativas, industrial, etc))

Lo siguiente que se hizo fue analizar el perfil de la víctima. En primero lugar se ve que el 77% de las víctimas son masculinas. Casi el 50% de las víctimas se encuentran en un rango etario entre los 25 a 55 años de edad, de los cuales el 84% de ellos son masculinos. 

Si se observa que rol de la víctima, es decir la posición relativa que ocupaba al momento del hecho,  casi el 47% era conductor. En particular, este 47% se distribuye en un 79% de víctimas que se movilizaban en moto y 19% en auto. En relación a la cantidad de víctimas según el medio de transporte al momento del hecho, el 42% de las víctimas son conductores de moto, de los cuales el 88% de los conductores de moto son masculino.

Asimismo, si se analiza la responsabilidad en el hecho, es decir, el vehículo que ocupaba quien resultó acusado, en el 29% de los casos fue el auto, pero en el 75% son responsabilidad de vehículos como auto, colectivos y camiones.

Por último, se buscaron patrones en la distribución espacial de los hechos. Lo que se destaca de este análisis, es que en todas las comunas de CABA se presenta como factor común los accidentes en las avenidas, que son vías arteriales de calzada ancha, de por lo menos 13 metros. El 62% de las víctimas perdió la vida en avenidas. En particular, en el 82% ocurrió en el cruce de las avenidas con otra calle. Este es un comportamiento que se mantiene entre los distintos años. En cuanto al rol de la víctima al momento del hecho, en las distintas comunas varía entre moto y peatón.

## KPI

En función de lo analizado en el punto anterior, se plantearon tres objetivos en relación a la disminución de la cantidad de víctimas fatales de los siniestros viales, desde los cuales se proponen tres indicadores de rendimiento clave o KPI.

* *Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior*

    Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Se define como **Tasa de homicidios en siniestros viales** al número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico, en este caso se toman 6 meses. Su fórmula es:

    $\text{Tasa de homicidios en siniestros viales} = \frac{\text{Número de homicidios en siniestros viales}}{\text{Población total}}·100,000$

    Como *Población Total* se calculó la población para el año 2021 a partir de los censos poblacionales del año 2010 y 2022.

    En este caso, para el año 2021, la *Tasa de homicidios en siniestros viales* fue de 1.77 lo que significa que, durante los primeros 6 meses del año 2021, hubo aproximadamente 1.77 homicidios en accidentes de tránsito por cada 100,000 habitantes. Ahora, el objetivo planteado es reducir esta tasa para el siguiente semestre de 2021 en un 10%, esto es **1.59**. Cuando se calcula el KPI para este período se obtiene que la *Tasa de homicidios en siniestros viales* fue de **1.35**, lo que significa que para el segundo semestre de 2021 se cumple con el objetivo propuesto.

* *Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior*

    Como se vio en el análisis exploratorio, el 42% de las víctimas mortales se transportaban en moto al momento del hecho. Por lo que se consideró importante proponer el monitoreo de la cantidad de accidentes mortales en este tipo de conductor. Para ello se define a la **Cantidad de accidentes mortales de motociclistas** como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. La fórmula para medir la evolución de los accidentes mortales con víctimas en moto es:

    $\text{Cantidad de accidentes mortales de motociclistas} = -\frac{\text{Víctimas moto año anterior - Víctimas moto año actual}}{\text{Víctimas moto año anterior}}·100$

    Donde:
    - $\text{Víctimas moto año anterior}$: Número de accidentes mortales con víctimas en moto en el año anterior
    - $\text{Víctimas moto año actual}$: Número de accidentes mortales con víctimas en moto en el año actual 

    Para este caso, se toma como año actual al año 2021 y como año anterior al año 2020. En primer lugar, se calculó la *Cantidad de accidentes mortales de motociclistas* para el año 2020, el cual resultó de 44.00, de esta manera el objetivo a cumplir es de **42.78** (es decir, la reducción del 7% de la cantidad de accidentes para 2020). El calcular la *Cantidad de accidentes mortales de motociclistas* para el año 2021 resultó de **46.00** lo que significa que aumentó un 64% la cantidad de muertes de conductores de motociclistas respecto del 2021.

* *Reducir en un 8% la cantidad de accidentes mortales de autos en el último año, en CABA, respecto al año anterior.*

    Se consideró importante proponer el monitoreo de la cantidad de accidentes mortales en este tipo de conductor. Para ello se define a la **Cantidad de accidentes mortales de automovilistas** como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en auto en un determinado periodo temporal. La fórmula para medir la evolución de los accidentes mortales con víctimas en auto es: 

    $\text{Cantidad de accidentes mortales de automovilistas} = -\frac{\text{Víctimas auto año anterior - Víctimas auto año actual}}{\text{Víctimas auto año anterior}}·100$

    Donde:
    - $\text{Víctimas auto año anterior}$: Número de accidentes mortales con víctimas en auto en el año anterior
    - $\text{Víctimas auto año actual}$: Número de accidentes mortales con víctimas en auto en el año actual

    Para este caso, se toma como año actual al año 2021 y como año anterior al año 2020. En primer lugar, se calculó la *Cantidad de accidentes mortales de automovilistas* para el año 2020, el cual resultó de 0.0 (este numero refiere a que la variacion entre el año 2019 y 2020 en la cantidad de accidendetes mortales con victimas en auto no tuvo variacion), de esta manera el objetivo a cumplir es de **-8.0** (es decir, la reducción del 8% de la cantidad de accidentes para 2020). El calcular la *Cantidad de accidentes mortales de motociclistas* para el año 2021 resultó de **-2.96** lo que significa que disminuyó casi un 3% la cantidad de muertes de conductores de automovilistas respecto del 2021.

## Conclusiones y recomendaciones

Entre los años 2016 a 2021 se registraron 717 víctimas fatales en accidentes de tránsito. Alrededor del 70% de las víctimas se registraron durante la semana. En cuanto a la franja horaria, mas del 26% de los hechos ocurre entre las 6 y las 11:59 de la mañana. Diciembre es el mes que resulta con el máximo de fallecimientos en el período analizado. Podemos señalar como potencial patron el inicio de actividades, tanto productivas como escolares en el caso de la franja horaria de la mañana, y de vacaciones como puntos de variabilidad, con su maximo exponente en las fiestas de fin de año para el caso del mes de Diciembre

Mas del 83% de las victimas en accidentes son masculinos. En relación al tipo de usuario, el 42% fueron motociclistas. El 62% de los homicidios ocurrió en algún punto de las avenidas de CABA.
Las victimas de mayor edad se observan mas concentradas cuando son pasajeros y las victimas mas jovenes se observan mas concentradas cuando se desplazan en moto.

En las combinaciones de participantes en siniestros con mayor cantidad de accidentes, estan involucrados los motociclistas o los peatones (las 5 primeras combinaciones suman más del 55% del total de victimas)

3 de cada 4 siniestros son generados por automovilistas, transporte público o transporte de carga (el 75% del total), mas del 75% se producen en cruces y 3 de cada 5 siniestros ocurren en intersecciones con una avenida. Y este porcentaje aumenta en el caso de la franja horaria de la la noche hasta la mañana (es decir, entre las 19 pm y las 11:59 am)
Resumiendo, las franjas horarias en donde más accidentes ocurren, contienen más proporcion de accidentes en cruces en proporcion del total acaecido.

Finalmente, para el segundo semestre del año 2021, se cumplió con el objetivo de bajar la tasa de homicidios en siniestros viales, pero no se cumplieron los objetivos de reducir la cantidad de accidentes mortales en motociclistas y de bajar el porcentaje de victimas en automoviles.

En función de lo anterior, se hacen las siguientes recomendaciones:

* Continuar monitoreando los objetivos propuestos acompañados de campañas puntuales, en especial a conductores de motos y usuarios de las avenidas.
* Reforzar las campañas de seguridad vial entre los días viernes a lunes, intensificando particularmente en el mes de Diciembre.
* Puntualizar campañas de conducción segura en avenidas .
* Dirigir las campañas de seguridad hacia el sexo masculino, especialmente en cuanto a conducción en moto, para un rango etario entre los 21 a 50 años.
* Vital la incorporacion de controles (como camaras o multas digitales) en cruces de la ciudad (tengan semaforos o no), principalmente en avenidas

Complementariamente, se recomienda tambien:

* Realizar un estudio de las medidas incoporadas a partir del año 2019, que es el primer año donde se presenta el descenso gradual de la cantidad total de accidentes por año
* Analizar exhaustivamente el porque el repunte de siniestros en los meses de agosto y principalmente de noviembre y diciembre.
* Complementar con un estudio que apunte al genero de conductores, ya que se presenta una gran desproporcion en la cantidad de victimas en los diferentes géneros

## Deploy y publicación

Disponibilizamos el informe interactivo (Dashboard) en la plataforma NovyPro.

Se puede consultar el dashboard [aquí](https://www.novypro.com/profile_projects/marco-caro?Popup=memberProject&Data=1715989529496x344761139490530750).

