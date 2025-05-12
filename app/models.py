class Product:
    def __init__(self):
        pass

class Opinion:
    def __init__(self,opinion_id,author,recommend,stars,content,pros,cons,up_wotes,down_wotes,published,purchased):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendr = recommend
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons =cons
        self.up_wotes = up_wotes
        self.down_wotes = down_wotes
        self.published = published
        self.purhased = purchased
    def __str__(self):
        pass