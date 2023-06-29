import torch
device = "cuda" if torch.cuda.is_available() else "gpu"
import torch.nn as nn
from tqdm.auto import tqdm

def train_step(model: torch.nn.Module,
               dataloader: torch.utils.data.DataLoader,
               loss_fn: torch.nn.Module,
               optimizer: torch.optim.Optimizer):
    model.train()

    #Setup loss and train accuracy
    train_loss, train_acc = 0, 0

    #Loop through data loader and data batches
    for batch, (x, y) in enumerate(dataloader):
        x, y = x.to(device), y.to(device)

        y_preds = model(x)
        loss = loss_fn(y_preds, y)
        train_loss += loss.item()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        y_pred_class = torch.argmax(torch.softmax(y_preds, dim = 1), dim = 1)
        train_acc += (y_pred_class == y).sum().item() / len(y_preds)

    train_loss = train_loss / len(dataloader)
    train_acc = train_acc / len(dataloader)

    return train_loss, train_acc

def test_step(model: torch.nn.Module,
              dataloader: torch.utils.data.DataLoader,
              loss_fn: torch.nn.Module,
              device: device):
    model.eval()

    test_loss, test_acc = 0, 0

    with torch.inference_mode():
        for batch, (x, y) in enumerate(dataloader):
            x, y = x.to(device), y.to(device)

            y_preds = model(x)
            loss = loss_fn(y_preds, y)
            test_loss += loss.item()

            y_pred_class = torch.argmax(torch.softmax(y_preds, dim = 1), dim = 1)
            test_acc += (y_pred_class == y).sum().item() / len(y_preds)

        test_loss = test_loss / len(dataloader)
        test_acc = test_acc / len(dataloader)

        return test_loss, test_acc

def train(model: torch.nn.Module,
          train_dataloader: torch.utils.data.DataLoader,
          test_dataloader: torch.utils.data.DataLoader,
          optimizer: torch.optim.Optimizer,
          loss: torch.nn.Module = nn.CrossEntropyLoss(),
          epochs: int = 5,
          device = device):
    
    results = {"train_loss": [],
               "train_acc": [],
               "test_loss": [],
               "test_acc": []}

    for epoch in tqdm(range(epochs)):
        train_loss, train_acc = train_step(model, train_dataloader, loss, optimizer)
        test_loss, test_acc = test_step(model, test_dataloader, loss, device)

        print(f"Epoch: {epoch} | Training Loss: {train_loss:.4f} | Training Acc: {train_acc:.4f} | Testing Loss: {test_loss:.4f} | Testing Acc: {test_acc:.4f}")

        results["train_loss"].append(train_loss)
        results["train_acc"].append(train_acc)
        results["test_loss"].append(test_loss)
        results["test_acc"].append(test_acc)

    return results
