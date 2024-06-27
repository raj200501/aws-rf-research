import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from rf_ml_model import RFMLModel, train_model
from data_preprocessing import load_data, preprocess_data

if __name__ == "__main__":
    features, labels = load_data('radio_frequencies.csv')
    scaled_features = preprocess_data(features)
    X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels, test_size=0.2, random_state=42)

    train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.long))
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

    model = train_model(train_loader)

    torch.save(model.state_dict(), 'rfml_model.pth')
