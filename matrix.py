# Define the planets and their relationships
planets = [
    ["PLANET NUMBER", "PLANET NAME", "FRIEND NUMBERS", "NEUTRAL NUMBERS", "ENEMY NUMBERS"],
    [1, "SUN", [1, 2, 4, 7], [3, 5, 6, 9], [8]],
    [2, "MOON", [1, 2, 3, 4, 7], [8, 9], [5, 6]],
    [3, "JUPITER", [1, 2, 3, 9], [6, 5, 8], [4, 7]],
    [4, "RAHU", [1, 2, 7], [5, 6, 9], [3, 4, 8]],
    [5, "MERCURY", [1, 3, 4, 5, 6, 8], [7, 9], [2]],
    [6, "VENUS", [5, 8, 9], [1, 3, 4, 6, 7], [2]],
    [7, "KETU", [1, 2], [4, 5, 7], [3, 6, 8, 9]],
    [8, "SATURN", [3, 5], [2, 6], [1, 4, 7, 8, 9]],
    [9, "MARS", [2, 3], [1, 5, 6, 9], [4, 7, 8]]
]

# Print the matrix
for row in planets:
    print(row)