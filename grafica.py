# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:06:36 2019

@author: jairo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("suicidios2015.csv")
plt.figure(figsize=(15,7))
plt.plot(df["Grupo de edad"],df["Hombre"],df["Mujer"])

plt.annotate('Hombre', xy=(15, 52), xytext=(16, 52.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.annotate('Mujer', xy=(15, 3.14), xytext=(16,3.64),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.xlabel("Edad")
plt.ylabel("Número de suicidios")
plt.show()

plt.figure(figsize=(15,7))
plt.bar(df["Grupo de edad"],df["Total"])
plt.xlabel("Edad")
plt.ylabel("Número total de suicidios de hombres y mujeres")
plt.show()




plt.pie(df["%Total"],None,df["Grupo de edad"])
plt.legend(df["%Total"],title="Porcentajes",loc="right",bbox_to_anchor=(2, 0.5))
plt.show()
plt.figure(figsize=(15,7))
plt.bar(df["Grupo de edad"],df["Hombre"],0.4,color="grey",xerr=0.01)
plt.bar(df["Grupo de edad"],df["Mujer"],0.4,color="red",xerr=0.01)
plt.table(cellText=[df["Hombre"],df["Mujer"]],rowLabels=["Hombre","Mujer"], rowColours=["grey","red"],colLabels=df["Grupo de edad"])

plt.xticks([])
plt.yticks([50,100,150,200])
plt.show()



plt.hist(x=df["Total"],bins=7, weights=df["Hombre"])
plt.xlabel("Totales de suicidios")
plt.ylabel("Número de hombres correspondientes")
plt.show()


colors=np.random.rand(16)
plt.figure(figsize=(15,10))
plt.scatter(df["Hombre"],df["Mujer"],s=df["Total"]*10,c=colors)
plt.xlabel("Suicidios de hombres")
plt.ylabel("Suicidios de mujeres")
plt.show()
