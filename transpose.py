from pandas import DataFrame as df
readf = open("SP-HECO_sys.tex", 'r')

lines = readf.readlines()
startnow = False
endnow = False
rows = []

for line in lines:
    if line.startswith("\\begin{tabular}") == True:
        startnow = True
        continue
    if line.startswith("\\end{tabular}") == True:
        endnow= True
        startnow = False
        continue
    if line.startswith("%") == True:
        continue

    if startnow == True:
        splitting = line.split("&") 
        split_and_strip = []
        for split_s in splitting:
            split_s1 = split_s.replace("\\\\", "")
#            split_s2 = spli
            split_and_strip.append(split_s1.strip())
        rows.append(split_and_strip)

    if endnow == True:
        break


## Build the first column; since its a combination of two rows
firstrow = []
for r0, r1 in zip(rows[0], rows[1]):
    r1_s = r1.replace("\\\\", "")
    r0_s = r0.replace("\\\\", "")
    
    firstrow.append(r0_s.strip()+" "+r1_s.strip())



x_df = df({firstrow[0]: firstrow[1:len(firstrow)], 
           rows[2][0]: rows[2][1:len(rows[2])],
           rows[3][0]: rows[3][1:len(rows[3])],
           rows[4][0]: rows[4][1:len(rows[4])],
           # rows[5][0]: rows[5][1:len(rows[5])],
           # rows[6][0]: rows[6][1:len(rows[6])],
           # rows[7][0]: rows[7][1:len(rows[7])],
           })
