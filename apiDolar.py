import requests

def DolarReal():

    try:
        data = 'USD-BRL'
        url = f"https://economia.awesomeapi.com.br/last/{data}";
        dict = requests.get(url, data)
        dict = dict.json()

        for i, j in dict.items():
            dolar_low = j['low']
            dolar_high = j['high']
            dolar_ask = j['ask']
            print ('Dólar mais alto:', dolar_high)
            print ('Dólar mais baixo:', dolar_low)
            print ('Dólar Agora:', dolar_ask)

    except Exception as e:
        print("Erro no sendMessage:", e)

    return dict


dict = DolarReal()