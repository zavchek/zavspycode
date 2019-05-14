#! python

"""
Create an API call to collect data from the marvel character database with input from user
"""

#functions to be imported for this call
import requests
import argparse
import time
import hashlib

#Global varibles and constants
XAVIER = 'http://gateway.marvel.com/v1/public'

#Create a hashing function using MD5
def hashbuilder(curtime, privkey, pubkey):
    return hashlib.md5((curtime + privkey + pubkey).encode('utf-8')).hexdigest()

#Create a character lookup from marvel database
def marvelcharcall(curtime, hashkey, pubkey, charkey):
    marvelurl = XAVIER + '/characters'
    marvelurl += '?name='+charkey+'&ts='+curtime+'&apikey='+pubkey+'&hash='+hashkey
    hulk = requests.get(marvelurl)
    return hulk.json()

def main():
    with open('marvel.pub') as pubkeyfile:
        beast = pubkeyfile.read()

    with open('marvel.priv') as privkeyfile:
        storm = privkeyfile.read()
        curtime = (str(int(time.time())))

        charlook = input('What character are we looking up? ')
        hashy = hashbuilder(curtime, storm, beast)
        print(marvelcharcall(curtime, hashy, beast, charlook))

main()




