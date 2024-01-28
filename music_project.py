#!/usr/bin/env python
# coding: utf-8

# # Déjame escuchar la música

# # Contenido 
# 
# * [Introducción]
# * [Etapa 1. Descripción de los datos]
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypotheses)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
#     * [3.2 Hipótesis 2: preferencias musicales los lunes y los viernes](#week)
#     * [3.3 Hipótesis 3: preferencias de género en Springfield y Shelbyville](#genre)
# * [Conclusiones]

# ## Introducción 
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; y otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar las hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba tres hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 2. Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre los viernes por la noche.
# 3. Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar las hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos
#  2. Preprocesamiento de datos
#  3. Prueba de hipótesis
# 
# 
# ### Desafío
# 
# En este proyecto, preparamos un pequeño reto para ti. Incluimos un nuevo tipo de estructura de datos: las marcas temporales. Las marcas temporales son muy comunes y merecen una atención adicional. Más adelante en el programa, aprenderás mucho sobre ellas. Sin embargo, por ahora las trataremos como simples strings. Necesitamos marcas temporales en este proyecto para poner a prueba una de nuestras hipótesis. No te preocupes, te ayudaremos con esto. Tu nivel de conocimientos actual será suficiente para abordarlo.
# 
# Por ejemplo, digamos que tenemos dos marcas temporales: `dt1 = "12:00:00"` y `dt2 = "06:00:00"`. Queremos comparar estas dos marcas temporales y ver cuál es posterior.
# 
# Podemos compararlas mediante los operadores de comparación estándar (`<`, `>`, `<=`, `>=`, `==`, `!=`). Ejecuta la siguiente celda de código para comparar dos marcas temporales:
# 

# In[1]:


# Comparar los objetos datetime

dt1 = "12:00:00"
dt2 = "06:00:00"

if dt1 < dt2:
    print("La marca temporal 2 es posterior")
else:
    print("La marca temporal 1 es posterior")




# ## Etapa 1. Descripción de los datos 
# Abre los datos en Y.Music y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[2]:


# importar pandas
import pandas as pd


# Lee el archivo `music_project_en.csv` de la carpeta dentro del proyecto y guárdalo en la variable `df`:

# In[3]:


# Para pruebas, el usuario debe definir la ruta del archivo csv donde se encuentra el proyecto
df = pd.read_csv(r'/Users/StephyHerrera/Desktop/music_project/music_project_en.csv') 


# Muestra las 10 primeras filas de la tabla:

# In[4]:



(df.head(10))


# Obtén la información general sobre la tabla con un comando:

# In[5]:



df.info()


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Todas almacenan el mismo tipo de datos: `object` (objeto).
# 
# Según la documentación:
# - `' userID'` — identificador del usuario o la usuaria;
# - `'Track'` — título de la canción;
# - `'artist'` — nombre del artista;
# - `'genre'` — género musical;
# - `'City'` — ciudad del usuario o la usuaria;
# - `'time'` — hora exacta en la que se reprodujo la canción;
# - `'Day'` — día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas; otros, en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. `Detecta el tercer problema por tu cuenta y descríbelo aquí`.
# 
# 
# 

# 3.Que UserID esta junto en ves de tener una separación 'user_id'.

# 
# `Escribe tus observaciones aquí:
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?` Tenemos los datos de la población de Springfield y Shelbyville de lo que escucha cada usuario, el tipo de genero, el día y la hora. Podemos entender lo que almacenan las columnas por el nombre del encabezado ya que concuerda con la información que almacena la columna.
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestras tres hipótesis o necesitamos más información?`
#  Hay suficientes datos ya que contamos con 65079 filas de información.
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# El método info me ayudo a ver los valores ausentes o nulos que había en los datos.

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado 
# Muestra los encabezados de la tabla:

# In[6]:



(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * todos los caracteres deben ser minúsculas;
# * elimina los espacios;
# * si el nombre tiene varias palabras, utiliza snake_case.

# Pon todos los caracteres en minúsculas y muestra el encabezado de la tabla de nuevo:

# In[7]:



new_col_names = []
for old_name in df.columns:
    name_lowered = old_name. lower()
    name_no_spaces = name_lowered
    new_col_names.append( name_no_spaces)
df.columns = new_col_names
print(df.columns)


# Ahora elimina los espacios al principio y al final de los encabezados y muéstralos:

# In[8]:



new_col_names = []
for old_name in df.columns:
    name_stripped = old_name. strip()
    new_col_names.append(name_stripped)
df.columns = new_col_names
print(df.columns)


# Aplica snake_case al encabezado userID y muestra el encabezado de la tabla:

# In[9]:



columns_new = {'userid' : 'user_id', }
df.rename(columns = columns_new, inplace = True)

print(df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[10]:



(df.columns)



# ### Valores ausentes 
# Primero, encuentra el número de valores ausentes en la tabla. Para ello, utiliza dos métodos pandas:

# In[11]:



print(df.isna().sum())


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Para hacer esto, crea la lista `columns_to_replace`, recórrela con un bucle `for` y reemplaza los valores ausentes en cada columna:

# In[12]:



columns_to_replace = ['track', 'artist', 'genre']
for col in columns_to_replace:
    df[col].fillna('unknown', inplace=True)
    print(df)


# Asegúrate de que la tabla no contiene más valores ausentes. Cuenta de nuevo los valores ausentes.

# In[13]:



print(df.isna().sum())




# ### Duplicados 
# Encuentra el número de duplicados explícitos en la tabla usando un comando:

# In[14]:



print(df.duplicated().sum()) 


# Llama al método `pandas` para deshacerte de los duplicados explícitos:

# In[15]:



df = df.drop_duplicates()


# Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[16]:



print(df.duplicated().sum()) 


# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para hacerlo:
# * recupera la columna deseada del dataFrame;
# * llama al método que te devolverá todos los valores de columna únicos;
# * aplica un método de ordenamiento a tu resultado.
# 

# In[17]:



df.sort_values(by='genre')['genre'].unique()


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, declara la función `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=` — la lista de duplicados;
# * `correct_genre=` — el string con el valor correcto.
# 
# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplaza cada valor de la lista `wrong_genres` con el valor en `correct_genre`. Utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos y reemplazarlos con el género correcto en la lista principal.

# In[18]:



def replace_wrong_genres(wrong_genres, correct_genre):
    for wrong_genres in  wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genres, correct_genre)


# Llama a `replace_wrong_genres()` y pásale argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[19]:



wrong_genres = ['hip', 'hop', 'hip-hop']
correct_genre = 'hiphop'
replace_wrong_genres(wrong_genres,correct_genre)
    


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[20]:




(df['genre'].sort_values().unique()) 




# ### Tus observaciones 
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`

# La verdad me costo mucho trabajo, llegar al segundo código para remplazar los duplicados.

# Hemos tenido un proceso de limpieza de los datos, eliminando duplicados, datos nulos remplazandolos por 'know', eliminando mayúsculas que pueden afectar nuestro proceso a la hora de buscar datos, también hemos corregido errores ortográficos para facilitar su busqueda.



# ## Etapa 3. Prueba de hipótesis 

# ### Hipótesis 1: comparar el comportamiento del usuario o la usuaria en las dos ciudades 

# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[21]:



df.groupby('city')['track'].count()


# `Comenta tus observaciones aquí`: En este apartado de la hipótesis queremos observar la cantidad de reproducciones musicales que hay en cada ciudad para verificar si hay alguna diferencia entre Springfield y Shelbyville

# Ahora agrupa los datos por día de la semana y encuentra el número de canciones reproducidas el lunes, miércoles y viernes.
# 

# In[22]:



df.groupby('day')['track'].count()


# `Comenta tus observaciones aquí`: En este apartado podemos observar que el día viernes es el día con mayor reproducciones de canciones.

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la `number_tracks()` para calcular el número de canciones reproducidas en un determinado día y ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'`.
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[23]:



def number_tracks(df, day, city):
    track_list = df[(df['day'] == day) & (df['city'] == city)]
    track_list_count =(track_list['user_id'].count())
    return track_list_count

result = number_tracks(df, day='Monday', city='Springfield')
print(result)


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[24]:



print(number_tracks(df, day='Monday', city='Springfield'))


# In[25]:



print(number_tracks(df, day='Monday', city='Shelbyville'))


# In[26]:



print(number_tracks(df, day='Wednesday', city='Springfield'))


# In[27]:



print(number_tracks(df, day='Wednesday', city='Shelbyville'))


# In[28]:



print(number_tracks(df, day='Friday', city='Springfield'))


# In[29]:



print(number_tracks(df, day='Friday', city='Shelbyville'))


# Utiliza `pd.DataFrame` para crear una tabla, donde
# * Los encabezados de la tabla son: `['city', 'monday', 'wednesday', 'friday']`
# * Los datos son los resultados que conseguiste de `number_tracks()`

# In[30]:



number_tracks = [
    ['Shelbyville', '5614', '7003', '5895' ],
    ['Springfield', '15740', '11056', '15945'],
]
entries = ['city', 'monday', 'wednesday', 'friday']
time = pd.DataFrame(data=number_tracks, columns=entries)
print(time)


# **Conclusiones**
# 
# `Comenta si la primera hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# Si es correcta porque con la extracción de los datos podemos ver como Springfield escucha un total de 42741 y Shelbyville escucha un total de 18512, esto nos muestra que Springfield es la ciudad que más música escucha. 



# ### Hipótesis 2: música al principio y al final de la semana 

# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros diferentes a los que disfrutan los usuarios de Shelbyville.

# Cree dos tablas con los nombres proporcionados en los dos bloques de código siguientes:
# * Para Springfield — `spr_general`
# * Para Shelbyville — `shel_general`

# In[31]:


spr_general = df[df['city'] == 'Springfield']
print(spr_general)


# In[32]:



shel_general = df[df['city'] == 'Shelbyville']
print(shel_general)


# Escribe la función `genre_weekday()` con cuatro parámetros:
# * Una tabla para los datos (`df`)
# * El día de la semana (`day`)
# * La primera marca de tiempo, en formato (`time1`)
# * La última marca de tiempo, en formato (`time2`)
# 
# La función debería devolver información de los 15 géneros más populares de un día determinado en un período entre dos marcas de fecha y hora.
# Aplique la misma lógica de filtrado consecutivo, pero esta vez utilice cuatro filtros y luego cree una nueva columna con los respectivos recuentos de reproducción.
# Ordene el resultado de mayor a menor y devuélvalo.

# In[33]:



def genre_weekday(df, day, time1, time2):
   
    genre_df = df[(df['day'] == day) & (df['time'] > time1) & (df['time'] < time2)] # escribe tu código aquí

   
    genre_df_count = genre_df.groupby('genre')['track'].count() 

    
    genre_df_sorted = genre_df_count.sort_values(ascending = False) 

    return genre_df_sorted[:15]


# Compara los resultados de la función `genre_weekday()`para Springfield y Shelbyville el lunes por la mañana (de 7 a 11) y el viernes por la tarde (de 17:00 a 23:00). Utilice el mismo formato de 24 horas que el conjunto de datos (por ejemplo, 05:00 = 17:00:00):

# In[34]:



genre_weekday(spr_general, 'Monday', '07:00:00', '11:00:00]')


# In[35]:



genre_weekday(shel_general, 'Monday', '07:00:00', '11:00:00]')


# In[36]:



genre_weekday(spr_general, 'Friday', '07:00:00', '11:00:00]')


# In[37]:



genre_weekday(shel_general, 'Friday', '07:00:00', '11:00:00]')


# **Conclusión**
# 
# `Comente si la segunda hipótesis es correcta o debe rechazarse. Explique su razonamiento.`
# La hipótesis es parcialmente correcta, escuchan casi los mismos generos entre las dos ciudades, claro cada género en cada ciudad lo reproducen más veces en una ciudad en comparación con la otra, pero son casí los mismos, igual podemos observar como Springfield sigue siendo la ciudad que más escucha música.



# ### Hipótesis 3: preferencias de género en Springfield y Shelbyville 
# Hipótesis: Shelbyville ama la música rap. A los residentes de Springfield les gusta más el pop.

# Agrupa la tabla `spr_general` por género y encuentra el número de canciones reproducidas de cada género con el método `count()`. Después, ordena el resultado en orden descendente y guárdalo en `spr_genres`.

# In[38]:



spr_genres = spr_general.groupby('genre')['track'].count().sort_values(ascending = False)


# Muestra las 10 primeras filas de `spr_genres`:

# In[39]:



print(spr_genres[:10])


# Ahora haz lo mismo con los datos de Shelbyville.
# 
# Agrupa la tabla `shel_general` por género y encuentra el número de canciones reproducidas de cada género. Después, ordena el resultado en orden descendente y guárdalo en la tabla `shel_genres`:
# 

# In[40]:



shel_general = shel_general.groupby('genre')['track'].count().sort_values(ascending = False)


# Muestra las 10 primeras filas de `shel_genres`:

# In[41]:



print(shel_general[:10])


# **Conclusión**
# 
# Se debe rechazar, según los datos extraidos podemos ver que a ambás ciudades lo que más les gusta es el pop a Springfield le gusta mas el pop que ha Shelbyville 


# # Conclusiones

# 
# Con este proyecto pude darme cuenta el poder que pueden tener los datos ya que uno puede crear ciertas hipótesis que pueden ser ciertas o falsas, conforme se avanza el proyecto y los datos salen, pude diferenciar los géneros de música que más escuchaba cada ciudad entre Lunes-Viernes, cómo Springfield fue de las ciudades qué mas escucha música y que el género favorito tanto de Springfield y Shelbville es el Pop.
# Con esto puedo darme cuenta que es sencillo y rápido extraer los datos y encontrar resultados a hipótesis o problemas que necesitemos resolver con datos.
# Stephy Herrera.