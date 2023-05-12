import requests
from bs4 import BeautifulSoup

def get_cos(ancestor,selector=None,attribute=None, return_list=False):
   try:
        if return_list:
            return  [tag.get_text().strip for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute].strip()
        if attribute:
            return  ancestor.select_one(selector)[attribute].strip()
        return  ancestor.select_one(selector).get_text().strip()
   except (AttributeError, TypeError):
        return None

# kod produktu bez opinii = 144826098
# product_code =  "58835954"
product_code = "39562616"
# product_code = input("Podaj kod produktu: ")

# url = "https://www.ceneo.pl/"+product_code+"#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
# url = "https://www.ceneo.pl/{}#tab=reviews".format(product_code)

respons = requests.get(url)
if respons.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(respons.text, "html.parser")
        # opinions = page_dom.select("div.js_product-reviews > div.js_product-review")
        opinions = page_dom.select("div.js_product-review")
        # if len(opinions) > 0:
            # print("Sa opinie")
        opinions_all = []
        for opinion in opinions:
            single_opinion = {
                    "opinion_id":  (None, "data-entry-id"),
                    "author": ("span.user-post__author-name"),
                    "recommendation":  ("span.user-post__author-recomendation > em "),
                    "stars":  ("span.user-post__score-count"),
                    "purchased": ("div.review-pz"),
                    "opinion_date": ("span.user-post__published > time:nth-child(1)",'datetime'),
                    "purchase_date":  ("span.user-post__published > time:nth-child(2)"),
                    "usefull_count":  ("button.vote-yes",'data-total-vote'),
                    "not_usefull_count":  ("button.vote-no",'data-total-vote'),
                    "content":("div.user-post__text"),
                    "pros": ("div.review-feature__title--positives ~ div.review-feature__item",None, True),
                    "cons":("div.review-feature__title--positives ~ div.review-feature__item",None, True)
                }
        # else:
        #     print("Brak opinii")

        opinions_all.append(single_opinion)
print(opinions_all)