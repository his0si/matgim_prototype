import qrcode

url = "https://matgim-prototype.vercel.app/"

img = qrcode.make(url)
img.save("qr.png")

print("saved qr.png")
