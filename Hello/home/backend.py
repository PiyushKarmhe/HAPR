import pandas as pd
# l=[]
# csvFile = pd.read_csv(r'Hello\\static\\file\\Sev Final.csv')
# for i in csvFile['Symptom']:
#     i=i.replace("_","  ")
#     i=i.title()
#     l.append(i)
# print(l)
def disease_predict(l_input):
    # Creating a list of all diseases
    l_all_disease = []
    df = pd.read_csv(r'static//file//Only_Single Final.csv')
    y = df["Disease"]
    for j in y:
        l_all_disease = l_all_disease + [j]

    #l_input = ["chills", "fatigue", "high_fever"]  # User-Defined input

    # Creating a list of predicted diseases
    ds = pd.read_csv(r'static//file//Only_Single Final.csv', index_col="Disease")
    lf = []
    for a in l_all_disease:
        x = ds.loc[a]
        count = 0
        for b in x:
            if type(b) == str:
                if b.strip() in l_input:
                    count = count + 1
        if count == len(l_input):  # if count >= 3: (Probabilities wil be wrong so not calculated)
            lf = lf + [a]

    l_disease = lf
    print(l_disease)

    df = pd.read_csv(r'static//file//Sev Final.csv', index_col="Symptom")

    # Sum of the severity values of the input
    l2 = []
    n = 0
    n1 = len(l_input)
    while n != n1:
        x = df.loc[l_input[n]]
        n += 1
        l2 = l2 + [x["weight"]]
    print(l2)
    total = 0
    for i in l2:
        total = total + i

    print(f"The sum of severity values of the input is {total}")  # Sum of severity values of input

    # List of sum of total severity values of the diseases predicted

    ds = pd.read_csv(r'static//file//Only_Single Final.csv', index_col="Disease")
    lf = []
    for a in l_disease:
        x = ds.loc[a]
        ls = []
        for b in x:
            if type(b) == str:
                ls = ls + [b.strip()]
        lf = lf + [ls]

    #print(lf)  # The list made of list of symptoms of the diseases

    dt = pd.read_csv(r'static//file//Sev Final.csv', index_col="Symptom")

    l3 = []

    for b in lf:
        l4 = []
        n = 0
        n1 = len(b)
        while n != n1:
            x = dt.loc[b[n]]
            n += 1
            l4 = l4 + [x["weight"]]
        #print(l4)
        s = 0
        for k in l4:
            s = s + k
        l3 = l3 + [s]

    #print(l3)  # List of sum of severity values oof the disease

    dict1 = {}
    num = 0
    num1 = len(l3)
    while num != num1:
        dict1.update({l_disease[num]: l3[num]})
        num = num + 1
    print(dict1)  # Dictionary of the disease name and the sum of symptom severity as the value

    # Calculating the probabilities of disease occurrence
    dict2 = {}
    p = 0
    p1 = len(l_disease)
    while p != p1:
        dict2.update({l_disease[p]: (total / (dict1[l_disease[p]]))})
        p = p + 1

    print(dict2)  # Dictionary of the disease name and probability as the value
#disease_predict()