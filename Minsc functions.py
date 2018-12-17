# -*- coding: utf-8 -*-# git change 2
"""
Created on Wed Dec 12 10:09:15 2018

@author: dougl
"""


# Define connection to DB function:

def ConnectarDb( PRODUCCION ):
        
    if PRODUCCION == False:
            conn = pyodbc.connect(
                    '''DRIVER={ODBC Driver 13 for SQL Server};
                    SERVER=localhost\sqlexpress;
                    DATABASE=QueryGoPruebas;
                    Trusted_Connection=yes;
                    autocommit = True;'''
                    )
    else:
            conn = str('No hay DB de Produccion actualmente')
    return( conn )
        


# Define ETL function:

def ETLrespuestas ( IdCliente, IdSegmento, IdDimension, IdIndicador, IdPregunta, conn):
    # Call  Js SP
    Query = '''exec dbo.spRespuestas @IdCliente = {},
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
    
                                             
    cursor = conn.cursor()
    cursor.execute(Query)
    Datos = cursor.fetchall()
    return(Datos)
    
    
    

def ETLrespuestasConAnimo ( IdCliente, 
                           IdDimension,
                           IdIndicador,
                           IdPregunta, 
                           FechaDesde,
                           FechaHasta,
                           conn): # Esta funcion no puede sacar datos segmentados ( por ahora no se necesitan )
    
    # Call  Js SP
    Query = '''exec dbo.spRespuestasConAnimo @IdCliente = {},
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
    
                                             
    cursor = conn.cursor()
    cursor.execute(Query)
    Datos = cursor.fetchall()
    return(Datos)

    
    
    
    
    # Call  Js SP
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
    
    
    

### Preguntas function : Linear Regression with categorical altered scales 1:10

def RegresionLinearPrAnimo :
    
    # Get Data