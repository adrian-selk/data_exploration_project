import kagglehub

# Download dataset to a custom local directory
path = kagglehub.dataset_download("balabaskar/tom-and-jerry-image-classification", path="./data/")

print("Path to dataset files:", path)