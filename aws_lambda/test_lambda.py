import json
def lambda_handler():
    print ("hello from lambda")
    return {
        'status_code': 200,
        'body': json.dumps('')
    }