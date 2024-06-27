import torch
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader, TensorDataset
from rf_ml_model import RFMLModel
from data_preprocessing import load_data, preprocess_data

def evaluate_model(model, test_loader):
    model.eval()
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for data, labels in test_loader:
            outputs = model(data)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.numpy())
            all_labels.extend(labels.numpy())

    accuracy = accuracy_score(all_labels, all_preds)
    return accuracy

if __name__ == "__main__":
    features, labels = load_data('radio_frequencies.csv')
    scaled_features = preprocess_data(features)
    _, X_test, _, y_test = train_test_split(scaled_features, labels, test_size=0.2, random_state=42)

    test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32), torch.tensor(y_test, dtype=torch.long))
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    model = RFMLModel()
    model.load_state_dict(torch.load('rfml_model.pth'))

    accuracy = evaluate_model(model, test_loader)
    print(f'Test Accuracy: {accuracy * 100:.2f}%')
