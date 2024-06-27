import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    features = data.iloc[:, :-1].values
    labels = data.iloc[:, -1].values
    return features, labels

def preprocess_data(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features

if __name__ == "__main__":
    features, labels = load_data('radio_frequencies.csv')
    scaled_features = preprocess_data(features)
    # Save or use scaled_features and labels for training
