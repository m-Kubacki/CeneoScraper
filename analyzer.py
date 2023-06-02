import os
import json
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# print([filename.removesuffix(".json") for filename in os.listdir("opinions")])
print(*list(map(lambda x: x.removesuffix(".json"),os.listdir("opinions"))), sep = "\n")
product_code = input("Podaj kod produktu: ")
opinions = pd.read_json(f"opinions/{product_code}.json")
print(opinions)
opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",", ".")))

try:
    os.mkdir("charts")
except FileExistsError:
    pass

stats = {
    # 'opinions_count': len(opinions),
    'opinions_count': opinions.shape[0],
    'pros_count': opinions.pros.map(bool).sum(),
    'cons_count': opinions.cons.map(bool).sum(),
    'average_score': opinions.stars.mean()
}
print(f"""dla produktu o identyfikatorze {product_code} pobrano {stats['opinions_count']} opinii.
Dla {stats['pros_count']} opinii podana zostala lista zalet produktu, a dla {stats['cons_count']} opinii podana zostala lista jego wad.
Srednia ocena produktu wynosi {stats['average_score']:.2f}""")
colors_stars ={}
for i in np.arange(0,5.5,0.5):
    colors_stars[i] = "crimson" if i <= 2.5 else "steelblue" if i <= 3.5 else "forestgreen"

stars = opinions.stars.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
print(stars)
stars.plot.bar(color=colors_stars.values())
plt.xticks(rotation='horizontal')

plt.title("rozklad liczby gwizdek w opiniach konsumentow")
plt.xlabel("liczba gwiazdek")
plt.ylabel("liczba opinii")
plt.ylim(0,max(stars)+10)
plt.grid()
for index, value in enumerate(stars):
    plt.text(index, value+0.5, str(value), ha = 'center')

recommendations = opinions['recommendation'].value_counts(dropna=False).reindex(["Polecam", "Nie polecam", None], fill_value=0)
recommendations.plot.pie(
    label="",
    autopct = lambda p: '{:.f1}%'.format(round(p)) if p>0 else '',
    labels=['Polecam', "Nie polecam", "nie mam zdania"],
    colors = ['forestgreen', 'crimson', 'steelblue']
)
plt.legend(loc='upper center', ncol=3)
plt.title("Rozklad rekomendacji w opiniach konsumentow ")

plt.savefig(f"charts/{product_code}_stars.png")
plt.savefig(f"charts/{product_code}recommendations.png")
plt.close()

stats['stars'] = stars.to_dict()
stats['recommendations'] = recommendations.to_dict()

print(stats)
with open(f"stats/{product_code}.json","w", encoding="UTF-8") as jf:
    json.dump(stats, jf, indent=4, ensure_ascii=False )