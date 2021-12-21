'''
    Comunio Stats ETL Project
    
    Author: Enrique Revuelta
    Date: 30th November 2021

'''


from src.comunio_stats import comunio_stats
from src.sources import teams_set
    
if __name__ == "__main__":
    print('Antes de empezar debes introducir la jornada actual.')
    print('A fecha de 30 de Noviembre la jornada actual es la 15')
    journey = int(input('Introduce la jornada de esta semana: '))
    comunio_stats(teams_set, journey)