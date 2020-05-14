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


Como Utilizar
=============
1. Baixe e coloque o executável chromedriver.exe no diretório raiz do Projeto
   A. Baixe por aqui (https://chromedriver.chromium.org/)
2. Instale as bibliotecas do Python Selenium e BeautifulSoup
   A. Abra o Terminal e execute pip install selenium BeautifulSoup, caso o usuário não tenha privilégios
      administrativos, execute pip -U install selenium BeautifulSoup
3. Execute o Script update_webpages.py
4. execute o Script main.py
5. Abra a planilha SOR4_Reviews.xlsx
6. Para realizar a análise das Reviews, utilize a biblioteca Pandas e sua criatividade
      A. Abra o Terminal e execute pip install pandas

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
