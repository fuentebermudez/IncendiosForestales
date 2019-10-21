import pandas as pd

def calcula_clase(sup):
    if sup<=1:
        clase=0
    if sup>1 and sup<=500:
        clase=1
    if sup>500:
        clase=2
    return clase

def add_clase(df_incendios):
    df_incendios['clase']=df_incendios['superficie'].apply(lambda x:calcula_clase(x))
    print(df_incendios)
    return df_incendios