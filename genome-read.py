

def readFastq(fileName):
  sequences = []
  qualities = []
  with open(fileName) as f:
    while True:
      f.readline()
      seq = f.readline().rstrip()
      f.readline()
      qual = f.readline().rstrip()
      if len(seq) == 0:
        break
      sequences.append(seq)
      qualities.append(qual)
  return sequences, qualities

def readGenome(filename):
  genome = ""
  with open(filename) as f:
    for line in f:
      if not line[0] == '>':
        genome += line.rstrip()
  
  return genome

def phred33ToQ(qual):
  return ord(qual) - 33

def createHist(qualities):
  hist = [0] * 50
  for qual in qualities:
    for phred in qual:
      q = phred33ToQ(phred)
      hist[q] += 1
  return hist


# genome = readGenome('lambda_virus.fa')
# print(genome[:100])
# print(len(genome))

seqs, quals = readFastq('SRR835775_1.first1000.fastq')
print(seqs[:3])
print(quals[:3])
h = createHist(quals)
print(h)

# %matplotlib inline
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
plt.show()