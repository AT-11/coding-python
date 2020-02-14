def DNA_strand(dna):
    value = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ""
    for val in dna:
        result += value.get(val)
    return result


if __name__ == '__main__':
    print(DNA_strand("ACGT"))
