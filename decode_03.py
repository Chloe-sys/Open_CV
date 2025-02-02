import pyzxing

reader = pyzxing.BarCodeReader()
barcode = reader.decode('03.jpg')

if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No barcode found.")