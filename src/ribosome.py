import os
import src.Genetic as Genetic
from bindsnet.network import nodes
from bindsnet.network import Network
from bindsnet.network.topology import Connection
from bindsnet.learning.learning import MSTDP

def Translate_into_Networks(input_N,Shape,Output_N):
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
        layer = []
        for j in range(len(Gene_List[i])):
            Decoded_Gene=Gene_List[i][j].split('-')
            if Gene_List[i][j]
            if Decoded_Gene[1] == '~':
                layer.append([int(Decoded_Gene[0]),int(Decoded_Gene[2]),0])
            elif Decoded_Gene[1] == '!':
                layer.append([int(Decoded_Gene[0]),int(Decoded_Gene[2]),1])
            elif Decoded_Gene[1] == '@':
                layer.append([int(Decoded_Gene[0]),int(Decoded_Gene[2]),2])
            elif Decoded_Gene[1] == '#':
                layer.append([int(Decoded_Gene[0]),int(Decoded_Gene[2]),3])
            elif Decoded_Gene[1] == '$':
                layer.append([int(Decoded_Gene[0]),int(Decoded_Gene[2]),4])
            else:
                print("THE GENOTYPE VALUE IS UNVALID");raise ValueError
        for k in range(len(layer)):
            if layer[k][2] == 0:
                source_layer = nodes.IFNodes(n=1)
                target_layer = nodes.LIFNodes(n=1)
                inpt_connection = Connection(source=Input_Layer,target_layer=source_layer,wmin=0,wmax=1e-1)
                mid_connection = Connection(source=source_layer,target=target_layer,wmin=0,wmax=1,update_rule=MSTDP,
                                            nu=1e-1,norm=0.5*source_layer.n)
                output_connection = Connection(source=target_layer,target=Output_Layer,wmin=0,wmax=1,
                                               update_rule=MSTDP,nu=1e-1,norm=0.5*target_layer.n)
                network.add_layer(layer=source_layer, name=str(layer[k][0])); network.add_layer(layer=target_layer, name=str(layer[k][1]))
                network.add_connection(inpt_connection,source_layer="Input_Layer",target_layer=str(layer[k][0]))
                network.add_connection(mid_connection, source_layer=str(layer[k][0]), target_layer=str(layer[k][1]))
                network.add_connection(output_connection, source_layer=str(layer[k][1]),target_layer="Output_Layer")


            elif layer[k][2] == 1:
                source_layer = nodes.LIFNodes(n=1)
                target_layer = nodes.LIFNodes(n=1)
                inpt_connection = Connection(source=Input_Layer, target_layer=source_layer, wmin=0, wmax=1e-1)
                mid_connection = Connection(source=source_layer, target=target_layer, wmin=0, wmax=1, update_rule=MSTDP,
                                            nu=1e-1, norm=0.5 * source_layer.n)
                output_connection = Connection(source=target_layer, target=Output_Layer, wmin=0, wmax=1,
                                               update_rule=MSTDP, nu=1e-1, norm=0.5 * target_layer.n)
                network.add_layer(layer=source_layer, name=str(layer[k][0]));
                network.add_layer(layer=target_layer, name=str(layer[k][1]))
                network.add_connection(inpt_connection, source_layer="Input_Layer", target_layer=str(layer[k][0]))
                network.add_connection(mid_connection, source_layer=str(layer[k][0]), target_layer=str(layer[k][1]))
                network.add_connection(output_connection, source_layer=str(layer[k][1]), target_layer="Output_Layer")

            elif layer[k][2] == 2:
                source_layer = nodes.McCullochPitts(n=1)
                target_layer = nodes.LIFNodes(n=1)
                inpt_connection = Connection(source=Input_Layer, target_layer=source_layer, wmin=0, wmax=1e-1)
                mid_connection = Connection(source=source_layer, target=target_layer, wmin=0, wmax=1, update_rule=MSTDP,
                                            nu=1e-1, norm=0.5 * source_layer.n)
                output_connection = Connection(source=target_layer, target=Output_Layer, wmin=0, wmax=1,
                                               update_rule=MSTDP, nu=1e-1, norm=0.5 * target_layer.n)
                network.add_layer(layer=source_layer, name=str(layer[k][0]));
                network.add_layer(layer=target_layer, name=str(layer[k][1]))
                network.add_connection(inpt_connection, source_layer="Input_Layer", target_layer=str(layer[k][0]))
                network.add_connection(mid_connection, source_layer=str(layer[k][0]), target_layer=str(layer[k][1]))
                network.add_connection(output_connection, source_layer=str(layer[k][1]), target_layer="Output_Layer")

            elif layer[k][2] == 3:
                source_layer = nodes.IzhikevichNodes(n=1)
                target_layer = nodes.LIFNodes(n=1)
                inpt_connection = Connection(source=Input_Layer, target_layer=source_layer, wmin=0, wmax=1e-1)
                mid_connection = Connection(source=source_layer, target=target_layer, wmin=0, wmax=1, update_rule=MSTDP,
                                            nu=1e-1, norm=0.5 * source_layer.n)
                output_connection = Connection(source=target_layer, target=Output_Layer, wmin=0, wmax=1,
                                               update_rule=MSTDP, nu=1e-1, norm=0.5 * target_layer.n)
                network.add_layer(layer=source_layer, name=str(layer[k][0]));
                network.add_layer(layer=target_layer, name=str(layer[k][1]))
                network.add_connection(inpt_connection, source_layer="Input_Layer", target_layer=str(layer[k][0]))
                network.add_connection(mid_connection, source_layer=str(layer[k][0]), target_layer=str(layer[k][1]))
                network.add_connection(output_connection, source_layer=str(layer[k][1]), target_layer="Output_Layer")

            elif layer[k][2] == 4:
                source_layer = nodes.SRM0Nodes(n=1)
                target_layer = nodes.LIFNodes(n=1)
                inpt_connection = Connection(source=Input_Layer, target_layer=source_layer, wmin=0, wmax=1e-1)
                mid_connection = Connection(source=source_layer, target=target_layer, wmin=0, wmax=1, update_rule=MSTDP,
                                            nu=1e-1, norm=0.5 * source_layer.n)
                output_connection = Connection(source=target_layer, target=Output_Layer, wmin=0, wmax=1,
                                               update_rule=MSTDP, nu=1e-1, norm=0.5 * target_layer.n)
                network.add_layer(layer=source_layer, name=str(layer[k][0]));
                network.add_layer(layer=target_layer, name=str(layer[k][1]))
                network.add_connection(inpt_connection, source_layer="Input_Layer", target_layer=str(layer[k][0]))
                network.add_connection(mid_connection, source_layer=str(layer[k][0]), target_layer=str(layer[k][1]))
                network.add_connection(output_connection, source_layer=str(layer[k][1]), target_layer="Output_Layer")
        Network_List.append(network)
    
    return Network_List
