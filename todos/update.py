import json
import time
import logging

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")
TableName = 'JOGADOR'


def update(event, context):
    data = json.loads(event['body'])
    if 'id_jogador' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(TableName)

    # update the todo in the database
    result = table.update_item(
        Key={
            'id_jogador': event['pathParameters']['id_jogador']
        },
        ExpressionAttributeNames={
          '#nome_jogador': 'nome_jogador',
        },
        ExpressionAttributeValues={
          ':nome_jogador': data['nome_jogador'],
          ':id_time': data['time']['id_time'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #nome_jogador = :nome_jogador, '
                         'time.id_time = :id_time, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
