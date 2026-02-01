class SocialRAG:
    def __init__(self, max_memory=20):
        self.memory = []
        self.max_memory = max_memory

    def store(self, posts):
        self.memory.extend(posts)
        self.memory = self.memory[-self.max_memory:]

    def summarize(self):
        if not self.memory:
            return "No dominant social signal."
        avg = sum(abs(p["opinion"]) for p in self.memory) / len(self.memory)
        if avg > 0.6:
            return "Polarized discourse dominates."
        return "Moderate discourse dominates."
