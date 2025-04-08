import qrcode
import matplotlib.pyplot as plt

# Define the SMS link
phone_number = "+1234567890"
message = "Hey, how are you?"
sms_link = f"sms:{phone_number}?body={message.replace(' ', '%20')}"

# Generate QR Code
qr = qrcode.make(sms_link)

# Display QR Code
plt.figure(figsize=(5, 5))
plt.imshow(qr, cmap="gray")
plt.axis("off")
plt.show()