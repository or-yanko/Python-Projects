import qrcode
import sys
try:
    data = sys.argv[1]
    filename = sys.argv[2]
except:
    print("enter like -> python qr-generator.py https://www.google.com ./qr-file.png")
    exit()
img = qrcode.make(data)
img.save(filename)
