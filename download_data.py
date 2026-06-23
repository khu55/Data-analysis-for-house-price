import kagglehub

path = kagglehub.dataset_download(
    "shashanknecrotthapa/ames-housing-dataset"
)

print(path)