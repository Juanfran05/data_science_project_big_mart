import pandas as pd

import plotly.graph_objects as go

import datetime as dt

from sklearn.metrics import mean_squared_error
import math
from sklearn.metrics import r2_score


def modelos(prueba_X, prueba_Y, entrenamiento_X, entrenamiento_Y,
            algoritmo, tipo):

    algoritmo.fit(entrenamiento_X, entrenamiento_Y)
    prediccion = algoritmo.predict(prueba_X)
    mean_squared_error_model = mean_squared_error(prueba_Y, prediccion)
    sqrt_mean_squared_error_model = math.sqrt(mean_squared_error_model)
    r2_model = r2_score(prueba_Y, prediccion)
    
    values = {"mean_squared_error_model": mean_squared_error_model,
              "sqrt_mean_squared_error_model": sqrt_mean_squared_error_model,
              "r2_model": r2_model}
    
    tabla = pd.DataFrame(prueba_X.copy())
    tabla["real"] = prueba_Y.copy()
    tabla["predicho"] = prediccion.copy()
    
    data = tabla[["real","predicho"]].reset_index(drop=True)  

    # plotly line plot real vs predictions
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=data.index, y=data["real"],
                mode="lines", name="real"))
    fig1.add_trace(go.Scatter(x=data.index, y=data["predicho"],
                mode="lines", name="predicho"))
    fig1.update_layout(title='Real vs Predicho',
                                xaxis_title="Real",
                                yaxis_title="Predicho")

    if tipo == "lineal":
        coef = pd.DataFrame(algoritmo.coef_)
    if tipo == "compleja":    
        coef = pd.DataFrame(algoritmo.feature_importances_)
    coef.rename(columns={0: 'coeficientes'}, inplace=True)
    coef["parametros"] = entrenamiento_X.columns
    #plot feature importance plotly
    fig2 = go.Figure(data=[go.Bar(x=coef["parametros"],
                                y=coef["coeficientes"],
                                marker_color='rgb(0,0,0)',
                                marker_line_color='rgb(0,0,0)',
                                marker_line_width=1.5,
                                opacity=0.6)])
    fig2.update_layout(title='Importancia de los parámetros')
    
    return coef, fig1, fig2, values