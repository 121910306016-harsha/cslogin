from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

blockNumber = web3.eth.block_number
print(blockNumber)

account_1= "0xBfE1F82E48d9545717e79B702df9586beC953b3d"
account_2= "0xf859a489934d7e316B2277ab39efAe9d8E68986A"
private_key="3df42c6f7ecb47f765b3e4face605a6778ef4a169765518126fc0823e7de4e62"

#send crytp currency from actn1 to acunt2

##STEPS
#get the nonce  
nonce = web3.eth.getTransactionCount(account_1)
#build transaction
n= 20
ts= {
    'nonce': nonce, #nonce prevents u from sending transaction twice on ethereum 
    'to': account_2,
    'value': web3.toWei(n,'ether'),
    'gas': 2000000, #units of gas but not ethereum #compensation/cryptocurrency for miners on blockchain network
    'gasPrice': web3.toWei('50', 'gwei')
}
#sign transaction
signed_ts = web3.eth.account.signTransaction(ts,private_key)
#send transaction
ts_hash = web3.eth.sendRawTransaction(signed_ts.rawTransaction)
#get transaction hash
print(ts_hash) #binary format
print(web3.toHex(ts_hash)) #Hex Format
