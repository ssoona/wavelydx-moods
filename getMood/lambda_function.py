import boto3
import random


s3 = boto3.client('s3')
bucket = 'wavelydx-moods'


def lambda_handler(event, context):

    random_mood = random.choice(['happy', 'sad', 'calm'])
    try:
        mood_file = s3.list_objects_v2(Bucket=bucket, Prefix=f"{random_mood}/")
        if 'Contents' in mood_file:
            for object in mood_file['Contents']:
                url = s3.generate_presigned_url(
                    ClientMethod='get_object', 
                    Params={
                        'Bucket': bucket,
                        'Key': object['Key']
                    },
                    ExpiresIn=3600
                )
                return url
        raise Exception("No mood file for", random_mood)
    except Exception as e:
        print(e)
        raise e
