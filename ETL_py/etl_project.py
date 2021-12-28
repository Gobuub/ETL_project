'''
    Comunio Stats ETL Project
    
    Author: Enrique Revuelta
    Date: 30th November 2021

'''


from src.comunio_stats import comunio_stats
from src.comunio_stats_fbref import comunio_stats_fbref
from src.sources import teams_set
from src.sources_fbref import teams_set_fbref
    
if __name__ == "__main__":
    print('Antes de empezar debes introducir la jornada actual.')
    journey = int(input('Introduce la jornada de esta semana: '))
    print('También deberás elegir una de las siguientes fuentes de datos')
    print('Pulsa 1 para elegir ESPN como tu fuente de datos')
    print('Pulsa 2 para elegir FBREF como tu fuente de datos')
    source = int(input('Elige fuente de datos: '))
    
    while source != 1 or source !=2:
    
        if source == 1:
            comunio_stats(teams_set, journey)
            break
        elif source == 2:
            comunio_stats_fbref(teams_set_fbref, journey)
            break
        else:
            print('La opción elegida no es válida, introduce una opción correcta.')
            source = int(input('Elige fuente de datos: '))