import qrcode

data = input("Enter the text or URL for the QR code: ").strip()
img_name = 'some_file'

while True:
    img_name = input("Enter the filename (without file extension): ")

    if img_name.strip():
        break

qr = qrcode.QRCode(border=4, box_size=10)
qr.add_data(data)
qr.make(fit=True)

while True:
    try:
        fill_color = input('Enter a color for the QR code: ')
        img = qr.make_image(fill_color=fill_color)
        full_img_name = img_name + '.png'
        img.save(img_name + '.png')
        print(f"QR code saved as {full_img_name}")

        break
    except ValueError:
        print("Invalid color")
