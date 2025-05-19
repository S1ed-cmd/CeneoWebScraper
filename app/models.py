import os
import json
import requests
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
from config import headers




class Product:
    def __init__(self, product_id ,product_name ,opinions, stats):
        self.product_id = product_id
        self.product_name = product_name
        self.opinions = opinions
        self.stats = stats

def __str__(self):
    return f"product_id:{self.product_id}\nproduct_name:{self.product_name}\nstats: "+json.dumps(self.stats, indent =4,
    ensure_acsii=False)+"\nopinions"+"\n\n".join([str(Opinion) for opinion in self.opinions])
    

def __repr__(self):
    return f"Product(product_id={self.product_id}, product_name={self.product_name}, opinions=["+",".join(repr(opinion) for opinion in self.opinions)+f"], stats={self.stats})"




def get_link(self):
        return f"https://www.ceneo.pl/{self.product_id}#tab=reviews"


def extract_name(self):
   response = requests.get(self.get_link(), headers = headers)
   page_dom = BeautifulSoup(response.text, 'html.parser')
   self.product_name = page_dom.select_one("h1")

def opinions_to_dict(self):
    return[opinions_to_dict() for opinion in self.opinions]

def calculate_stars(self):
    opinions = pd.DataFrame.from_dict(opinions_to_dict())
    self.stats["opinions_count"] = opinions.shape[0]
    self.stats["opinions_count"] = opinions.shape[0]
    self.stats["pros_count"] = sum(opinions.pros_pl.astype(bool)) # converts the list into a bool [empty]/[not-empty], the sum counts trues a 1s and falses as 0s
    self.stats["cons_count"] = sum(opinions.cons_pl.astype(bool))
    self.stats["pros_cons_count"] = opinions.apply(lambda opinion: bool(opinion.pros_pl) and bool(opinion.cons_pl), axis=1).sum() 
    self.stats["average_score"] = opinions.score.mean()
    self.stats["pros"] = opinions.pros_en.explode().value_counts()
    self.ststs["cons"] = opinions.cons_en.explode().value_counts()
    self.ststs["recommendations"] = opinions.recommendation.value_counts(dropna=False).reindex([True, False, None], fill_value=0)
    self.stats["scores"] = opinions.score.value_counts().reindex(list(np.arange(0.5,5.5,0.5)), fill_value=0)


def generate_charts(self):
 if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
 with open(f"./opinions/{product_id}.json", "w", encoding="UTF-8") as json_file:
    json.dump(all_opinions, json_file, indent=4, ensure_ascii=False)

 self.stats["recommendations"].plot.pie(
    label = "",
    labels = ["Recommend", "Not recommend", "No opinion"],
    colors = ["forestgreen", "crimson", "steelblue"], 
    autopct = lambda r: f"{r:.1f}%" if r > 0 else "" 
)
plt.title(f"recommendations for product {product_id}")

plt.savefig(f"./pie_charts/{product_id}.png")
plt.plot()


ax = self.stats["scores"].plot.bar(
    color = ["forestgreen" if s > 3.5 else "crimson" if s < 3 else "steelblue" for s in scores.index]
    )
plt.bar_label(container=ax.containers[0])
plt.xlabel("Score")
plt.ylabel("Number of opinions")
no_opinions = len(opinions)
plt.title("Number of opinions about {product_id} by their respective scores.\nTotal number of opinions: {no_opinions}")
plt.xticks(rotation=0)
plt.savefig(f"./bar_charts/{product_id}.png")
plt.show()


class Opinion:
    selectors = {
        'opinion_id': (None, "data-entry-id"),
        'author': ("span.user-post__author-name",),
        'recommendation': ("span.user-post__author-recomendation > em",),
        'score': ("span.user-post__score-count",),
        'content_pl': ("div.user-post__text",),
        'pros_pl': ("div.review-feature__item--positive", None, True),
        'cons_pl': ("div.review-feature__item--negative", None, True),
        'thumbs_up': ("button.vote-yes", "data-total-vote",),
        'thumbs_down': ("button.vote-no", "data-total-vote",),
        'date_published': ("span.user-post__published > time:nth-child(1)", "datetime"),
        'date_purchased': ("span.user-post__published > time:nth-child(2)", "datetime")
    }

    def __init__(self, opinion_id, author, recommendation, score, content, pros, cons, thumbs_up, thumbs_down, date_published, date_purchased):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.score = score
        self.content = content
        self.pros = pros
        self.cons = cons
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        self.date_published = date_published
        self.date_purchased = date_purchased

        
    def __str__(self):
        return "\n".join([f"{key}: {getattr(self,key)}" for key in self.selectors.keys()])

    def __repr__(self):
        return "Opinion("+", ".join([f"{key}={getattr(self,key)}" for key in self.selectors.keys()])+")"
    
    def to_dict(self):
        return {key: {getattr(self,key)} for key in self.selectors.keys()}