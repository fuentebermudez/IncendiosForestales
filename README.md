
# IDRAPI

## Introducción

En este proyecto se presenta una aplicación cuyo objetivo es determinar la gravedad de un incendio forestal estimando la superficie que se puede ver afectada en caso de producirse.

Esta aplicación es el resultado del estudio de dos problemas:

 El  primer problema consiste en saber si era posible partir de un conjunto de datos y enriquecerlo desde otras fuentes para conseguir la información necesaria para analizar el segundo problema. 

Este segundo problema consiste en estudiar si es posible entreran un modelo de aprendizaje supervisado que, partiendo de los datos obtenidos, fuera capaz de estimar la superficie total afectada por el un incendio forestal.

Saber de antemano, ya no sólo el riesgo de que se produzca un incendio sino tener una estimación de la gravedad del mismo, permite elaborar planes de contingencia y manejar los recursos disponibles de forma más óptima.

## Funcionalidad
Partiendo de unas coordenadas y el ID de una estación meteorológica la aplicación obtiene una serie de datos meteorológicos, relacionados con la orografía y telemétricos para hacer la estimación de la superficie quemada por un incendio en una determinada localización.

## Uso
El suso de la aplicación es sencillo, basta con clonar el repositorio y ejecutar el archivo IDRAPI_V.py. 

### Requerimientos
Para ejecutar la aplicación se requiere la instalación de los siguientes paquetes:
* Pandas
* Numpy
* [Richdem](https://richdem.readthedocs.io/en/latest/python_api.html)
* Requests


### Ejecutar la aplicación en local.
Ejecutar la aplicación en local requiere:

1. Clonar el repositorio.
 
2. [Instalar Richdem](https://richdem.readthedocs.io/en/latest)
	
3. Ejecutar el archivo IDRAPI_V.py

### Estructura del proyecto

Use the below for Markdown formatting syntax:

#### Data

En la carpeta datos encontramos los datos que se han usado para entrenar el modelo y los generados por los pasos intermedios.

* Meteo-Datos meteorológicos
* Shp-Archivos en formato shp generados para unir geoespacialmente los datos relacionandos con los incendios con los datos de las estaciones meteorológicas.
* DatosRemotos- Contiene los datos obtenidos de repositorios remotos para cada uno de los incendios recogidos en la fuente de datos original.
* Incendios- Contiene los datos originales así como los datos derivados de la uníón con las diferentes fuentes de datos remotos.

#### Source
##### Notebboks
Esta carpeta contien los Notebooks que se han utilizado para obtener los datos remotos y para realizar el mergeo de los datos.
##### Modelado
Contiene el script utilizado para testear diferentes modelos de regresión supervisada elegidos y poder elegir el más adecuado.

## Useful links 
Remove this section if it is not needed.

[Publication](www.github.com)  
[Additional link](www.github.com)  
[Additional link](www.github.com)

## Contributors

Include a section for credits in order to highlight and link to the authors of your project. 
Apart from listing contacts of specific people involved in the project, aslo include the general email to the ONS Big Data project

## License

MIT? OGL?