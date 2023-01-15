from django.shortcuts import render
from .models import Service
import pandas as pd
import math

# Create your views here.
def fun_grupos(df):
    grupos = len(df)/4
    grupo_col = []
    for i in range(math.ceil(grupos)):
        for j in range(4):
            grupo_col.append(i)
    df['grupo'] = grupo_col[:len(df)]
    return df

def services(request):
    services = Service.objects.values('title' , 'content', 'image')
    df_services = pd.DataFrame.from_records(services)
    df_services = fun_grupos(df_services)
    print(df_services.head())
   
  
    return render(request, "Services/services.html", {'services':df_services.to_records()})