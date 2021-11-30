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

Estadisticas de jugadores (partidos jugados, goles y asistencias) web scraping desde espn.

Datos de comunio (Nombre, posición, valor, puntos, ... ). web scraping página comuniazo y comuniate.

Se entrega notebook en el que se obtendran diferentes archivos con los que trabajar: 
    - 1 csv con los equipos de la liga. 
    - 1 csv por equipo con los datos de los jugadores de la plantilla. 
    - 1 csv con los datos de todos los jugadores de la liga. 
    - 1 json con los datos de todos los jugadores de la liga.

#### Estructura del repositorio:

Directorio 'data', donde se guardan los resultado de la ejecución del notebook.
Directorio principal:

    - data - donde se guardaran los resultados de la ejecución del notebook.
    
    
    - enviroment.yml archivo para instalar el entorno virtual con las librerias necesarias ya instaladas para ejecutar el notebook sin incidencias.
        
        - Para instalar el entorno vitual ejecutar el siguiente comando en la consola: 
                    
                    conda env create -f environment.yml
        
   - Project_ETL notebook para ejecutar y obtener los datos requeridos para el proyecto.
   
   - Entregable_ETL notebook de pruebas.
   
   - Readme.md archivo con la descripción del repositorio.

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

Player statistics (games played, goals and assists) web scraping from espn.

Community data (Name, position, value, points, ...). web scraping page comuniazo and comuniate.

Notebook is delivered in which different files will be obtained with which to work: 
    - 1 csv with league teams. 
    - 1 csv per team with the data of the players in the squad.
    - 1 csv with the data of all the players in the league.
    - 1 json with the data of all the players in the league.

#### Repository structure:


Main directory:

     - data  directory where the results of the notebook execution will be saved.
     
     
     - enviroment.yml file to install the virtual environment with the necessary libraries already installed to run the notebook without incident.
        -To install enviroment type on terminal:
        
                conda env create -f environment.yml
                
     - Project_ETL notebook to execute and obtain the data required for the project.
     
     - Deliverable_ETL test notebook.
     
     - Readme.md file with the description of the repository. 
