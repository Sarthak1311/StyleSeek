# test_search.py
from search_engine import search_query

query_image = "/Users/sarthaktyagi/Desktop/projects /StyleSeek/query.png"  # Make sure this image exists in your root or adjust the path

print("🔍 Running image search...")
results = search_query(query_image)

print("\n🖼️ Top Matching Results:")
for i, path in enumerate(results, 1):
    print(f"{i}. {path}")
