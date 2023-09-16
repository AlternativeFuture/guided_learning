sentence = '''Beaches are cool places to visit in spring however the Mackinaw Bridge is near. 
              Most people visit Mackinaw later since the island is a cool place to explore.'''

d = {}

for char in sentence:
    d[char] = d.get(char, 0) + 1

min_value = min(d, key=d.get)

print(f'Dictionary of character counts: {d}')
print(f'Key with the minimum value: {min_value}')
