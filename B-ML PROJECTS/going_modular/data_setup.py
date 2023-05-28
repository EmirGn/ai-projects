import os
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

num_workers = os.cpu_count()

def create_dataloader(
    train_dir: str,
    test_dir: str,
    transforms: transforms.Compose,
    batch_size = int,
    num_workers: int = num_workers):

    """
    Args:
        train_dir: Train data directory, type:string.
        test_dir: Test data directory, type: string.
        transforms: Which transform is going to be apply on the data, type: transforms.Compose.
        batch_size: Batch size for dataloader, type: integer.
        num_workers: Number of total workers, type: integer.

    Return values:
        train_dataloader, test_dataloader, class_names.
    """

    train_data = datasets.ImageFolder(
        root = train_dir,
        transform = transforms
    )

    test_data = datasets.ImageFolder(
        root = test_dir,
        transform = transforms
    )

    #Take the class names of the datas
    class_names = train_data.classes

    #Dataloader of the train and test data
    train_dataloader = DataLoader(train_data, batch_size = batch_size, num_workers = num_workers, shuffle = True, pin_memory = True, drop_last = True)
    test_dataloader = DataLoader(test_data, batch_size = batch_size, num_workers = num_workers, shuffle = True, pin_memory = True, drop_last = True)

    return train_dataloader, test_dataloader, class_names
