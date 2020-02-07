def DNA_strand(dna):

    changedna = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return ''.join(changedna[x] for x in dna)

print (DNA_strand("ATTGC"))