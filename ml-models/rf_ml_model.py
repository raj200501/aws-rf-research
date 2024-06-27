import torch
import torch.nn as nn
import torch.optim as optim

class RFMLModel(nn.Module):
    def __init__(self):
        super(RFMLModel, self).__init__()
        self.layer1 = nn.Linear(100, 256)
        self.layer2 = nn.Linear(256, 128)
        self.layer3 = nn.Linear(128, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x

def train_model(train_loader, epochs=10):
    model = RFMLModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        for data, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(data)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')

    return model

if __name__ == "__main__":
    # Assume train_loader is defined and loads data
    model = train_model(train_loader)
    torch.save(model.state_dict(), 'rfml_model.pth')
