import boto3

def collect_rf_data():
    # Simulate RF data collection
    data = {
        'frequency': [1e6, 2e6, 3e6],
        'signal_strength': [0.5, 0.8, 0.3]
    }
    return data

def upload_data_to_s3(data, bucket_name, file_name):
    s3_client = boto3.client('s3')
    s3_client.put_object(Body=str(data), Bucket=bucket_name, Key=file_name)
    print(f"Data uploaded to S3 bucket {bucket_name} with key {file_name}")

if __name__ == "__main__":
    data = collect_rf_data()
    upload_data_to_s3(data, 'my-rf-data-bucket', 'rf_data.json')
