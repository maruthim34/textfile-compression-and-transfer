from os import system
from huffman import HuffmanCoding
import sys
//from huffman_dec import Huffman_decompress
from qrgenerator import qrgenerate
print("Please Select Your Choice\n1.Compression\n2.Decompression")
opath=""
ch=int(input())
if(ch==1):
    path = "sample.txt"
    h = HuffmanCoding(path)
    output_path = h.compress()
    opath=output_path
    print("Compressed")
    print("Compressed file path: " + output_path)
    print("Do you want to transfer compressed file via QR CODE?\tY/N")
    chq=input()
    qr=qrgenerate()
    if(chq=="Y"):
        qr.start_1()
elif ch==2:
    hw=HuffmanCoding("sample.txt")
    print(opath)
    hw.compress()
    decom_path=hw.decompress("sample.bin")
    print("Decompressed file path "+decom_path)
    
