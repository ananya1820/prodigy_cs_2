from PIL import Image

def encrypt(img, key):
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Apply a random permutation to the pixel values
            r = (r + i + j) % 256
            g = (g + i * 2 + j * 3) % 256
            b = (b + i * 3 + j * 2) % 256

            # Apply a bitwise XOR operation to the pixel values
            r = r ^ key
            g = g ^ key
            b = b ^ key

            encrypted_pixel = (r, g, b)

            pixels[i, j] = encrypted_pixel

    return img

def decrypt(img, key):
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Reverse the bitwise XOR operation
            r = r ^ key
            g = g ^ key
            b = b ^ key

            # Reverse the random permutation
            r = (r - i - j) % 256
            g = (g - i * 2 - j * 3) % 256
            b = (b - i * 3 - j * 2) % 256

            decrypted_pixel = (r, g, b)

            pixels[i, j] = decrypted_pixel

    return img

# Image path
img_path = r"idk.jpg"
encrypted_img_path = r"enxr.jpg"
decrypted_img_path = r"decr.jpg"

# Load the image
img = Image.open(img_path)

# Encrypt the image
key = 22
encrypted_img = encrypt(img, key)
encrypted_img.save(encrypted_img_path)
print("Image encrypted successfully!")

# Decrypt the image
decrypted_img = decrypt(encrypted_img, key)
decrypted_img.save(decrypted_img_path)
print("Image decrypted successfully!")