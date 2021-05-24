import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import numpy as np

import torch.distributed as dist
import torch

from parameters import get_args
#from FL.utils.node import Client, Master
from FL.utils.topology import Graph



def main(args):
    
    
    
    dist.init_process_group("mpi")
    
    
    # init the config.
    init_config(args)
    
    # sync the processes.
    dist.barrier()

    # start federated learning.
    
    
#     if args.graph.rank == 0:
#         process = Master(args) 
#     else:
#         process = Worker(args)
    
#     process.run()
    
    
def init_config(args):
    # define the graph for the computation.
    args.graph = Graph(dist.get_rank(), args.n_processes, args.world, args.on_cuda)
    
    
    
    # init related to randomness on cpu.
    if not args.same_seed_for_processes:
        args.manual_seed = 1000 * args.manual_seed + args.graph.rank
    args.random_state = np.random.RandomState(args.manual_seed)
    torch.manual_seed(args.manual_seed)
    
    

    if args.graph.on_cuda:
        assert torch.cuda.is_available()
        torch.cuda.manual_seed(args.manual_seed)
        torch.cuda.set_device(args.graph.device)
        torch.backends.cudnn.enabled = True
        torch.backends.cudnn.benchmark = True
        
    

    
    







if __name__ == '__main__':
    
    args = get_args()    
    main(args)



