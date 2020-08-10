count = 0
fname = input("Enter file name: ")
fh = open(fname)
OfThem = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    atpos = line.find(':')
    lastL = float(line[atpos+1 : -1])
    OfThem = OfThem + lastL

print('Average spam confidence:',OfThem / count)
