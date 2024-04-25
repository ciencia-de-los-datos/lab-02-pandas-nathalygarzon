"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    filas = tbl0.shape[0]

    return filas


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    columnas = tbl0.shape[1]

    return columnas


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """

    columna_c1 = tbl0.iloc[:,[1]]

    lista_c1 = list(columna_c1['_c1'])

    new_c1 = []
    for word in lista_c1:
        new_c1.append((word, 1))

    sorted_c1 = sorted(new_c1, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_c1:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
            
    new_sequence1=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence1.append(tupla)

    registros_c1 = pd.DataFrame(new_sequence1)

    return registros_c1


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """

    columna_c1 = tbl0.iloc[:,[1]]

    lista_c1 = list(columna_c1['_c1'])

    new_c1 = []
    for word in lista_c1:
        new_c1.append((word, 1))

    sorted_c1 = sorted(new_c1, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_c1:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
            
    new_sequence1=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence1.append(tupla)

    columnas_c1c2 = tbl0.iloc[:,[1,2]]
    tuplas = [tuple(x) for x in columnas_c1c2.to_records(index=False)]
    sorted_tupla = sorted(tuplas, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
            
        new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    promedio = new_sequence1 + new_sequence

    diccionario={}
    for key, value in promedio:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
            
        promedio1=[]
    for key, value in diccionario.items():
        tupla=(key, value)
        promedio1.append(tupla)

    prom = [(item[0], '{:.6f}'.format(item[1][1] / item[1][0])) for item in promedio1]

    prom = pd.DataFrame(prom)
    
    return prom


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """

    columnas_c1c2 = tbl0.iloc[:,[1,2]]
    tuplas = [tuple(x) for x in columnas_c1c2.to_records(index=False)]
    sorted_tupla = sorted(tuplas, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
            
    max1=[]
    for key, value in diccionario.items():
        tupla=(key, max(value))
        max1.append(tupla)

    max1 = pd.DataFrame(max1)

    return max1


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    columna_c4 = tbl1.iloc[:,[1]]
    lista_c4 = list(columna_c4['_c4'])
    conjunto_c4 = sorted(set(lista_c4))
    mayusculas = [letra.upper() for letra in conjunto_c4]

    return mayusculas



def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """

    columnas_c1c2 = tbl0.iloc[:,[1,2]]
    tuplas = [tuple(x) for x in columnas_c1c2.to_records(index=False)]
    sorted_tupla = sorted(tuplas, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
                
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    suma = pd.DataFrame(new_sequence)

    return suma


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']

    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    columna_c3 = tbl0.iloc[:,[3]]
    lista_c3 = list(columna_c3['_c3'])
    lista_de_listas = [lista.split('-')[0] for lista in lista_c3]
    year = pd.DataFrame(lista_de_listas)

    tbl0['year'] = year
    
    return tbl0

def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    
    columnas_c1c2 = tbl0.iloc[:,[1,2]]
    tuplas = [tuple(x) for x in columnas_c1c2.to_records(index=False)]
    sorted_tupla = sorted(tuplas, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
                
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, value)
        new_sequence.append(tupla)

    sorted_data = [(key, sorted(values)) for key, values in new_sequence]
    formatted_data = [(key, ':'.join(map(str, values))) for key, values in sorted_data]

    valores = pd.DataFrame(formatted_data)
    valores.columns = ['_c0','_c1']    

    return valores


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """

    columnas_c0c4 = tbl1.iloc[:,[0,1]]
    tuplas = [tuple(x) for x in columnas_c0c4.to_records(index=False)]
    sorted_tupla = sorted(tuplas, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
                
    tabla1=[]
    for key, value in diccionario.items():
        tupla=(key, value)
        tabla1.append(tupla)

    sorted_data = [(key, sorted(values)) for key, values in tabla1]
    formatted_data = [(key, ','.join(map(str, values))) for key, values in sorted_data]

    tabla = pd.DataFrame(formatted_data)

    tabla.columns = ['_c0','_c4']

    return tabla


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    columnas_c0c5ac5b = tbl2.iloc[:,[0,1,2]]
    tuplas = [tuple(x) for x in columnas_c0c5ac5b.to_records(index=False)]
    nuevas_tuplas = [(t[0], f"{t[1]}:{t[2]}") for t in tuplas]

    diccionario={}
    for key, value in nuevas_tuplas:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
                
    tabla2=[]
    for key, value in diccionario.items():
        tupla=(key, value)
        tabla2.append(tupla)

    sorted_tabla = [(key, sorted(values)) for key, values in tabla2]
    formatted_data = [(key, ','.join(map(str, values))) for key, values in sorted_tabla]

    tablafinal = pd.DataFrame(formatted_data)
    tablafinal.columns = ['_c0','_c5']

    return tablafinal


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    tabla = pd.merge(tbl0,tbl2,on = '_c0')
    tabla = tabla[['_c0','_c1','_c5b']]
    tabla = tabla.groupby(['_c1'])['_c5b'].sum()

    return tabla
