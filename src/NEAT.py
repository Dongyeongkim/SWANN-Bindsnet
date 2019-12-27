import random as rd

### - IMPLEMENT NEAT ALGORITHM TO THIS - ###

def Crossover(gene1,gene2):
    A_Gene1 = []; A_Gene2 = []
    C_Gene1 = gene1; C_Gene2 = gene2
    # Crossovering Process
    for i in range(len(C_Gene1)):
        if(i>len(C_Gene2)-1):
            A_Gene1.append(C_Gene1)
        else:
            S_Genotype = rd.randint(0, 1)
            if(S_Genotype==0):
                A_Gene1.append(C_Gene1[i])
            else:
                A_Gene1.append(C_Gene2[i])
     
    for j in range(len(C_Gene2)):
        if j > len(C_Gene1)-1:
            A_Gene2.append(C_Gene2)
        else:
            S_Genotype = rd.randint(0, 1)
            if S_Genotype == 0:
                A_Gene2.append(C_Gene1[j])
            else:
                A_Gene2.append(C_Gene2[j])
    
    return A_Gene1, A_Gene2

def Generate_Gene_Base(Neuron_a):
    Neuron_Num = Neuron_a # Neuron Amount
    Neuron_Type = rd.choice('~!@#$')
    s = rd.randint(1,Neuron_Num)
    t = rd.randint(1,Neuron_Num)
    Source_Neuron = s; Target_Neuron = t
    Connection = rd.choice('01')
    if(Connection=='0'):
        Connection = 'F'
    elif(Connection=='1'):
        Connection = 'T'
    Gene_Base = str(Source_Neuron) +'-'+ Neuron_Type +'-'+ str(Target_Neuron) +'-'+ Connection
    return Gene_Base


def Mutate(Gene,accr,Neuron_Num):
    Mutated_Gene = []
    for i in range(len(Gene)):
        random_PER = rd.random()
        if(1-accr>random_PER):
            Mutated_Gene.append(Gene[i])
        else:
            Decoded_Gene = Gene[i].split('-')
            Source_Neuron = Decoded_Gene[0]
            Target_Neuron = Decoded_Gene[2]
            Neuron_Type = rd.choice('~!@#$')
            Connection = rd.choice('01')
            if(Connection=='0'):
                Connection = 'T'
            else:
                Connection = 'F'
            Mutated_Gene.append(str(Source_Neuron)+'-'+Neuron_Type +'-'+str(Target_Neuron)+'-'+Connection)
        
    random_factor = rd.random()
    while 0.7 - accr > random_factor:
        random_factor = rd.random()
        Mutated_Gene.append(Generate_Gene_Base(Neuron_Num))
    
    return Mutated_Gene


def calc_and_select_gene(accr_set, gene_list):
    all_sum = sum(accr_set)
    fitness_set = []; selected_gene = []
    for i in range(len(accr_set)):
        fitness_set.append(accr_set[i]/all_sum)
    for j in range(len(gene_list)):
        selected_gene.append(rd.choice(gene_list, p=fitness_set))
    return selected_gene
