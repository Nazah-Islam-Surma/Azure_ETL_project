import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files(
  "ukveteran/adventure-works",
  path="./data",
  unzip= True
)
print("Aventure works datasets downloaded")
