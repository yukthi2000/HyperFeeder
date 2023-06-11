from story import Story

class HackerNewsStory(Story):
    def __init__(self, newsRank, title, link, storyType, source):
        super().__init__(newsRank, title, link, storyType, source)
        self.hackerNewsRank = newsRank # This gives more context to the fact that this is a hacker news article for the LLM