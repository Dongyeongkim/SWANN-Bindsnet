import os
import src.Genetic as Genetic
from bindsnet.network import nodes
from bindsnet.network import Network
from bindsnet.network.topology import Connection
from bindsnet.learning.learning import PostPre

def Translate_Into_Networks(input_N,Shape,Output_N,Weight):
    path = "gene/"; file_list = os.listdir(path)
    gene_file_check = [file for file in file_list if file.endswith(".txt")]
    if len(gene_file_check) == 0:
        import src.startup
    Gene_List = Genetic.Read_Gene()
    for i in range(len(Gene_List)):
        network = Network()
        Input_Layer = nodes.Input(n=input_N, shape=Shape, traces=True)
        Output_Layer = nodes.LIFNodes(n=Output_N, refrac=0, traces=True)
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
                    print("THE GENOTYPE VALUE IS UNVALID")
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

        layer_list = {}
        for m in range(len(Decoded_List)):
            for n in range(len(Decoded_List)):
                if Decoded_List[m][1] == Decoded_List[n][0]:
                    if Decoded_List[n][2] == '0':
                        layer_list[m] = nodes.IFNodes(n=1,traces=True)
                    elif Decoded_List[n][2] == '1':
                        layer_list[m] = nodes.LIFNodes(n=1,traces=True)
                    elif Decoded_List[n][2] == '2':
                        layer_list[m] = nodes.McCullochPitts(n=1,traces=True)
                    elif Decoded_List[n][2] == '3':
                        layer_list[m] = nodes.IzhikevichNodes(n=1,traces=True)
                    elif Decoded_List[n][2] == '4':
                        layer_list[m] = nodes.SRM0Nodes(n=1,traces=True)
                    else:
                        print("UNVALID GENO_NEURON CODE");raise ValueError

                elif n == len(Decoded_List)-1:
                    layer_list[m] = nodes.LIFNodes(n=1)

        for key_l in list(layer_list.keys()):
            network.add_layer(layer=layer_list[key_l], name=str(key_l))

        for key_ic in list(layer_list.keys()):
            input_connection = Connection(source=Input_Layer, target=layer_list[key_ic], w=Weight)
            network.add_connection(input_connection, source="Input_Layer", target=str(key_ic))

        for key_op in list(layer_list.keys()):
            output_connection = Connection(source=layer_list[key_op], target=Output_Layer[key_op % len(Output_Layer)])
            network.add_connection(output_connection, source=str(key_op), target="Output_" + str(key_op % len(Output_Layer)),
                                   w=Weight)

        for o in range(len(Decoded_List)):
            mid_connection = Connection(source=layer_list[Decoded_List[0]], target=layer_list[Decoded_List[1]],
                                        wmin=-2, wmax=2, update_rule=PostPre, norm=Weight)
            network.add_connection(mid_connection,source=str(Decoded_List[0]), target=str(Decoded_List[1]))

        network.save('Network/'+str(i)+'.pt')





