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
        if(j>len(C_Gene1)-1):
            A_Gene2.append(C_Gene2)
        else:
            S_Genotype = rd.randint(0, 1)
            if(S_Genotype==0):
                A_Gene2.append(C_Gene1[j])
            else:
                A_Gene2.append(C_Gene2[j])
    
    return A_Gene1,A_Gene2

def Generate_Gene_Base(Neuron_a):
    Neuron_Num = Neuron_a # Neuron Amount
    Neuron_Type = rd.choice('~!@#$')
    while True:
        s = rd.randint(1,Neuron_Num)
        t = rd.randint(1,Neuron_Num)
        if(s!=t):
            q= len(str(Neuron_a))-len(str(s))
            r= len(str(Neuron_a))-len(str(t))
            Emp_S='';Emp_T='' # For Filling empty space by 0
            for _ in range(q):
                Emp_S+='0'
            Emp_S+=str(s)
            for _ in range(r):
                Emp_T+='0'
            Emp_T+=str(t)
            Source_Neuron = Emp_S
            Target_Neuron = Emp_T
            break
        else:
            pass
    Connection = rd.choice('01')
    if(Connection=='0'):
        Connection = 'T'
    else:
        Connection = 'F'

    Gene_Base = Source_Neuron + Neuron_Type + Target_Neuron + Connection
    return Gene_Base


def Mutate(Gene,accr,Neuron_Num):

    Mutated_Gene = []
    for i in range(len(Gene)):
        random_PER = rd.random()
        if(1-accr>random_PER):
            Mutated_Gene.append(Gene[i])
        else:
            if(Gene[i].isdecimal()==False):
                Gene_Slave = Gene.split(Gene[i])
                Source_Neuron = int(Gene_Slave[0])
                Gene_Slave = Gene_Slave[1]
                for j in range(len(Gene_Slave)):
                    if(Gene_Slave[j].isdecimal()==False):
                        Gene_Slave = Gene_Slave.split(Gene_Slave[j])
                        Target_Neuron = Gene_Slave[0]
                    else:
                        pass

            else:
                pass
                
            Neuron_Type = rd.choice('~!@#$')
            Connection = rd.choice('01')
            if(Connection=='0'):
                Connection = 'T'
            else:
                Connection = 'F'
            Mutated_Gene.append(Source_Neuron + Neuron_Type + Target_Neuron + Connection)
        
    random_factor = rd.random()
    while(0.7-accr>random_factor):
        random_factor = rd.random()
        Mutated_Gene.append(Generate_Gene_Base(Neuron_Num))
    
    return Mutated_Gene


def Calc_Fitness(accr_set):
    Sum=sum(accr_set)
    fitness_set = []
    for i in range(len(accr_set)):
        fitness_set.append(accr_set[i]/Sum)
    return fitness_set
