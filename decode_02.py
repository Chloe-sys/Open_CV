import pyzxing

# Initialize ZXing reader
reader = pyzxing.BarCodeReader()

# Decode the image
barcode = reader.decode('02.jpg')

if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No Data Matrix code found.")