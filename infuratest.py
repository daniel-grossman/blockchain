#this is a basic script that gets a wallet's tx count and value using Infura
#eventually will add Etherscan API support for more detailed info

#import the Web3 module etc.
import web3
import requests

#API keys
infura = "ENTER-INFURA-API-KEY"

#create Web3 object using Infura & test connection
w3 = web3.Web3(web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura}"))
print("Am I connected to a node?", w3.isConnected())

#set up exchange rates
exch_response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
exch_rate = float(exch_response.json()["data"]["amount"])

#print a wallet's tx_count and balance
def print_txCount_balance(wallet_address):
    tx_count = w3.eth.get_transaction_count(wallet_address)
    balance_ether = float(w3.fromWei(w3.eth.get_balance(wallet_address), 'ether'))
    balance_usd = "${:,.2f}".format(balance_ether * exch_rate)
    format_eth = "Ξ{:,.2f}".format(balance_ether)
    format_tx = "Txs: {:,}".format(tx_count)
    print(wallet_address + "\n", format_tx + "\n", format_eth + "\n", balance_usd)

#print multiple wallets' txCnt and balance
def print_multiple():
    wallet_list = []
    while True:
        wallet_address = str(input("Input wallet address: "))
        if wallet_address == "":
            break
        wallet_list.append(wallet_address)
    for i in wallet_list:
        print_txCount_balance(i)

print_multiple()
