import argparse
from mbo_algorithm import MBOG
from functions import MinimizationFunctions
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='Run the MBO algorithm to find a solution to a minimization problem.')
parser.add_argument('-f', nargs='?',default='f6',
                    choices=['f6','f7','achley', 'schwefel', 'rastrigin'],
                    help='Minimization function')
parser.add_argument('-d', nargs='?',default=2, type=int,
                    help='Number of dimensions of the minimization function')

parser.add_argument('-n', nargs='?',default=10, type=int,
                    help='Number of repeat evaluations')

parser.add_argument('-ncpu', nargs='?',default=4, type=int,
                    help='Number of CPU cores to use')

def average_results(results, dim):
    avg = [0.0 for i in range(dim+1)]
    for r in results:
        for x in range(dim+1):
            avg[x] += r[x]
    return [x/len(results) for x in avg]

if __name__ == '__main__':
    args = parser.parse_args()
    min_func = MinimizationFunctions(func_type=args.f)
    mbog = MBOG(dims=args.d, min_func=min_func.f)
    
    print('\n')
    print(f'MBO Algorithm is starting on function {args.f}...')


    with Pool(processes=args.ncpu) as pool:
        results = pool.map(mbog.run, range(args.n))
    
    avg_r = average_results(results, args.d)

    print(f'Solution found!\n')
    print(f'{avg_r[0]} @ x={avg_r[1:]}\n')
    print('DONE!\n')