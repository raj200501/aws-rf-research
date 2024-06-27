import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name or file_name)
        print(f'Successfully uploaded {file_name} to {bucket}')
    except Exception as e:
        print(f'Failed to upload {file_name}: {e}')

if __name__ == "__main__":
    upload_to_s3('processed_radio_frequencies.csv', 'my-bucket')
