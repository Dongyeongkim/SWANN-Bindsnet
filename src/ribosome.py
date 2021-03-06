import os
import torch
import Genetic
from bindsnet.network import nodes
from bindsnet.network import Network
from bindsnet.network.topology import Connection
from bindsnet.learning.learning import MSTDP


def Translate_Into_Networks(input_N,Shape,Output_N,Weight):
    network_list = []
    path = "gene/"; file_list = os.listdir(path)
    gene_file_check = [file for file in file_list if file.endswith(".txt")]
    if len(gene_file_check) == 0:
        import startup
    Gene_List = Genetic.Read_Gene()
    for i in range(len(Gene_List)):
        network = Network()
        Decoded_List = []; Decoded_DNA_List = []
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
                    print("THE GENOTYPE VALUE IS UNVALID")
                    raise ValueError
            Decoded_DNA_List.append(Decoded_List)

        Decoded_RNA_List: list = Decoded_DNA_List.copy()

        for decoded_dna_idx, decoded_dna in enumerate(Decoded_DNA_List):
            Gene_NUM = len(decoded_dna)
            for k in range(Gene_NUM):
                a = Decoded_DNA_List[decoded_dna_idx][k]
                for l in range(k, Gene_NUM):
                    b = Decoded_DNA_List[decoded_dna_idx][l]
                    if a and b == 1:
                        if decoded_dna[k][2] == 0:
                            Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[l])

                        elif decoded_dna[k][2] == 1:
                            if decoded_dna[l][2] < 1:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[k])
                            else:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[l])

                        elif decoded_dna[k][2] == 2:
                            if decoded_dna[l][2] < 2:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[k])
                            else:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[l])

                        elif decoded_dna[k][2] == 3:
                            if decoded_dna[l][2] < 3:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[k])
                            else:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[l])

                        elif decoded_dna[k][2] == 4:
                            if decoded_dna[l][2] >= 4:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[l])
                            else:
                                Decoded_RNA_List[decoded_dna_idx].remove(decoded_dna[k])

                        else:
                            pass

                    else:
                        pass


        for Decoded_RNA in Decoded_RNA_List:
            
            layer_list = {}
            
            for m in range(len(Decoded_RNA)):

                for n in range(m, len(Decoded_RNA)):
                    if Decoded_RNA[m][1] == Decoded_RNA[n][0]:
                        if Decoded_RNA[n][2] == 0:
                            layer_list[Decoded_RNA[m][0]] = nodes.IFNodes(n=1, traces=True)
                        elif Decoded_RNA[n][2] == 1:
                            layer_list[Decoded_RNA[m][0]] = nodes.LIFNodes(n=1, traces=True)
                        elif Decoded_RNA[n][2] == 2:
                            layer_list[Decoded_RNA[m][0]] = nodes.McCullochPitts(n=1, traces=True)
                        elif Decoded_RNA[n][2] == 3:
                            layer_list[Decoded_RNA[m][0]] = nodes.IzhikevichNodes(n=1, traces=True)
                        elif Decoded_RNA[n][2] == 4:
                            layer_list[Decoded_RNA[m][0]] = nodes.SRM0Nodes(n=1, traces=True)
                        else:
                            print("UNVALID GENO_NEURON CODE")
                            raise ValueError

                    elif n == len(Decoded_List) - 1:
                        layer_list[Decoded_RNA[m][1]] = nodes.LIFNodes(n=1)
            
            for l in range(len(Decoded_RNA)):
                if not Decoded_RNA[l][0] in layer_list:
                    if Decoded_RNA[l][2] == 0:
                        layer_list[Decoded_RNA[l][0]] = nodes.IFNodes(n=1, traces=True)
                    elif Decoded_RNA[l][2] == 1:
                        layer_list[Decoded_RNA[l][0]] = nodes.LIFNodes(n=1, traces=True)
                    elif Decoded_RNA[l][2] == 2:
                        layer_list[Decoded_RNA[l][0]] = nodes.McCullochPitts(n=1, traces=True)
                    elif Decoded_RNA[l][2] == 3:
                        layer_list[Decoded_RNA[l][0]] = nodes.IzhikevichNodes(n=1, traces=True)
                    elif Decoded_RNA[l][2] == 4:
                        layer_list[Decoded_RNA[l][0]] = nodes.SRM0Nodes(n=1, traces=True)

        Input_Layer = nodes.Input(n=input_N, shape=Shape, traces=True)
        out = nodes.LIFNodes(n=Output_N, refrac=0, traces=True)
        network.add_layer(layer=Input_Layer,name="Input Layer")
        for key_l in list(layer_list.keys()):
            network.add_layer(layer=layer_list[key_l], name=str(key_l))
        network.add_layer(layer=out, name="Output Layer")
        if len(layer_list.keys()) == 0:
            layer = nodes.LIFNodes(n=1,traces=True)
            network.add_layer(layer=layer,name="mid layer")
            inpt_connection = Connection(source=Input_Layer,target=layer,w=Weight*torch.ones(input_N))
            opt_connection = Connection(source=layer,target=out,w=Weight*torch.ones(1))
            network.add_connection(inpt_connection,source="Input_Layer",target="mid layer")
            network.add_connection(opt_connection,source="mid layer",target="Output Layer")
        else:
            for key_ic in list(layer_list.keys()):
                inpt_connection = Connection(source=Input_Layer, target=layer_list[key_ic],
                                             w=Weight*torch.ones(input_N))
                network.add_connection(inpt_connection, source="Input_Layer", target=str(key_ic))
            for key_op in list(layer_list.keys()):
                output_connection = Connection(source=layer_list[key_op], target=out,
                                               w=Weight*torch.ones(1), update_rule=MSTDP)
                network.add_connection(output_connection, source=str(key_op), target="Output Layer")
            for generating_protein in Decoded_RNA:
                mid_connection = Connection(source=layer_list[generating_protein[0]],
                                            target=layer_list[generating_protein[1]],
                                            w=Weight*torch.ones(1),update_rule=MSTDP)
                network.add_connection(mid_connection, source=str(generating_protein[0]),
                                       target=str(generating_protein[1]))

        network_list.append(network)
        network.save('Network/' + str(i) + '.pt')
    return network_list




