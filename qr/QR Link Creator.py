import qrcode
import matplotlib.pyplot as plt

# Define the link
sms_link = ""

# Generate QR Code
qr = qrcode.make(sms_link)

# Display QR Code
plt.figure(figsize=(5, 5))
plt.imshow(qr, cmap="gray")
plt.axis("off")
plt.show()