class Agent:
    def __init__(self, agent_id, opinion):
        self.id = agent_id
        self.opinion = opinion

    def post(self):
        return {
            "agent": self.id,
            "opinion": self.opinion,
            "engagement": abs(self.opinion)
        }
