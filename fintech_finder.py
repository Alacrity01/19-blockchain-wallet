# Cryptocurrency Wallet

################################################################################
# For this Challenge, you will assume the perspective of a Fintech Finder
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a Fintech Finder candidate for their work.

# * Digitally sign a transaction that pays a Fintech Finder candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to the Transactions
# section of Ganache to review the blockchain transaction details. To confirm that 
# you have successfully created the transaction, you will save screenshots to the 
# README.md file of your GitHub repository for this Challenge assignment.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from crypto_wallet import generate_account, get_balance, send_transaction

def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")
############ Step 1: Fintech Finder Candidate Information ######################




# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


######################### Streamlit Code #######################################

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")


st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether") # Streamlit Sidebar Code - Start

account = generate_account() #  Call the `generate_account` function and save it as the variable `account`

st.sidebar.write(account.address) # Write the client's Ethereum account address to the sidebar

st.sidebar.write(get_balance(w3, account.address)) # Call `get_balance` function and write the returned ether balance to the sidebar

person = st.sidebar.selectbox('Select a Person', people) # Create a select box to chose a FinTech Hire candidate

hours = st.sidebar.number_input("Number of Hours") # Create a input field to record the number of hours the candidate worked

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

candidate = candidate_database[person][0] # Identify the FinTech Hire candidate

st.sidebar.write(candidate) # Write the Fintech Finder candidate's name to the sidebar

hourly_rate = candidate_database[person][3] # Identify the FinTech Finder candidate's hourly rate

st.sidebar.write(hourly_rate) # Write the inTech Finder candidate's hourly rate to the sidebar

candidate_address = candidate_database[person][1] # Identify the FinTech Finder candidate's Ethereum Address

st.sidebar.write(candidate_address) # Write the FinTech Finder candidate's Ethereum Address to the sidebar

st.sidebar.markdown("## Total Wage in Ether") # Write the Fintech Finder candidate's name to the sidebar


############## Step 2: Sign and Execute a Payment Transaction ##################

wage = candidate_database[person][3] * hours # Calculate total `wage`
st.sidebar.write(wage) # Write the `wage` calculation to the Streamlit sidebar

if st.sidebar.button("Send Transaction"):
    transaction_hash = send_transaction(w3, account, candidate_address, wage) # Call the `send_transaction` function, save as variable `transaction_hash`

    st.sidebar.markdown("#### Validated Transaction Hash") # Markdown for the transaction hash

    st.sidebar.write(transaction_hash) # Write the returned transaction hash to the screen

    st.balloons() # Celebrate successful payment

get_people(w3) # Writes FinTech Finder candidates to the Streamlit page


######################## Step 3: Inspect the Transaction #######################
# - Send a test transaction by using the application’s web interface, 
# - Look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `fintech_finder.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# To test streamlit application locally, start Ganache app, then run terminal commands:
    # conda activate localstreamlitenv
    # streamlit run fintech_finder.py

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.
    
# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
    # * Take a screenshot of the address, balance, and transaction (TX) count.
    # Save this screenshot to the README.md file of your GitHub repository for
    #  this Challenge assignment.
    
# 6. Navigate to the Ganache transactions tab and locate the transaction.
    # * Click the transaction and take a screenshot of it.
    # Save this screenshot to the README.md file of your GitHub repository for
    #  this Challenge assignment.