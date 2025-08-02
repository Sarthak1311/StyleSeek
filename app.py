import streamlit as st
from PIL import Image
from search_engine import search_query

# ------------------ Page Config ------------------ #
st.set_page_config(
    page_title="StyleSeek - Visual Search",
    layout="wide",
    page_icon="🧵",
)

# ------------------ Custom CSS ------------------ #
st.markdown("""
    <style>
    .title-text {
        font-size: 3rem;
        font-weight: bold;
        color: #E91E63;
    }
    .subtitle-text {
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .footer {
        font-size: 0.8rem;
        color: #aaa;
        text-align: center;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Header ------------------ #
st.markdown('<div class="title-text">👗 StyleSeek</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Find similar fashion items using your uploaded image</div>', unsafe_allow_html=True)

# ------------------ Layout ------------------ #
left_col, right_col = st.columns([1, 2])

with left_col:
    uploaded_file = st.file_uploader("📸 Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image.resize((300, 300)), caption="Your Uploaded Image", use_column_width=False)
        st.session_state["image_ready"] = True
    else:
        st.warning("Upload a fashion image to begin!")

if uploaded_file is not None:
    with right_col:
        search_btn = st.button("🔍 Search Similar Styles")
        if search_btn:
            # Save image temporarily
            temp_path = "query.jpg"
            image.save(temp_path, format="JPEG")

            with st.spinner("Searching for similar items... 🔄"):
                results = search_query(temp_path)

            if results:
                st.success(f"Found {len(results)} similar styles!")
                st.subheader("🎯 Top Matches")

                # Display results in a responsive grid
                num_cols = 3
                rows = len(results) // num_cols + int(len(results) % num_cols != 0)
                for i in range(rows):
                    cols = st.columns(num_cols)
                    for j in range(num_cols):
                        idx = i * num_cols + j
                        if idx < len(results):
                            with cols[j]:
                                st.image(Image.open(results[idx]), caption=f"Match {idx+1}", use_column_width=True)
            else:
                st.error("No matches found. Try another image!")

# ------------------ Footer ------------------ #
st.markdown('<div class="footer">© 2025 StyleSeek — Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
