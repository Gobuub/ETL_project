# Proyecto ETL Comunio

### Se pide:

##### Realizar un proyecto ETL con un tema de libre elección en la que se deben obtener datos con al menos 2 tipos técnicas de extracción
##### diferentes y desde al menos tres tipos de fuentes de datos distintas.

### Descripción del proyecto:

Vamos a realizar un proyecto de ETL sobre el fantasy de fútbol Comunio, con el que buscamos obtener los siguientes tipos de datos.

Tabla de Equipos de La Liga. ( Id. , Nombre Equipo) .

Tabla de Jugadores.

(Id Jugador, Id del equipo, Posición, Partidos Jugados 21/22, Goles, Asistencias, Puntos Comunio, Precio de mercado comunio, Puntos totales temporada 20/21 comunio, Pts ultimas 5 jornadas, Pts de media del campeonato, ptos de media de las últimas 5 jornadas).

#### Fuentes:

Tabla Equipos desde API. api.football-data.org

Estadisticas de jugadores (partidos jugados, goles y asistencias) web scraping desde espn o fbref.

Datos de comunio (Nombre, posición, valor, puntos, ... ). web scraping página comuniazo y comuniate.

Se entrega notebook en el que se obtendran diferentes archivos con los que trabajar: 

    - 1 csv con los equipos de la liga. 
    
    - 1 csv por equipo con los datos de los jugadores de la plantilla. 
    
    - 1 csv con los datos de todos los jugadores de la liga. 
    
    - 1 json con los datos de todos los jugadores de la liga.


#### Estructura del repositorio:

Directorio 'data', donde se guardan los resultado de la ejecución del notebook.
Directorio principal:

        - ETL_py directorio que contiene la app para obtener los datos desde la terminal.
        
            Para ejecutar ir a la ruta del archivo y escribir:
            
                    python o python3 etl_project.py
                    
                    El programa pedirá la jornada, debe introducirse la jornada actual de la liga, la app es operativa desde la jornada 15,, jornada actual a                         fecha de 30 de Noviembre de 2021
        
        - data - donde se guardaran los resultados de la ejecución del notebook.
    
    
        - enviroment.yml archivo para instalar el entorno virtual con las librerias necesarias ya instaladas para ejecutar el notebook sin incidencias.
        
            - Para instalar el entorno vitual ejecutar el siguiente comando en la consola: 
                    
                    conda env create -f environment.yml
        
        - Project_ETL notebook para ejecutar y obtener los datos requeridos para el proyecto.
            - Contiene dos funciones puedes que deben usarse en función de la fuente de datos que quieras usar ESPN o FBREF.
   
        - Entregable_ETL notebook de pruebas.
        
        - ETL para Dashboard, jupyter notebook para EDA del top 35 de jugadores de la jornada y crear un Dashboard.
   
        - Readme.md archivo con la descripción del repositorio.

#### Actualización jornada 27. 8 marzo de 2022:

Añadida la carpeta Project ML, en la que encontraremos notebooks con modelos de ML para predecir la puntuación de los jugadores en la próxima jornada.

A partir de esta jornada se separan los data sets de comunio y de fbref, para evitar la pérdida de datos al realizar el merge, esta pérdida de datos impedía realizar un modelo de previsión de ML, incluido en la carpeta de 'Project ML'.

### It is requested:

#### Carry out an ETL project with a subject of free choice in which data must be obtained with at least 2 types of extraction techniques
#### different and from at least three different types of data sources.

### Project description:

We are going to carry out an ETL project on the football fantasy Comunio, with which we seek to obtain the following type of data.

La Liga Team Table. (Id., Team Name).

Players table.

(Player Id, Team Id, Position, Matches Played 21/22, Goals, Assists, Community Points, Community Market Price, Total Season 20/21 Community Points, Pts in the last 5 days, Average Pts of the championship, average pts of the last 5 days).

#### Sources:

Table Equipment from API. api.football-data.org

Player statistics (games played, goals and assists) web scraping from espn or FBREF.

Community data (Name, position, value, points, ...). web scraping page comuniazo and comuniate.

Notebook is delivered in which different files will be obtained with which to work: 

    - 1 csv with league teams. 
    
    - 1 csv per team with the data of the players in the squad.
    
    - 1 csv with the data of all the players in the league.
    
    - 1 json with the data of all the players in the league.
    

#### Repository structure:


Main directory:

     - ETL_py directory contains app to get data from terminal.
        
            To execute go to the file root and type:
            
                    python o python3 etl_project.py
                    
                    The app will ask for the journey, it only works from journey 15th that is the actually journey at 30th November 2021.
                    
     - data  directory where the results of the notebook execution will be saved.
     
     
     - enviroment.yml file to install the virtual environment with the necessary libraries already installed to run the notebook without incident.
        
        -To install enviroment type on terminal:
        
                conda env create -f environment.yml
                
     - Project_ETL notebook to execute and obtain the data required for the project.
        - Include two functions you may choose one of those based on the source of data you want to use ESPN or FBREF.
     
     - Deliverable_ETL test notebook.
     
     - ETL para Dashboard, jupyter notebook for EDA of top 35 players of the journey, to make a dashboard.
     
     - Readme.md file with the description of the repository. 

#### Update journey 27. 8th March 2022:


Add directory with Project ML, inside it you can find, somo notebooks with model of ML to predict the score of the player on next journey.


Since this data, i decide to split the dataset of comunio and fbref, because the dataleaks on merge two datasets, this merge cause some leaks on the data.