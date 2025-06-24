# imorting the libraries 
import os
import clip
import torch
from PIL import Image

# load model and preprocesing
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def extract_image_feature(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model.encode_image(image)
        features = features/ features.norm(dim = -1,keepdim = True)
    return features.cpu().numpy().flatten()
