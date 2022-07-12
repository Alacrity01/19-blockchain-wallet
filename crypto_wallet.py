###################################### Cryptocurrency Wallet (crypto_wallet.py) ###################################### 
# This file contains the Ethereum transaction functions to be imported into `fintech_finder.py`
###################################################################################################################### 

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from mnemonic import Mnemonic
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

################################################################################
# Wallet functionality

def generate_account(): # Create a digital wallet and Ethereum account from a mnemonic seed phrase.
    mnemonic = os.getenv("MNEMONIC") # Fetch mnemonic from environment variable.
    
    if mnemonic == None: # Create a mnemonic if one does not exist
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)

        with open(".env", "w") as text_file: # Save mnemonic to .env 
            text_file.write(f"MNEMONIC = '{mnemonic}'")
            text_file.close()

    wallet = Wallet(mnemonic) # Create Wallet Object
    private, public = wallet.derive_account("eth") # Derive Ethereum Private Key    
    account = Account.privateKeyToAccount(private) # Convert private key into an Ethereum account

    return account

def get_balance(w3, address): # Using an Ethereum account address access the balance of Ether    
    wei_balance = w3.eth.get_balance(address) # Get balance of address in Wei
    ether = w3.fromWei(wei_balance, "ether") # Convert Wei value to ether

    return ether # Return the value in ether


def send_transaction(w3, account, to, wage): # Send an authorized transaction to the Ganache blockchain.
    
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy) # Set gas price strategy


    value = w3.toWei(wage, "ether") # Convert eth amount to Wei


    gasEstimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value}) # Calculate gas estimate

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 0,
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    signed_tx = account.signTransaction(raw_tx) # Sign the raw transaction with ethereum account


    return w3.eth.sendRawTransaction(signed_tx.rawTransaction) # Send the signed transactions
