from modelos import models
import pandas as pd

data = models.create_df(31)

pred_rf = pd.DataFrame(models.predict_rf(data))

if __name__ == "__main__":
    
    print('Hola')
