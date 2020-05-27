import steamreviews
import pandas as pd

# Este Script foi utilizado para pegar as reviews em PT-BR do Game na plataforma da Steam utilizando o steamreviews

app_id = 985890
review_dict, query_count = steamreviews.download_reviews_for_app_id(app_id)
reviews_steam = pd.DataFrame(review_dict['reviews'])
reviews_steam = reviews_steam.transpose()

# Filtrando reviews em PT-BR
reviews_steam = reviews_steam.loc[reviews_steam.language == 'brazilian']
reviews_steam = reviews_steam[['review', 'voted_up']]

# Retirando tags Regex como \n
regex_tags = ['\n', '\b']
for regex_tag in regex_tags:
    reviews_steam['review'] = reviews_steam.review.str.replace(regex_tag, '')
reviews_steam['review'] = reviews_steam.review.str.lower()
reviews_steam['review'] = reviews_steam.review.str.replace('   ', ' ')

reviews_steam.to_excel('SOR4_Reviews_Steam.xlsx')
