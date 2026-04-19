import kaggle
kaggle.api.authenticate()
kaggle.api.download_data_files(
  "datasets/ukveteran/adventure-works",
  path="./data",
  unzip= True
)
print("Aventure works datasets downloaded")
