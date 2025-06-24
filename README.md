# StyleSeek

**StyleSeek: Visual Fashion Search Engine**

StyleSeek is a content-based image retrieval system that helps users find visually similar fashion items by uploading an image. It uses OpenAI's CLIP model to extract semantic features from images and FAISS for efficient similarity search.

---

## Features

- Upload an image of any clothing item.
- Get visually similar fashion products from the database.
- Uses CLIP (ViT-B/32) for high-quality image embeddings.
- Fast nearest neighbor search using FAISS.
- Lightweight Streamlit web app interface.

---

## How it Works

1. **Image Upload:**  
   User uploads a fashion image (e.g., a shirt, dress, etc.).

2. **Feature Extraction:**  
   The image is encoded using the CLIP model to extract a feature vector.

3. **Similarity Search:**  
   The feature vector is compared to pre-indexed fashion items using FAISS to find the most similar items.

4. **Results Displayed:**  
   Similar images are shown in the interface.

---

## Project Structure

