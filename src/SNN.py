import os
import torch
from tqdm import tqdm
from time import time as t
from torchvision import transforms
from bindsnet.datasets import MNIST
from bindsnet.network.network import load
from bindsnet.encoding import PoissonEncoder
from bindsnet.network.monitors import Monitor


dt = 1.0
time = 50
n_epochs = 100
intensity = 128.0
progress_interval = 10

path = "Network/"
file_list = os.listdir(path)
network_file = [file for file in file_list if file.endswith(".pt")]
network_list = []

for network in network_file:
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(0)
        network = load(network, map_location="cuda", learning=True)
        network.to("cuda")
        network_list.append(network)
    else:
        torch.manual_seed(0)
        load(network, map_location='cpu', learning=True)
        network_list.append(network)




train_dataset = MNIST(
    PoissonEncoder(time=time, dt=dt),
    None,
    "../../data/MNIST",
    download=True,
    train=True,
    transform=transforms.Compose(
        [transforms.ToTensor(), transforms.Lambda(lambda x: x * intensity)]
    ),
)

for network in network_list:
    spikes = {}
    for layer in set(network.layers):
        spikes[layer] = Monitor(network.layers[layer], state_vars=["s"], time=time)
        network.add_monitor(spikes[layer], name="%s_spikes" % layer)

    print("Begin training.\n")

    start = t()

    inpt_axes = None
    inpt_ims = None
    spike_ims = None
    spike_axes = None
    weights1_im = None
    voltage_ims = None
    voltage_axes = None

    for epoch in range(n_epochs):
        if epoch % progress_interval == 0:
            print("Progress: %d / %d (%.4f seconds)" % (epoch, n_epochs, t() - start))
            start = t()
        train_dataloader = torch.utils.data.DataLoader(
            train_dataset, batch_size=1, shuffle=True, num_workers=4, pin_memory=True
        )
        for step, batch in enumerate(tqdm(train_dataloader)):
            # Get next input sample.

            inputs = {"X": batch["encoded_image"]}
            if torch.cuda.is_available():
                inputs = {k: v.cuda() for k, v in inputs.items()}
            label = batch["label"]

            # Run the network on the input.
            network.run(inpts=inputs, time=time, input_time_dim=1)
        network.reset_state_variables()

    print("Progress: %d / %d (%.4f seconds)\n" % (n_epochs, n_epochs, t() - start))
    print("Training complete.\n")
    print(spikes)




