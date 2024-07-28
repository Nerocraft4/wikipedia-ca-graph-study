### Imports
import pandas as pd
import glob
step = int(input("processing step"))

if step <= 0:
    ### Step 1.1
    #preproc sql file
    lines = []
    with open(file="cawiki-20240501-pagelinks.sql", mode="r", encoding='utf-8') as f:
        for line in f:
            if line[:6] == "INSERT":
                for temp in line[32:-3].split("),("):
                        lines.append(temp.split(",")[:5])
    print("1.1 done")
    ### Step 1.2
    #chunkify file into different csvs, write to mem
    for i in range(6):
        df1 = pd.DataFrame(lines[10000000*i:10000000*(i+1)]) #total 65674867
        df1.to_csv("cawiki-pagelinks"+str(i)+".csv", index=False, header=None)
    df1 = pd.DataFrame(lines[60000000:])
    df1.to_csv("cawiki-pagelinks7.csv", index=False, header=None)
    print("1.2 done")

elif step<=1:
    ### Step 1.3
    # concat all files into dfa dataframe
    csv_files = glob.glob('*.{}'.format('csv'))
    df1 = pd.concat([pd.read_csv(csv_files[0], header=None),pd.read_csv(csv_files[1], header=None)])
    df2 = pd.concat([pd.read_csv(csv_files[2], header=None),pd.read_csv(csv_files[3], header=None)])
    df3 = pd.concat([pd.read_csv(csv_files[4], header=None),pd.read_csv(csv_files[5], header=None),pd.read_csv(csv_files[6], header=None)])
    dfa = pd.concat([df1,df2,df3])
    print("1.3 done")
    ### Step 1.4
    #Filter out dfa
    dfa = dfa[dfa[1]==0] #65M -> 60M rows
    dfa = dfa[dfa[3]==0] #60,8M -> 9,2M rows
    print("1.4 done")

elif step<=2:
    ### Step 2.1
    #preproc sql file from aux table
    lines = []
    with open(file="cawiki-20240501-page.sql", mode="r", encoding='utf-8') as f:
        lines = f.readlines()
    lines = lines[50:-12]
    print("2.1 done")

    ### Step 2.2
    #clean that up a bit and write aux table to memory
    rows = []
    for line in lines:
        line = line[26:]
        values = line.split("),(")
        values[0] = values[0][1:]
        values[-1] = values[-1][:-3]
        for value in values:
            rows.append(value.split(",")[:6])
    page_df = pd.DataFrame(rows)[[0,1,2]]
    page_df = page_df[page_df[1]=="0"][[0,2]] #namespace 0, drop 1
    page_df.rename({0:"id",2:"name"},axis=1,inplace=True)
    page_df.to_csv("cawiki-page.csv", index=False, header=None)
    print("2.2 done")

elif step<=3:
    ### Step 2.3
    #apply transformations to dfa and write it to memory
    repdic = page_df.set_index('id').T.to_dict('list')
    dfa[5] = dfa[0].apply(lambda x: repdic[str(x)][0][1:-1] if str(x) in repdic.keys() else "ERRmissing")
    dfa = dfa[[5,2]]
    dfa.rename({5:"from",2:"to"},axis=1,inplace=True)
    dfa["to"] = dfa["to"].apply(lambda x: x[1:-1])
    dfa.to_csv("cawiki-pagelinks.csv", index=False, header=None)
    print("2.3 done")