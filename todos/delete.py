
import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")
TableName = 'JOGADOR'


def delete(event, context):
    table = dynamodb.Table(TableName)

    # delete the todo from the database
    table.delete_item(
        Key={
            'id_jogador': event['pathParameters']['id_jogador']
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
