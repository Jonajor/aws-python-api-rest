import json
import logging
import time
import uuid

import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")
TableName = 'JOGADOR'


def create(event, context):
    data = json.loads(event['body'])
    if 'id_time' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    timestamp = str(time.time())

    table = dynamodb.Table(TableName)

    dados_jogador = {
        'id_jogador': str(uuid.uuid1()),
        'nacionalidade': data['nacionalidade'],
        'nivel': data['nivel']
    }

    # write the todo to the database
    table.put_item(Item=data)

    # create a response
    response = {
        "statusCode": 201,
        "body": json.dumps(dados_jogador)
    }

    return response
