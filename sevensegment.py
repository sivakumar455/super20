print("Seven Segment Converter")

rows=3
cols=3
with open('input.txt') as f:
   data = []
   for i in range(0, rows):
      data.append(list(map(str, f.readline().split()[:cols])))
print (data)


