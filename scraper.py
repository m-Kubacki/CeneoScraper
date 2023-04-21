import requests
from bs4 import BeautifulSoup

# kod produktu bez opinii = 144826098
product_code =  "58835954"
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
                    "opinion_id":  opinion["data-entry-id"],
                    "author": opinion.select_one("span.user-post__author-name").get_text().strip(),
                    "recommendation": opinion.select_one("span.user-post__author-recomendation > em ").get_text().strip(),
                    "stars": opinion.select_one("span.user-post__score-count").get_text().strip(),
                    "purchased": opinion.select_one("div.review-pz").get_text().strip(),
                    "opinion_date": opinion.select_one("span.user-post__published > time:nth-child(1)")['datetime'].strip(),
                    "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)").get_text().strip(),
                    "usefull_count": opinion.select_one("button.vote-yes")['data-total-vote'].strip(),
                    "not_usefull_count": opinion.select_one("button.vote-no")['data-total-vote'].strip(),
                    "content": opinion.select_one("div.user-post__text").get_text().strip(),
                    "pros":[p.get_text().strip for p in  opinion.select("div.review-feature__title--positives ~ div.review-feature__item")],
                    "cons":[c.get_text().strip for c in  opinion.select("div.review-feature__title--positives ~ div.review-feature__item")]
                }
        # else:
        #     print("Brak opinii")
        opinions_all.append(single_opinion)
print(opinions_all)