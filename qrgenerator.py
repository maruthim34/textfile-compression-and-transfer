import pyqrcode
import png
from PIL import Image
from pyqrcode import QRCode
import requests
class qrgenerate:
	def start_1(str):
		filepath=("sample.bin")
		filepath=filepath.strip()
		if filepath.startswith("'") and filepath.endswith("'"):
				filepath = filepath[1:len(filepath)-1]
		filename=input('Enter file name\n')
		files= {
			'file':(filename,open(filepath,'rb')),
		}
		url='https://api.anonfiles.com/upload'
		response=requests.post(url,files=files)
		data=response.json()
		print(data['data']['file']['url']['short'])
		s=data['data']['file']['url']['short']
		url=pyqrcode.create(s)
		url.png('myqr.png',scale=6)
		im=Image.open(r"C:\Users\marut\Downloads\mini_project\huffman-coding-master\myqr.png")
		im.show()
	
