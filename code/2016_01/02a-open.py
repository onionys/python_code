vals = []

with open('oil2.csv',encoding='utf8') as f:
    head = f.readline()
    for line in f:
        val = float(line.split(',')[1].strip())
        vals.append(val)

print("95oil:",sum(vals)/len(vals))





## -------------------------- ##
a = []
with open('oil2.csv',encoding='utf8') as f:
    field = 4
    head = f.readline().split(',')[field]
    a = [float(line.split(',')[field]) for line in f]
print(head, sum(a)/len(a))
