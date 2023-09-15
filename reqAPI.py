import requests
import pandas as pd


url='http://apilivro.jogajuntoinstituto.org/'

def buscaLivro():

    response = requests.get(url+'books/')
    data=response.json()
    df = pd.DataFrame(data)
    print(df)

def cadastraLivro(livro):
    #print(url+'books/')
    response = requests.post(url+'books/', json=livro)



    
    