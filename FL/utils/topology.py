




class Graph():
    def __init__(self, rank, n_processes ,world, on_cuda):
        self._rank = rank
        self._n_processes = n_processes
        self._world = world
        self._on_cuda = on_cuda
        
    @property
    def rank(self):
        return self._rank
    
    @property
    def n_processes(self):
        return self._n_processes
    
    @property
    def on_cuda(self):
        return self._on_cuda
    
    
    @property
    def world(self):
        return [int(l) for l in self._world.split(',')]
    
    @property
    def device(self):
        return self.world[self.rank]


    
        