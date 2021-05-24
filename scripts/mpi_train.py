# -*- coding: utf-8 -*-
import os
import argparse




from parameters import get_args


import pdb






def main_mpi(args):
    
    
    
    args.world=",".join([str(i) for i in range(args.n_processes)])
        
    # get the n_participated clients per communication round.
    args.n_participated = int(args.n_clients * args.participation_ratio + 0.5)
    assert args.n_participated > 0
    
    args.n_processes=args.n_participated+1


    prefix_cmd = 'mpirun -np {} --allow-run-as-root  --oversubscribe --mca orte_base_help_aggregate 0 --mca btl_tcp_if_exclude docker0,lo '.format(args.n_processes)
    cmd = 'python main.py'
    for k,v in args.__dict__.items():
        if v is not None:
            cmd +=' --{} {}'.format(k, v)
    cmd = prefix_cmd + cmd
    print('\nRunnig the following command:\n' + cmd)
    os.system(cmd)




if __name__ == '__main__':
    
    args = get_args()    
    main_mpi(args)