import streamlit as st
from PIL import Image
from search_engine import search_query

st.set_page_config(page_title="StyleSeek - Visual Search", layout="wide")
st.title("👗 StyleSeek: Visual Fashion Search")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image and convert to RGB (removes alpha channel)
    image = Image.open(uploaded_file).convert("RGB")

    # Resize for 5x5cm view (approx. 200x200 pixels)
    st.image(image.resize((200, 200)), caption="Query Image (5x5 cm)", use_column_width=False)

    # Save as RGB JPEG safely
    temp_path = "query.jpg"
    image.save(temp_path, format="JPEG")

    # Run search
    st.info("Searching for similar styles...")
    results = search_query(temp_path)

    # Show results
    st.subheader("🧵 Similar Fashion Items:")
    cols = st.columns(len(results))
    for i, path in enumerate(results):
        with cols[i]:
            st.image(Image.open(path), caption=f"Match {i+1}")
