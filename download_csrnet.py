from huggingface_hub import hf_hub_download

print("Downloading… please wait")

path = hf_hub_download(
    repo_id="TrainedModels/CSRNet",
    filename="partBmodel_best.pth",
    local_dir="."
)

print("Downloaded file saved at:", path)
