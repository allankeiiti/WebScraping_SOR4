import pandas as pd
from bs4 import BeautifulSoup
from numpy import where

"""

"""

review_base = pd.DataFrame()
platforms = ['playstation-4', 'xbox-one', 'switch', 'pc']
for platform in platforms:
    print(platform)
    page = open(fr'WebPages\metacritic_sor4_{platform}.html', 'r', encoding='utf8')
    soup = BeautifulSoup(page, 'html.parser')

    # Atribuindo os textos encontrados no Site ás variáveis reviews e grades e armazenando-os em uma lista
    reviews = [text_review.text for text_review in soup.find_all("div", class_="review_body")]
    grades = [int(grade.text) for grade in soup.find_all("div", class_="review_grade")]
    date = [grade.text for grade in soup.find_all("div", class_="date")]

    df = pd.DataFrame({'Review': reviews, 'Nota': grades, 'Data': date})
    df['Plataforma'] = platform

    # Tratamento dos dados
    print(f'{len(df)}')
    df = df.loc[df.Nota <= 10]
    regex_tags = ['\n', '\b']
    for regex_tag in regex_tags:
        df['Review'] = df.Review.str.replace(regex_tag, '')
    df['Review'] = df.Review.str.lower()
    df['Review'] = df.Review.str.replace('   ', ' ')
    df['Review'] = df.Review.str.replace(' expand', '')
    # df.to_excel(f'{platform}_reviews.xlsx')
    print(f'{len(df)}')
    df['Status'] = where(df.Nota > 5, 'Boa', 'Ruim')
    review_base = pd.concat([review_base, df])

# Persistindo o DataFrame
review_base = review_base.reset_index()
del review_base['index']
review_base.to_excel('SOR4_Reviews.xlsx')
print('Done!')
