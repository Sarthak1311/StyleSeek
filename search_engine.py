# search_engine.py
import os
import faiss
import numpy as np
from clip_model import extract_image_feature

def build_index(image_folder="images", index_folder="indexed_data"):
    os.makedirs(index_folder, exist_ok=True)

    images = sorted(os.listdir(image_folder))  # ensure order
    image_paths = [os.path.join(image_folder, fname) for fname in images]

    features = []
    for path in image_paths:
        try:
            feat = extract_image_feature(path)
            features.append(feat)
        except Exception as e:
            print(f"Failed to extract features from {path}: {e}")

    features = np.array(features).astype("float32")
    index = faiss.IndexFlatL2(features.shape[1])
    index.add(features)

    # Save the index and paths
    faiss.write_index(index, f"{index_folder}/faiss_index.index")
    with open(f"{index_folder}/image_paths.txt", "w") as f:
        f.write("\n".join(image_paths))
    
    print("✅ Index built and saved successfully.")

def search_query(query_image_path, top_k=5, index_folder="indexed_data"):
    query_feature = extract_image_feature(query_image_path).astype("float32").reshape(1, -1)

    index = faiss.read_index(f"{index_folder}/faiss_index.index")
    with open(f"{index_folder}/image_paths.txt", "r") as f:
        image_paths = f.read().splitlines()

    distances, indices = index.search(query_feature, top_k)
    return [image_paths[i] for i in indices[0]]
