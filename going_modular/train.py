import os
import torch
import torch.nn as nn
import data_setup, engine, model

from torchvision import transforms

epochs = 10
batch_size = 32
in_channels = 3
hidden_channels = 64
out_channels = 3
learning_rate = 0.001

train_dir = "/content/datas/pizza_steak_sushi/train"
test_dir = "/content/datas/pizza_steak_sushi/test"

device = "cuda" if torch.cuda.is_available() else "gpu"

data_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.TrivialAugmentWide(),
    transforms.ToTensor()
])

model = model.CNNModel(in_channels, hidden_channels, out_channels).to(device)

train_dataloader, test_dataloader, class_names = data_setup.create_dataloader(train_dir, test_dir, data_transform, batch_size = batch_size)

loss = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

engine.train(model, train_dataloader, test_dataloader, optimizer, loss, epochs = epochs, device = device)
