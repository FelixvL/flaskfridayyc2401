import requests

def btcpricef():
    btc = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    btc_json = btc.json()
    btc_price = btc_json["bpi"]["USD"]["rate"]
    return str("BTC price: $" + btc_price)