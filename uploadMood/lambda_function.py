import boto3
import base64


s3 = boto3.client('s3')
bucket = 'wavelydx-moods'


def lambda_handler(event, context):
    try:
        data = base64.b64decode(event['body'])
        
        mood = event['mood']
        if mood not in ['happy', 'sad', 'calm']:
            raise IllegalArgumentException('Invalid mood', mood)
        
        content_type = event['content_type']
        if content_type not in ['mp3', 'wav']:
            raise IllegalArgumentException('Invalid input type', mood)

        file_name = f"{mood}/{mood}.{content_type}"

        existing_files = s3.list_objects_v2(Bucket=bucket, Prefix=f"{mood}/")
        if 'Contents' in existing:
            for object in existing_files['Contents']:
                print('Deleting', object['Key'])
                s3.delete_object(Bucket=bucket, Key=object['Key'])
        s3.put_object(Bucket=bucket, Key=file_name, Body=data)
        
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket,
                'Key': file_name
            } ,
            ExpiresIn=3600
        )

        print("Upload succeeded", url)
        return url
    except Exception as e:
        print(e)
        raise e
