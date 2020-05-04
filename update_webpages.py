from random import randint
from time import ctime, sleep
from os import stat, mkdir, getcwd
from datetime import date, datetime
from selenium import webdriver
from sys import exit


class updateWebPages():
    """
        Classe que
    """
    def __init__(self):
        self.Current_Date = date.today()
        self.create_folder()
        self.platforms = ['playstation-4', 'xbox-one', 'switch', 'pc']
        print('Classe update_webpages Iniciada.')
        try:
            self.browser = webdriver.Chrome(fr'{getcwd()}\chromedriver.exe')
        except FileNotFoundError:
            print('Por Favor, coloque o arquivo "chromedriver.exe" dentro da pasta do Projeto e inicie novamente '
                  '\nAdquira o executável aqui: https://chromedriver.chromium.org/')
            exit()
        print('WebDriver Iniciado.')

    def return_modify_date(self, platform, file):
        if platform not in self.platforms:
            print('Plataforma do jogo Streets Of Rage 4 não foi encontrada.')
        else:
            createDate = datetime.strptime(ctime(stat(file).st_mtime), '%a %b %d %H:%M:%S %Y').date()
            return createDate

    def random_seconds(self):
        return randint(10, 90)

    def create_folder(self):
        try:
            mkdir('WebPages')
        except FileExistsError:
            print('A pasta WebPages já foi criada no diretório do Projeto.')

    def create_html_files(self):
        for platform in self.platforms:
            print(platform)
            self.browser.get(f'https://www.metacritic.com/game/{platform}/streets-of-rage-4/user-reviews')
            content = self.browser.page_source
            with open(fr'{getcwd()}\WebPages\metacritic_sor4_{platform}.html', 'w', encoding='utf8') as f:
                f.write(content)
            print(f'Criado o arquivo HTML da página do {platform}!')
            sleep(30)

    def update_html_files(self):
        try:
            for platform in self.platforms:
                if self.Current_Date != self.return_modify_date(platform=platform, file=f'WebPages\metacritic_sor4'
                                                                                        f'_{platform}.html'):
                    self.browser.get(f'https://www.metacritic.com/game/{platform}/streets-of-rage-4/user-reviews')
                    content = self.browser.page_source
                    with open(fr'{getcwd()}\metacritic_sor4_{platform}.html', 'w', encoding='utf8') as f:
                        f.write(content)
                    print(f'Atualização da página do {platform} Completa!')
                    seconds = self.random_seconds()
                    sleep(seconds)
                else:
                    print(f'Arquivo da ágina do {platform} Já foi atualizada Hoje. Tente Novamente Amanhã.')
        except FileNotFoundError:
            print('Criando arquivos HTML.')
            self.create_html_files()


if __name__ == '__main__':
    x = updateWebPages()
    x.update_html_files()
