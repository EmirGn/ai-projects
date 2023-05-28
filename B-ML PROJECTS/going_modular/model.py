
import torch.nn as nn

class CNNModel(nn.Module):
    def __init__(self, in_channels: int,
                 hidden_channels: int,
                 out_channels: int):
        super(CNNModel, self).__init__()
        self.conv_block1 = nn.Sequential(
            nn.Conv2d(in_channels, hidden_channels, kernel_size = 3, stride = 1, padding = 0),
            nn.ReLU(),
            
            nn.Conv2d(hidden_channels, hidden_channels, kernel_size = 3, stride = 1, padding = 0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size = 2, stride = 2),
        )
        
        self.conv_block2 = nn.Sequential(
            nn.Conv2d(hidden_channels, hidden_channels, kernel_size = 3, stride = 1, padding = 0),
            nn.ReLU(),
            
            nn.Conv2d(hidden_channels, hidden_channels, kernel_size = 3, stride = 1, padding = 0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size = 2, stride = 2),
        )
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(hidden_channels * 13 * 13, 512),
            nn.ReLU(),
            nn.Linear(512, out_channels)
        )
        
    def forward(self, x):
        return self.classifier(self.conv_block2(self.conv_block1(x)))
