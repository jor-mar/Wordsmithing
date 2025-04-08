import qrcode
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# URL you want the QR code to link to
url = ''
box_size = 10 # in pixels
saveImg = False
output_size = 1000

# logo on QR code
logo_path = 'logo.png'
logo_prop = 3 # 1/logo_prop = proportion of the QR code that the logo covers, cannot be 0
logo_opacity = 255

# border?
border_prop = 0.0175 # what percentage of the logo's size is the border?, 0.0175
border_size = 0 # set to 0 if using border_prop, otherwise set border_prop to 0
borderOpacity = 255 // 2 + 30 # 0 (transparent) to 255 (opaque)
# borderColor =
borderRed = 169
borderGreen = 169
borderBlue = 169

# Define SMS link
phone_number = "+1"
message = "Prebuilt message"
url = f"sms:{phone_number}?body={message.replace(' ', '%20')}"

# Define email link
# email_address = "aimlclub.pcc@gmail.com"
# subject = "Mailing List Entry"
# message = "I would like to receive email updates about the AI Convention on April 30th, 2025. I will not receive emails beyond that date."
# url = f"mailto:{email_address}?subject={subject.replace(' ', '%20')}&body={message}"

# Create a QR code
qr = qrcode.QRCode(
    version=1,  # Larger QR codes are needed for more error correction
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest error correction level
    box_size=box_size,
    border=0,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
qr_img = qr.make_image(fill='black', back_color='white')
qr_img = qr_img.resize((output_size, output_size), Image.LANCZOS)

# Load the logo image (ensure it's in the same directory as the script)
logo = Image.open(logo_path)

# Resize the logo to cover a smaller portion of the QR code
if logo_prop > 0:
    logo_size = qr_img.size[0] // logo_prop  # 1/denominator is size of logo proportional to qr code
else:
    logo_size = 1
logo = logo.resize((logo_size, logo_size))

# Ensure the logo has an alpha channel (transparency) and convert if necessary
if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

logo.putalpha(logo_opacity)

# Create a grey border around the logo
border_size = border_size + round(border_prop * (qr_img.size[0] // logo_prop))  # Thickness of the border
bordered_logo = Image.new('RGBA', (logo_size + 2 * border_size, logo_size + 2 * border_size), (borderRed, borderGreen, borderBlue, borderOpacity))  # Grey color
bordered_logo.paste(logo, (border_size, border_size))  # Paste the logo onto the grey background

# Separate the logo with the border into RGB and Alpha channels
logo_rgb = bordered_logo.convert('RGB')
logo_alpha = bordered_logo.split()[3]

# Convert QR image to RGBA mode to ensure it can handle transparency
qr_img = qr_img.convert('RGBA')

# Calculate the position to place the logo with the grey border in the middle of the QR code
qr_width, qr_height = qr_img.size
logo_x = (qr_width - bordered_logo.size[0]) // 2
logo_y = (qr_height - bordered_logo.size[1]) // 2

# Paste the logo with the grey border onto the QR code using the alpha channel as a mask
qr_img.paste(logo_rgb, (logo_x, logo_y), mask=logo_alpha)

# Display the QR code with the logo in the middle using matplotlib
plt.imshow(qr_img)
plt.axis('off')  # Hide axes
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Crop tight
plt.show()

if saveImg:
    qr_img.save('qr_code.png')