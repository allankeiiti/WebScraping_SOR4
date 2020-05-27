.. WebScraping_SOR4 documentation master file, created by
   sphinx-quickstart on Thu May 14 01:02:16 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentação do WebScraping_SOR4
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Sobre
=====
Este pequeno projeto foi criado por fins didáticos voltados à WebScraping. Por conta do lançamento
do Game, resolvi utilizar ele como assunto principal e o site MetaCritic, o qual proíbe o uso de bibliotecas
como o request, retornando erro 404 na tentativa de extrair dados do HTML.
Por conta disso, criei um pequeno Script que utilizando o Selenium, acessa as páginas do MetaCritic do Game e
salva-os na estação local.
Aproveitei para aprender sobre a documentação utilizando Sphinx, o qual gerou esta simples documentação.

Update 26-05-2020: Foi criado outro Script que realiza a verificação das Reviews do Game na Steam, além de tentar
   utilizar análise de sentimentos nas Reviews.


Como Utilizar - MetaCritic
=============
1. Baixe e coloque o executável chromedriver.exe no diretório raiz do Projeto
   A. Baixe por aqui (https://chromedriver.chromium.org/)
2. Instale as bibliotecas do Python Selenium e BeautifulSoup
   A. Abra o Terminal e execute pip install selenium BeautifulSoup, caso o usuário não tenha privilégios
      administrativos, execute pip -U install selenium BeautifulSoup
3. Execute o Script update_webpages.py
4. Execute o Script main-metacritic.py
5. Abra a planilha SOR4_Reviews.xlsx

Como Utilizar - Steam
=============
1. Instale a bibilioteca do Python steamreviews
   A. Abra o Terminal e execute pip install steamreviews, caso o usuário não tenha privilégios
      administrativos, execute pip -U install steamreviews
3. Execute o Script main-steam.py
4. Abra a planilha SOR4_Reviews_Steam.xlsx

Filtrando Reviews do MetaCritic em PT-BR
==================
1. Baixe e coloque o executável chromedriver.exe no diretório raiz do Projeto
   A. Baixe por aqui (https://chromedriver.chromium.org/)
2. Instale as bibliotecas do Python Selenium
   A. Abra o Terminal e execute pip install selenium, caso o usuário não tenha privilégios
      administrativos, execute pip -U install selenium
3. Execute o Script check_rev_language.py
4. Abra a planilha SOR4_Reviews_PTBR_MetaCritic.xlsx

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
