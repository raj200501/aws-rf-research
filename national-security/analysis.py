import json
import boto3

def analyze_rf_data(file_name, bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    data = json.loads(response['Body'].read().decode('utf-8'))
    frequencies = data['frequency']
    signal_strengths = data['signal_strength']
    mean_strength = sum(signal_strengths) / len(signal_strengths)
    return mean_strength

if __name__ == "__main__":
    mean_strength = analyze_rf_data('rf_data.json', 'my-rf-data-bucket')
    print(f"Mean Signal Strength: {mean_strength}")
