class World:
    def __init__(self, mode="chronological"):
        self.mode = mode

    def rank_posts(self, posts):
        if self.mode == "engagement":
            return sorted(posts, key=lambda p: p["engagement"], reverse=True)
        return posts
