# Written by Benny Hwang for COMP9021 Lab 3


expectedi = []
expectedj = []
expectedk = []
expectedproduct = []
for i in range(10,100):
    for j in range(10,100):
        for k in range(10,100):
            if i != j and i != k and j != k:
                product = i*j*k
                if (i not in expectedi) and (j not in expectedj) and (k not in expectedk) and (product not in expectedproduct):
                    i_list_form = [int(n) for n in str(i)]
                    j_list_form = [int(n) for n in str(j)]
                    k_list_form = [int(n) for n in str(k)]
                    p_list_form = [int(n) for n in str(product)]

                    iTest = []
                    for a in i_list_form:
                        if a in p_list_form:
                            iTest.append(a)
                            p_list_form.remove(a)

                    if len(iTest) == 2:
                        jTest = []
                        for a in j_list_form:
                            if a in p_list_form:
                                jTest.append(a)
                                p_list_form.remove(a)

                        if len(jTest) == 2:
                            kTest = []
                            for a in k_list_form:
                                if a in p_list_form:
                                    kTest.append(a)
                                    p_list_form.remove(a)

                            if len(kTest) == 2:
                                expectedi.append(i)
                                expectedj.append(j)
                                expectedk.append(k)
                                expectedproduct.append(product)
                                print(i,'x',j,'x',k,'=',product)

                        
                    '''        
                    iTest = [a for a in i_list_form if a in p_list_form]
                    print(iTest)
                    
                    if len(iTest) == 2:
                        jTest = [a for a in j_list_form if a in p_list_form]
                        if len(jTest) == 2:
                            kTest = [a for a in k_list_form if a in p_list_form]
                    '''
                            

                    
