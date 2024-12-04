# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

import os
import zipfile
import pandas as pd

def descomprimir_archivo():
    """
    Descomprime el archivo input.zip y crea la estructura de carpetas requerida.
    """
    zip_path = os.path.abspath("files/input.zip")
    extract_path = os.path.abspath("files")  # Extraer directamente en 'files/'
    
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"El archivo {zip_path} no existe.")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def procesar_directorio(base_path, sentiment_labels):
    """
    Procesa los archivos en un directorio base y devuelve un DataFrame con las frases y sentimientos.
    """
    data = []
    for sentiment in sentiment_labels:
        dir_path = os.path.join(base_path, sentiment)
        if not os.path.exists(dir_path):
            raise FileNotFoundError(f"El directorio {dir_path} no existe. Verifica la descomposición del archivo ZIP.")
        
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                phrase = file.read().strip()
                data.append({"phrase": phrase, "target": sentiment})
    return pd.DataFrame(data)

def generar_datasets():
    """
    Genera los archivos train_dataset.csv y test_dataset.csv a partir de la estructura de archivos descomprimida.
    """
    # Directorios de entrada
    train_path = os.path.abspath("files/input/train")
    test_path = os.path.abspath("files/input/test")
    sentiment_labels = ["negative", "positive", "neutral"]

    # Verificar que los directorios existen antes de procesar
    if not os.path.exists(train_path):
        raise FileNotFoundError(f"El directorio {train_path} no existe.")
    if not os.path.exists(test_path):
        raise FileNotFoundError(f"El directorio {test_path} no existe.")

    # Procesar datasets
    train_df = procesar_directorio(train_path, sentiment_labels)
    test_df = procesar_directorio(test_path, sentiment_labels)

    # Crear directorio de salida si no existe
    output_dir = os.path.abspath("files/output")
    os.makedirs(output_dir, exist_ok=True)

    # Guardar los DataFrames en archivos CSV
    train_df.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)
    test_df.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)

def pregunta_01():
    """
    Ejecuta las tareas para descomprimir el archivo y generar los datasets.
    """
    descomprimir_archivo()
    generar_datasets()

# Para ejecutar:
# pregunta_01()