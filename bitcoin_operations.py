#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install bitcoin


# In[ ]:


pip install bitcoinlib


# In[ ]:


#Generate a BITCOIN PRIVATE KEY
from bitcoin import *

my_private_key = random_key()

print(my_private_key)


# In[ ]:


#Generate a BITCOIN PUBLIC KEY
from bitcoin import *

my_private_key = random_key()
my_public_key = privtopub(my_private_key)

print(my_public_key)


# In[ ]:


#Generate a BITCOIN WALLET
from bitcoinlib.wallets import HDWallet

w = HDWallet.create('Wallet1')
key1 = w.get_key()

key1.address


# In[ ]:


#Gather Wallet Info
w.scan()
w.info()


# In[ ]:


#Segregated Witness Wallet
from bitcoinlib.wallets import HDWallet

w = HDWallet.create('wallet_segwit_p2wpkh', witness_type='segwit')
w.get_key().address


# In[ ]:


#Create a BITCOIN RECIEVING ADDRESS(with priv and pub key)
from bitcoin import *

my_private_key = random_key()
my_public_key = privtopub(my_private_key)
my_bitcoin_address = pubtoaddr(my_public_key)

print('PRIV KEY: ' + my_private_key)
print('PUB KEY: ' + my_public_key)
print('ADDRESS: ' + my_bitcoin_address)


# In[ ]:


#Create a BITCOIN MULTI SIGNATURE ADDRESS
from bitcoin import *

my_private_key1 = random_key()
print('Private Key 1: ' + my_private_key1)

my_public_key1 = privtopub(my_private_key1)
print('Public Key 1: ' + my_public_key1)

my_private_key2 = random_key()
print('Private Key 2: ' + my_private_key2)

my_public_key2 = privtopub(my_private_key2)
print('Public Key 2: '  + my_public_key2)

my_private_key3 = random_key()
print('Private Key 3: ' + my_private_key3)

my_public_key3 = privtopub(my_private_key3)
print('Public Key 3: ' + my_public_key3)

my_multi_sig = mk_multisig_script(my_private_key1, my_private_key2, my_private_key3, 2,3)
my_multi_address = scriptaddr(my_multi_sig)
print('Multi-Address: ' + my_multi_address)


# In[ ]:


#Generate a BITCOIN TRANSACTION(if done correctly output will be transaction ID)
transaction = w.send_to('*RECIEVING ADDRESS*', 100000)


# In[ ]:


#Bitcoin Library Commands
### Listing of main commands:

#privkey_to_pubkey : (privkey) -> pubkey
#privtopub : (privkey) -> pubkey
#pubkey_to_address : (pubkey) -> address
#pubtoaddr : (pubkey) -> address
#privkey_to_address : (privkey) -> address
#privtoaddr : (privkey) -> address
#add : (key1, key2) -> key1 + key2 (works on privkeys or pubkeys)
#multiply : (pubkey, privkey) -> returns pubkey * privkey
#ecdsa_sign : (message, privkey) -> sig
#ecdsa_verify : (message, sig, pubkey) -> True/False
#ecdsa_recover : (message, sig) -> pubkey
#random_key : () -> privkey
#random_electrum_seed : () -> electrum seed
#electrum_stretch : (seed) -> secret exponent
#electrum_privkey : (seed or secret exponent, i, type) -> privkey
#electrum_mpk : (seed or secret exponent) -> master public key
#electrum_pubkey : (seed or secexp or mpk) -> pubkey
#bip32_master_key : (seed) -> bip32 master key
#bip32_ckd : (private or public bip32 key, i) -> child key
#bip32_privtopub : (private bip32 key) -> public bip32 key
#bip32_extract_key : (private or public bip32_key) -> privkey or pubkey
#deserialize : (hex or bin transaction) -> JSON tx
#serialize : (JSON tx) -> hex or bin tx
#mktx : (inputs, outputs) -> tx
#mksend : (inputs, outputs, change_addr, fee) -> tx
#sign : (tx, i, privkey) -> tx with index i signed with privkey
#multisign : (tx, i, script, privkey) -> signature
#apply_multisignatures: (tx, i, script, sigs) -> tx with index i signed with sigs
#scriptaddr : (script) -> P2SH address
#mk_multisig_script : (pubkeys, k, n) -> k-of-n multisig script from pubkeys
#verify_tx_input : (tx, i, script, sig, pub) -> True/False
#tx_hash : (hex or bin tx) -> hash
#history : (address1, address2, etc) -> outputs to those addresses
#unspent : (address1, address2, etc) -> unspent outputs to those addresses
#fetchtx : (txash) -> tx if present
#pushtx : (hex or bin tx) -> tries to push to blockchain.info/pushtx
#access : (json list/object, prop) -> desired property of that json object
#multiaccess : (json list, prop) -> like access, but mapped across each list element
#slice : (json list, start, end) -> given slice of the list
#count : (json list) -> number of elements
#sum : (json list) -> sum of all values

