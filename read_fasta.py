# reads fasta file to create a dictionary of key = chromosome name and value = sequenc

def read_fasta(input_fasta):
    fas = {}
    with open(input_fasta) as fasta:
        id = ""
        data = []
        chrm = ""
        for each in fasta:
            if each.startswith(">"):
                if chrm == "":
                    chrm = each[1:].strip()
                    continue
                #chromosome id
                seq = "".join(data)
                data = []
                fas[chrm] = seq
    #             if len(fas) > 0:
    #                 break
                chrm = each[1:].strip()
            else:
                data.append(each.strip())
        #last chromosome seq to be added
        fas[chrm] = "".join(data)
    return fas    

#test:        
input_fasta = "/home/raymond/Desktop/mouse_genome_mm10/mm10.fa"    
result = read_fasta(input_fasta)
print(result[list(result.keys())[0]][1000:2000])
    
for k,v in result.items():
    print(len(v))
    print(k, v[:10])
