# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')


import hashlib# what's it?

import json

from time import time

class Blockchain(object):
	"""docstring for Blockchain"""
	def __init__(self):
		#super(Blockchain, self).__init__()
		self.chain = []
		self.current_transactions = []

		#Create the genesis block
		self.new_block(previous_hash = 1,proof = 100)


	
	def new_block(self):
		'''
		#创建一个新的区块，并将其加入到链中
		:param proof:<int> The proof given by the Proof of Work algorithm
		:param previous_hash:(Optional) <str>Hash of previous Block
		:return:<dict New Block>


		'''

		block = {

		    'index': len(self.chain)+1,
		    'timestamp':time(),
		    'transactions':self.current_transactions,
		    'proof':proof,
		    'previous_hash':previous_hash or self.hash(self.chain[-1]),


		}

		self.current_transactions=[]

		self.chain.append(block)

		return block

	
	def new_transaction(self):

		#将新的交易加入交易列表
		'''
		生成新的交易信息，信息将加入下一个待挖的区块中
		：param sender:<str>Address of the Sender
		: param recipient:<str>Address of the Recipient
		: param amount:<int>Amount
		: return:<int>The index of the Block that will hold
		   this transaction
		'''
		self.current_transactions.append({

			'sender' : sender,
			'recipient':recipient,
			'amount':amount,

			})
		return self.last_block['index']+1

	@staticmethod

	def hash(block):
		#Hashes a Block
		'''
        bolck's SHA-256 hash
        "para block:<dict>Block
        :return:<str>
		'''
		#We must make sure that the Dictionary is Ordered,
		#or we'll have sistent hashes
		block_string = json.dumps(block,sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()


	@property

	def last_block(self):
		#Returns the last Block in the chain
		return self.chain[-1]
		pass
block = {
	'index' : 1,#索引
	'timestamp':1506057155.900785,#时间戳
	'transactions':[
	    {
	        'sender':"8527147fe11f5426f9dd545de4b27ee00",
	        'recipient' : "a77f5cdfa2934df3954a5c7c7da5df1f",
	        'amount':5,

	    }
	],#交易列表

	'proof':324984774000,#工作量证明
	'previous_hash':"2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e732242113425"
     #前区块Hash值

}



