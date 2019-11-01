import numpy as np
import time

class MBOG(object):
    def __init__(self, dims, min_func, pop_size=30,
                 max_gen=30, s_max=1, bar=float(5/12),
                 peri=1.2, p=float(5/12), num_elite=3):
        """
        Intialization requires the number of dimensions, `dims`, for the minimization function, `min_func`
        """
        self._dims = dims
        self.min_func = min_func
        self.tolarance = 1*(10**-3)
        self.termination_condtion_met = False
        self.pop_size = pop_size
        self.t = 1
        self.butterfly_population = None
        self.np1 = None
        self.np2 = None
        self.max_gen = max_gen
        self.s_max = s_max
        self.bar = bar
        self.peri = peri
        self.p = p

        self.num_elite = num_elite
        self.elite = None

    def _initialize_population(self, pop_size, dim):
        """ 
        Create the butterfly population according the array,
        [fitness, x1,x2,...]
        """
        dtype = [(f'x{i}', float) for i in range(dim)]
        dtype.insert(0, ('fitness', float))
        temp_list = []
        for row in range(self.pop_size):
            temp_list.append(tuple(np.random.randn(1,dim+1).squeeze()))
        return np.array(temp_list, dtype=dtype)

    
    def _sort_population(self, pop):
        """ Sort the population of butterflies, best to worst """
        return np.sort(pop, order='fitness')
    
    def _fitness_eval(self, pop):
        """ Evaluate the fitness of each butterfly """
        for i, butterfly in enumerate(pop):
            pop[i][0] = self.min_func(list(butterfly)[1:])
        return pop

    def _split_population(self):
        """ Split needs to distributed according to the ratio `p` """

        self.np1, self.np2 = np.split(self.butterfly_population, [np.math.ceil(self.p * self.pop_size)])

    def _migration_operator(self):
        """ The migration operator to be performed on population NP1 """

        for i, butterfly in enumerate(self.np1):
            for k in range(len(butterfly)):
                if k == 0:
                    # Skip the fitness element
                    pass
                else:
                    rand = np.random.uniform(low=0, high=1)
                    if rand*self.peri <= self.p:
                        random_butterfly_np1 = np.random.choice(self.np1)
                        butterfly[k] = random_butterfly_np1[k]
                    else:
                        random_butterfly_np2 = np.random.choice(self.np2)
                        butterfly[k] = random_butterfly_np2[k]
            # Evaluate new butterfly's fitness, if better than parent, replace parent
            if self.min_func(list(butterfly)[1:]) < butterfly[0]:
                self.np1[i] = butterfly
            # Evaluate NP1 fitness
            self.np1 = self._fitness_eval(self.np1)
            # Sort NP1
            self.np1 = self._sort_population(self.np1)

    
    def _butterfly_adjusting_operator(self):
        """ The butterfly adjusting operator to be performed on population NP2 """
        for i, butterfly in enumerate(self.np2):
            dx = self._levy()
            alpha = self.s_max/self.t**2
            for k in range(len(butterfly)):
                if k == 0:
                    pass
                else:
                    rand = np.random.uniform(low=0, high=1)
                    if rand <= self.p:
                        # Best butterfly in NP1 and NP2 will be the first
                        if self.np1[0][0] < self.np2[0][0]:
                            best_butterfly = self.np1[0]
                        else:
                            best_butterfly = self.np2[0]
                        butterfly[k] = best_butterfly[k]
                    else:
                        random_butterfly_np2 = np.random.choice(self.np2)
                        butterfly[k] = random_butterfly_np2[k]
                        if rand > self.bar:
                            butterfly[k] += alpha*(dx - 0.5)
                # Evaluate new butterfly's fitness, if better than parent, replace parent
            if self.min_func(list(butterfly)[1:]) < butterfly[0]:
                self.np2[i] = butterfly
            # Evaluate NP1 fitness
            self.np2 = self._fitness_eval(self.np2)
            # Sort NP1
            self.np2 = self._sort_population(self.np2)

    def _levy(self):
        """ Perform levy flight """
        return np.sum(np.tan(np.math.pi * np.random.uniform(low=0, high=1, size=(1,self.s_max))))

    def _combine_population(self):
        """ Recombine population NP1 and NP2 """
        self.butterfly_population = np.concatenate((self.np1,self.np2))
    
    def _check_termination_condition(self):
        delta = abs(self.butterfly_population[0][0] - self.elite[0][0])
        if delta <= self.tolarance and self.t != 1:
            self.termination_condtion_met = True

    def _main_loop(self):
        while not self.termination_condtion_met and self.t <= self.max_gen:
            self._sort_population(self.butterfly_population)
            self._elitism(action='apply')
            self._elitism(action='save')
            self._check_termination_condition()
            self._split_population()
            self._migration_operator()
            self._butterfly_adjusting_operator()
            self._combine_population()
        
            self.t += 1
    
    def _elitism(self, action):
        """ Keep the n best butterflies from previous generation """
        if action == 'save':
            self.elite = []
            for e in range(self.num_elite):
                self.elite.append(self.butterfly_population[e])
        elif self.elite and action =='apply':
            for i, e in enumerate(self.elite):
                self.elite[-1-i] = e


    def run(self,*args, **kwargs):
        self.butterfly_population = self._initialize_population(pop_size=self.pop_size,
                                    dim=self._dims)
        self._fitness_eval(self.butterfly_population)
        self._main_loop()
        # return the result of the run
        return list(self._sort_population(self.butterfly_population)[0])

    

    

