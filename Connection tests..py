# -*- coding: utf-8 -*- First Git change
"""
Created on Tue Dec 11 09:53:50 2018

@author: dougl
"""


import pyodbc
import datetime as dt
import string

# Coneection Test:

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=SERVERNAME;'
    r'DATABASE=DBNAME;'
    r'Trusted_Connection=yes;'
    r'autocommit = True;'
    )


cursor = conn.cursor()

# Definir Variables para llamar al SP

IdCliente = 7
IdSegmento = 'null'
IdDimension = 8
IdIndicador = 'null'
IdPregunta = 'null'
Desde = dt.date(2018,10,17)
Hasta = dt.date(2018,11,25)
NumMesesPreviosPreguntasEstaticas = 6

Query = '''exec dbo.spRespuestasSegmento @IdCliente = {},
                                         @IdSegmento = {},
                                         @IdDimension = {},
                                         @IdIndicador = {},
                                         @IdPregunta = {},
                                         @Desde = "{}",
                                         @Hasta = "{}",
                                         @NumMesesPreviosPreguntasEstaticas = {} 
                                         '''.format(IdCliente,
                                             IdSegmento,
                                             IdDimension, 
                                             IdIndicador, 
                                             IdPregunta,
                                             Desde, 
                                             Hasta, 
                                             NumMesesPreviosPreguntasEstaticas)

# need to print(str ) to see the string without /n and wierd format.

cursor.execute(Query)


Datos = cursor.fetchall()



Query = '''exec dbo.spRespuestas @IdCliente = {},
                                 @IdDimension = {},
                                 @IdIndicador = {},
                                 @IdPregunta = {},
                                 @Desde = "{}",
                                 @Hasta = "{}",
                                 @NumMesesPreviosPreguntasEstaticas = {} 
                                  '''.format(IdCliente,
                                             IdDimension, 
                                             IdIndicador, 
                                             IdPregunta,
                                             Desde, 
                                             Hasta, 
                                             NumMesesPreviosPreguntasEstaticas)

# need to print(str ) to see the string without /n and wierd format.

cursor.execute(Query)








cursor.excute(Query)
