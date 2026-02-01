from agents import Agent
from world import World
from social_rag import SocialRAG

agents = [
    Agent("A", -0.8),
    Agent("B", -0.3),
    Agent("C", 0.0),
    Agent("D", 0.4),
    Agent("E", 0.9),
]

world = World(mode="engagement")
rag = SocialRAG()

for t in range(10):
    posts = [a.post() for a in agents]
    ranked = world.rank_posts(posts)
    rag.store(ranked[:2])
    print(f"t={t}: {rag.summarize()}")
