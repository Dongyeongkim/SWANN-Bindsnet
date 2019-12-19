import os
import src.Genetic as Genetic
from bindsnet.network import nodes
from bindsnet.network import Network
from bindsnet.network.topology import Connection
from bindsnet.learning.learning import MSTDP

def Translate_into_Networks(input_N,Shape,Output_N,Weight):
    path = "gene/"; file_list = os.listdir(path)
    gene_file_check = [file for file in file_list if file.endswith(".txt")]
    if len(gene_file_check) == 0:
        import src.startup
    Network_List = []
    Gene_List = Genetic.Read_Gene()
    for i in range(len(Gene_List)):
        network = Network()
        Input_Layer = nodes.Input(n=input_N, shape=Shape)
        Output_Layer = nodes.LIFNodes(n=Output_N)
        network.add_layer(layer=Input_Layer, name="Input_Layer")
        network.add_layer(layer=Output_Layer, name="Output_Layer")
        Decoded_List = []
        for j in range(len(Gene_List[i])):
            Decoded_Gene=Gene_List[i][j].split('-')
            if(Decoded_Gene[3]=='F'):
                pass
            else:
                if Decoded_Gene[1] == '~':
                    Decoded_List.append([int(Decoded_Gene[0]), int(Decoded_Gene[2]), 0])
                elif Decoded_Gene[1] == '!':
                    Decoded_List.append([int(Decoded_Gene[0]), int(Decoded_Gene[2]), 1])
                elif Decoded_Gene[1] == '@':
                    Decoded_List.append([int(Decoded_Gene[0]), int(Decoded_Gene[2]), 2])
                elif Decoded_Gene[1] == '#':
                    Decoded_List.append([int(Decoded_Gene[0]), int(Decoded_Gene[2]), 3])
                elif Decoded_Gene[1] == '$':
                    Decoded_List.append([int(Decoded_Gene[0]), int(Decoded_Gene[2]), 4])
                else:
                    print("THE GENOTYPE VALUE IS UNVALID");
                    raise ValueError
        for k in range(len(Decoded_List)):
            if(k==len(Decoded_List)):
                break
            for l in range(k+1,len(Decoded_List)):
                if Decoded_List[k][0:1] == Decoded_List[l][0:1]:

                    if Decoded_List[k][2] == 0:
                        Decoded_List.remove(Decoded_List[l])

                    elif Decoded_List[k][2] == 1:
                        if Decoded_List[l][2] < 1:
                            Decoded_List.remove(Decoded_List[k])
                        else:
                            Decoded_List.remove(Decoded_List[l])

                    elif Decoded_List[k][2] == 2:
                        if Decoded_List[l][2] < 2:
                            Decoded_List.remove(Decoded_List[k])
                        else:
                            Decoded_List.remove(Decoded_List[l])

                    elif Decoded_List[k][2] == 3:
                        if Decoded_List[l][2] < 3:
                            Decoded_List.remove(Decoded_List[k])
                        else:
                            Decoded_List.remove(Decoded_List[l])

                    elif Decoded_List[k][2] == 4:
                        if Decoded_List[l][2] >= 4:
                            Decoded_List.remove(Decoded_List[l])
                        else:
                            Decoded_List.remove(Decoded_List[k])

                    else:
                        pass

                else:
                    pass
        layer_list = {};layer_key_list = []
        for m in range(len(Decoded_List)):
            for n in range(len(Decoded_List)):
                if Decoded_List[m][1] == Decoded_List[n][0]:
                    if Decoded_List[n][2] == '0':
                        layer_list[m] = nodes.IFNodes(n=1)
                    elif Decoded_List[n][2] == '1':
                        layer_list[m] = nodes.LIFNodes(n=1)
                    elif Decoded_List[n][2] == '2':
                        layer_list[m] = nodes.McCullochPitts(n=1)
                    elif Decoded_List[n][2] == '3':
                        layer_list[m] = nodes.IzhikevichNodes(n=1)
                    elif Decoded_List[n][2] == '4':
                        layer_list[m] = nodes.SRM0Nodes(n=1)
                    else:
                        print("UNVALID GENO_NEURON CODE");raise ValueError

                elif n == len(Decoded_List):
                    layer_list[m] = nodes.LIFNodes(n=1)
        





#TODO: ADDING THE CONNECTION BETWEEN THE LAYERS



