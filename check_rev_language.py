import pandas as pd
from selenium import webdriver
from sys import exit
from time import sleep


class checkReviewLang():
    """
        Esta Classe foi criado para detectar do DataFrame do MetaCritic as reviews que não são em PT-BR e então
        retirá-las. Utilizando o Selenium
    """
    def __init__(self):
        try:
            self.browser = webdriver.Chrome('chromedriver.exe')
        except FileNotFoundError:
            print('Por Favor, coloque o arquivo "chromedriver.exe" dentro da pasta do Projeto e inicie novamente '
                  '\nAdquira o executável aqui: https://chromedriver.chromium.org/')
            exit()
        self.reviews = list(pd.read_excel('SOR4_Reviews.xlsx').Review)

    def check_language(self, language_selected='português'):
        """
            Função que verifica o idioma da Review dentro do DataFrame
        :param language_selected: O idioma da Review que deseja salvar. inglês, japonês, etc (default: português)
        """
        self.review_ptbr = []
        self.browser.get('https://translate.google.com/?hl=pt-BR')
        opt = self.browser.find_element_by_class_name('sl-sugg-button-container')
        opt.find_element_by_class_name('jfk-button-collapse-right').click()
        opt.find_element_by_class_name('jfk-button-collapse-right').click()
        for review in self.reviews:
            translate_field = self.browser.find_element_by_id('source')
            translate_field.click()
            translate_field.send_keys(review[0:25])
            sleep(5)
            language = opt.find_element_by_class_name('jfk-button-collapse-right').text.lower().split(' ')[0]
            if language == language_selected:
                print(review)
                self.review_ptbr.append(review)
            translate_field.clear()
        self.browser.close()

    def save_dataFrame(self):
        """ Função que lê as Reviews do arquivo SOR4_Reviews.xlsx e retira todas as ROWs que não são
            do Idioma que foi verificado na check_language()"""
        self.reviews = pd.read_excel('SOR4_Reviews.xlsx')
        self.reviews = self.reviews.loc[self.reviews.Review.isin(self.review_ptbr)]
        self.reviews.to_excel('SOR4_Reviews_PTBR_MetaCritic.xlsx')


if __name__ == '__main__':
    x = checkReviewLang()
    x.check_language()
    x.save_dataFrame()
