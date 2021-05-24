import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import argparse


from FL import models



def str2bool(v):
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        return v



def get_args():
    
    model_names = sorted(
        name for name in models.__dict__ if name.islower() and not name.startswith("__")
    )
    
    
    
    
    parser = argparse.ArgumentParser(description='Parameters for running training')
    parser.add_argument('--data',type=str, default='mnist',choices=['mnist','cifar10'],help='dataset name')
    parser.add_argument('--models',type=str, default='mlp:vgg:resnet',help='model names:'+str(model_names))
    parser.add_argument('--n_clients',type=int, default=30, help='the number of clients')
    parser.add_argument('--participation_ratio',type=float, default=1.0, help='participated ratio of clients')
    parser.add_argument("--on_cuda", action='store_true')
    parser.add_argument("--same_seed_for_processes", action='store_true')
    parser.add_argument("--manual_seed", type=int, default=6, help="manual seed")
    
    
    parser.add_argument("--n_participated", default=None, type=int)
    parser.add_argument("--world", default=None, type=str)
    parser.add_argument("--n_processes", default=None, type=int)
    
    
    
    args = parser.parse_args()
    
    
    
    return args
