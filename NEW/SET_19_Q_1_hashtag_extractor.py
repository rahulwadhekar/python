posts = ["#fun day", "hello #world", "#fun #python"]

tags = set()

for post in posts:
    words = post.split()
    for w in words:
        if w.startswith("#"):
            tags.add(w)

print("Trending Hashtags:", tags)