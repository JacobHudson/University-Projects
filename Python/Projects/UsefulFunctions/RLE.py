def rle_encode(image):
    encoded = []
    for row in image:
        current_value = row[0]
        count = 0
        for pixel in row:
            if pixel == current_value:
                count += 1
            else:
                encoded.append((current_value, count))
                current_value = pixel
                count = 1
        encoded.append((current_value, count))  # Append the last run
    return encoded

image = [
    [1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
]

compressed = rle_encode(image)
print(compressed)