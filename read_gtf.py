# reads ensGene file and create a list of list, containing following information
# chromosome, gene id, type(transcript, cds, exon, intron, etc), starting, ending

def read_gtf(input_gtf):
    storage = []
    transId = ""
    with open(input_gtf) as gtf:
        temp = []
        valid = True
        for info in gtf:
            info = info.split()
            chromosome = info[0]
#           if chromosome == "chr10":
            tp = info[2]
            start = int(info[3])
            end = int(info[4])
            rev = info[6]
            transcriptId = info[11][1:len(info[11]) - 2]       

            #start of new transcript; cleanse global data
            if transId != transcriptId:
                transId = transcriptId
                temp = []
                valid = True

            #all with the same transcript id
            if valid:
                if rev == "+":
                    if tp == "CDS":
                        # creates a dictionary to improve performance
                        data = {}
                        data["chromosome"] = chromosome
                        data["transcriptId"] = transcriptId
                        data["start"] = start
                        data["end"] = end
                        data["rev"] = rev
                        temp.append(data)
                    #check if start of first codon is the same as the start codon
                    elif tp == "start_codon":
                        if len(temp) < 1 or start != temp[0]["start"]:
                            valid = False
                    #check if start of last CDS + 1 is the same as the start of the stop codon
                    elif tp == "stop_codon":
                        if len(temp) < 1 or start != temp[-1]["end"] + 1:
                            valid = False
                        else:
                            storage += temp
                else:
    #                 if transcriptId == "XM_006495550.3":
    #                     print(info)
                    #case for "-"
                    if tp == "CDS":
                        data = {}
                        data["chromosome"] = chromosome
                        data["transcriptId"] = transcriptId
                        data["start"] = start
                        data["end"] = end
                        data["rev"] = rev
                        temp.append(data)
                    elif tp == "start_codon":
                        if len(temp) < 1 or end != temp[-1]["end"]:
                            valid = False
                    elif tp =="stop_codon":
                        if len(temp) < 1 or end != temp[0]["start"] - 1:
                            valid = False
                        else:
                            storage += temp
        return storage

#test:
input_gtf = "/home/raymond/Downloads/mm10.ncbiRefSeq.gtf"
result = read_gtf(input_gtf)                        

print(result[0])
print(result[0:20])
