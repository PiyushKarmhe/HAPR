import pandas as pd

def disease_predict(l_input):
    l_all_disease = []
    df = pd.read_csv(r'static//file//Only_Single Final.csv')
    y = df["Disease"]
    for j in y:
        l_all_disease = l_all_disease + [j]

    #l_input = ["chills", "fatigue", "high_fever", "sweating", "obesity"]

    ds = pd.read_csv(r'static//file//Only_Single Final.csv', index_col="Disease")
    lf = []
    for a in l_all_disease:
        x = ds.loc[a]
        count = 0
        for b in x:
            if type(b) == str:
                if b.strip() in l_input:
                    count = count + 1
        if count == len(l_input):
            lf = lf + [a]

    #print(lf)
    l_disease = lf

    df = pd.read_csv(r'static//file//Sev Final.csv', index_col="Symptom")

    # Sum of the severity values of the input
    l2 = []
    n = 0
    n1 = len(l_input)
    while n != n1:
        x = df.loc[l_input[n]]
        n += 1
        l2 = l2 + [x["weight"]]
    #print(l2)
    total = 0
    for i in l2:
        total = total + i

    #print(f"The sum of severity values of the input is {total}")  # Sum of severity values of input

    # List of sum of total severity values of the diseases predicted
    if len(l_disease) == 0:
        lf = []
        for a in l_all_disease:
            x = ds.loc[a]
            count = 0
            for b in x:
                if type(b) == str:
                    if b.strip() in l_input:
                        count = count + 1
            if count >= 3:
                lf = lf + [a]

        #print(lf)
        l_disease = lf

        d1 = pd.read_csv(r'static//file//Desc Final.csv', index_col="Disease")

        lf = []
        for x in l_disease:
            y = d1.loc[x]
            ls = []
            for b in y:
                ls = ls + [b]
            lf = lf + ls

        l_desc = lf
        #print(l_desc)  # List of descriptions

        dict_1 = {}
        n1 = len(l_disease)
        n = 0
        while n != n1:
            dict_1.update({l_disease[n]: l_desc[n]})
            n = n + 1
        #print(dict_1)  # Dictionary disease : description

        lf = []
        for a in l_disease:
            x = ds.loc[a]
            ls = []
            for b in x:
                if type(b) == str:
                    ls = ls + [b.strip()]
            lf = lf + [ls]

        #print(lf)
        l_disease_sym = lf  # The list made of list of symptoms of the diseases

        p = len(l_disease)
        q = 0
        l1 = []
        while q < p:
            ln = lf[q]
            l2 = []
            for i in ln:
                if i in l_input:
                    l2 = l2 + [i]
            l1 = l1 + [l2]
            q = q + 1
        #print(l1)
        l_common_sym = l1

        dt = pd.read_csv(r'static//file//Sev Final.csv', index_col="Symptom")
        l3 = []
        for b in l_disease_sym:
            l4 = []
            n = 0
            n1 = len(b)
            while n != n1:
                x = dt.loc[b[n]]
                n += 1
                l4 = l4 + [x["weight"]]

            s = 0
            for k in l4:
                s = s + k
            l3 = l3 + [s]

        #print(l3)
        l_disease_sev = l3  # List of sum of severity values of the disease

        l3 = []

        for b in l_common_sym:
            l4 = []
            n = 0
            n1 = len(b)
            while n != n1:
                x = dt.loc[b[n]]
                n += 1
                l4 = l4 + [x["weight"]]

            s = 0
            for k in l4:
                s = s + k
            l3 = l3 + [s]
        #print(l3)
        l_input_sym = l3  # List of sum of severity values of the disease

        dict1 = {}
        num = 0
        num1 = len(l3)
        while num != num1:
            dict1.update({l_disease[num]: l_disease_sev[num]})
            num = num + 1
        #print(dict1)  # Dictionary of the disease name and the sum of symptom severity as the value

        # Calculating the probabilities of disease occurrence
        dict2 = {}
        p = 0
        p1 = len(l_disease)
        while p != p1:
            dict2.update({l_disease[p]: (l_input_sym[p] / (dict1[l_disease[p]]))})
            p = p + 1

        #print(dict2)  # Dictionary of the disease name and probability as the value

        # Switching the keys to items and sorting in Descending
        dict3 = {value: key for key, value in dict2.items()}
        #print(dict3)
        new_list = list(dict3.items())
        new_list.sort(reverse=True)
        dict4 = dict(new_list)
        #print(dict4)
        # count = 1
        # for z in dict4:
        #     #print(f'The number-{count} disease with the probability is: ')
        #     #print(f"It is {dict4[z]} with a probability of {z}")
        #     count = count + 1


    else:
        d1 = pd.read_csv(r'static//file//Desc Final.csv', index_col="Disease")

        lf = []
        for x in l_disease:
            y = d1.loc[x]
            ls = []
            for b in y:
                ls = ls + [b]
            lf = lf + ls

        l_desc = lf
        #print(l_desc)

        dict_1 = {}
        n1 = len(l_disease)
        n = 0
        while n != n1:
            dict_1.update({l_disease[n]: l_desc[n]})
            n = n + 1
        #print(dict_1)

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
                x = dt.loc[b[n]]#here showing error
                n += 1
                l4 = l4 + [x["weight"]]
            #print(l4)
            s = 0
            for k in l4:
                s = s + k
            l3 = l3 + [s]

        #print(l3)  # List of sum of severity values of the disease

        dict1 = {}
        num = 0
        num1 = len(l3)
        while num != num1:
            dict1.update({l_disease[num]: l3[num]})
            num = num + 1
        #print(dict1)  # Dictionary of the disease name and the sum of symptom severity as the value

        # Calculating the probabilities of disease occurrence
        dict2 = {}
        p = 0
        p1 = len(l_disease)
        while p != p1:
            dict2.update({l_disease[p]: (total / (dict1[l_disease[p]]))})
            p = p + 1

        #print(dict2)  # Dictionary of the disease name and probability as the value

        # Switching the keys to items and sorting in Descending
        dict3 = {value: key for key, value in dict2.items()}
        #print(dict3)
        new_list = list(dict3.items())
        new_list.sort(reverse=True)
        dict4 = dict(new_list)
        #print(dict4)
        count = 1
        # for z in dict4:
        #     #print(f'The number-{count} disease with the probability is: ')
        #     #print(f"It is {dict4[z]} with a probability of {z}")
        #     count = count + 1
    return dict4,dict_1,lf
