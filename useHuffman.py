from os import system
from huffman import HuffmanCoding
import PyPDF2
import sys
from qrgenerator import qrgenerate
choice=int(input("\nDo you want to compress 1.PDF File or 2.Text File\nEnter Your Choice\n"))
if(choice==1):
    samplet=open("sample.pdf","rb")
    output_file = open("sample.txt", "w")
    pdfReader = PyPDF2.PdfFileReader(samplet)
    numOfPages = pdfReader.numPages
    for i in range(numOfPages):
        page = pdfReader.getPage(i)
        text = page.extractText()
        output_file.write(text)
    output_file.close()
    samplet.close()
    # samplet.save("sample.txt")
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
        if(chq=="Y" or chq=="y"):
            qr.start_1()
    elif ch==2:
        hw=HuffmanCoding("sample.txt")
        print(opath)
        hw.compress()
        decom_path=hw.decompress("sample.bin")
        print("Decompressed file path "+decom_path)
else:
    print("Please Select Your Choice\n1.Compression\n2.Decompression")
    opath=""
    ch=int(input())
    if(ch==1):
        path = "sample.pdf"
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
        
