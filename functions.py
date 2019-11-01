import math

class MinimizationFunctions(object):
    def __init__(self, func_type):
        self._func_type = func_type
        self._bounds = None
        self._dict_bounds = {'f6': 100,
                            'f7': 100,
                            'ackley': 32.768,
                            'schwefel': 500,
                            'rastrigin': 5.12
                            }

        self._func_dict = {'f6': self._f6,
                          'f7': self._f7,
                          'ackley': self._achley,
                          'schwefel': self._schwefel,
                          'rastrigin': self._rastrigin
                          }
        
        
        self._set_bounds()
    
    def f(self, x):
        """ Evaluate the function over the given arguments, x """
        return self._func_dict[self._func_type](x)

    def _set_bounds(self):
        """ Private method to set up the bounds for the given functions """
        self._bounds = self._dict_bounds[self._func_type]
    
    def get_bounds(self):
        """ Get the boundry of the given function. Returns a postive float,
        b, which is interpreted as [-b, +b]
        """
        return self.bounds

    # Define the functions

    def _f6(self, x):
        """ Schaffer's F6 function [-100,100] min @ [0,0,...]"""
        sum_xsqrd = sum(xi**2 for xi in x)
        return 0.5 + (math.sin(math.sqrt(sum_xsqrd)**2) - 0.5) / (1 + 0.001 * sum_xsqrd)**2
    
    def _f7(self, x):
        """ Schaffer's F7 Function [-100,100] min @ [0,0,...]"""
        normalizer = 1.0/float(len(x)-1)
        fitness = 0
        for i in range(len(x)-1):
            si = sum(xi**2 for xi in x[i:i+2])
            fitness += normalizer * math.sqrt(si) * (math.sin(50.0 * si**0.2) + 1)**2
        return fitness
    
    def _achley(self, x):
        """ Achley's Function [-32.768, 32.768] min @ [0,0,...]"""
        a = 20
        b = 0.2
        c = 2 * math.pi
        sum_xi_sqrd = sum(xi**2 for xi in x)
        sum_xi_cos = sum(math.cos(c * xi) for xi in x)
        return -a * math.exp(-b * math.sqrt(1/len(x) * sum_xi_sqrd)) - math.exp(1/len(x) * sum_xi_cos) + a + math.exp(1)
    
    def _schwefel(self, x):
        """ Schwefel's Function [-500, 500] min @ [420.9687, 420.9687,...]"""
        return 418.9829 * len(x) - sum(xi * math.sin(math.sqrt(abs(xi))) for xi in x)
    
    def _rastrigin(self, x):
        """ Rastrigin's Function [-5.12, 5.12] min @ [0, 0,...]"""
        return 10*len(x) + sum(xi**2 - 10 * math.cos(2 * math.pi * xi) for xi in x)