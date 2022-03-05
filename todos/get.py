import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")
TableName = 'JOGADOR'


def get(event, context):
    table = dynamodb.Table(TableName)

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id_jogador': event['pathParameters']['id_jogador']
        }
    )

    item = result.get('Item')
    if not item:
        return json.dumps({'error': 'Jogador does not exist'}), 404

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
