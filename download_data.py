import os
import json

# Setup Kaggle credentials
kaggle_token = os.environ.get("KAGGLE_API_TOKEN")
kaggle_dir = os.path.expanduser("~/.config/kaggle")
os.makedirs(kaggle_dir, exist_ok=True)

with open(os.path.join(kaggle_dir, "kaggle.json"), "w") as f:
    f.write(kaggle_token)

os.chmod(os.path.join(kaggle_dir, "kaggle.json"), 0o600)

# Download dataset
import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files(
    "ukveteran/adventure-works",
    path="./data",
    unzip=True
)

print("Adventure works datasets downloaded")
