import requests
from bs4 import BeautifulSoup

# kod produktu bez opinii = 144826098
# product_code =  58835954
product_code = input("Podaj kod produktu: ")

# url = "https://www.ceneo.pl/"+product_code+"#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
# url = "https://www.ceneo.pl/{}#tab=reviews".format(product_code)

respons = requests.get(url)
if respons.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(respons.text, "html.parser")
        opinions = page_dom.select("div.js_product-reviews > div.js_product-review")
        if len(opinions) > 0:
            print("Sa opinie")
            opinions_all = []
            for opinion in opinions:
                single_opinion = {
                    "opinion_id": ,
                    "author": ,
                    "recommendation": ,
                    "stars": ,
                    "purchased": ,
                    "opinion_date": ,
                    "purchase_date": ,
                    "usefull_count": ,
                    "not_usefull_count": ,
                    "content": ,
                    "pros": ,
                    "cons": ,
                }
        else:
            print("Brak opinii")