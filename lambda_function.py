import os
import boto3
import pandas as pd
import pymysql
from io import StringIO
import re
from datetime import datetime

def lambda_handler(event, context):
    # Obtenha os parâmetros bucket_name e object_key da requisição HTTP
    bucket_name = event["queryStringParameters"]["bucket_name"]
    object_key = event["queryStringParameters"]["object_key"]
    
    # Leia o arquivo CSV do bucket S3
    s3 = boto3.client('s3')
    csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_string = csv_obj["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    
    # Trate os dados
    # Remova a máscara dos campos CPF e CNPJ
    df["cpf"] = df["cpf"].apply(lambda x: re.sub(r'\D', '', x))
    df["cnpj"] = df["cnpj"].apply(lambda x: re.sub(r'\D', '', x))
    
    # Converta as colunas de data para o padrão yyyy-MM-dd
    date_columns = ['data1', 'data2']  # Substitua pelos nomes das colunas de data
    for col in date_columns:
        df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')
    
    # Conecte-se ao banco de dados e salve os dados tratados
    connection = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )
    
    with connection.cursor() as cursor:
        for index, row in df.iterrows():
            sql = """
                INSERT INTO minha_tabela (cpf, cnpj, data1, data2, ...)
                VALUES (%s, %s, %s, %s, ...);
            """  # Substitua "minha_tabela" pelo nome da tabela e adicione os nomes e valores das outras colunas
            cursor.execute(sql, (row["cpf"], row["cnpj"], row["data1"], row["data2"], ...))
        connection.commit()

    return {
        'statusCode': 200,
        'body': 'Dados processados e salvos no banco de dados.'
    }
