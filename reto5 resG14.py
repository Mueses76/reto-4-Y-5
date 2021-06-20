import pandas as pd

import numpy as np

def resumen_cotizaciones(fichero: str) -> pd.DataFrame:
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])

def HacerMatrizN(fichero: str) -> np.load:
    
    data = np.loadtxt(fichero, delimiter=";",skiprows=2, dtype="str")
    return data

def ObtenerInfo(fichero: str,Buscar: str ) -> pd.DataFrame:
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.')
    return(df[df['Nombre'] == Buscar])

