# Monarch Butterfly Optimization

Particle Swarm Optimization (PSO) techniques are based on leveraging the global behavior of a particle cloud to find optimized conditions for a given problem/function. The Monarch Butterfly Optimization (MBO) technique falls in the meta-heuristic algorithms subset of PSOs and has been shown to outperform similar optimization methods such as ABC, ACO, BBO, DE, MBO, and SGA. This is the Python 3.7 implementation of the algorithm which can be found in the article by Gai-Ge Wang [1].



## Getting Started

To get started with using this optimization algorithm, install the prerequisites and follow the installation instructions.

### Prerequisites

Python 3.7
```
>> sudo apt-get install python3.7
```
Numpy 1.17.2
```
>> pip install numpy
```

### Installing

Get a local copy of code

```
git clone https://github.com/justinvzyl/Monarch-Butterfly-Optimization.git
```

## Usage

In the base directory ```../Monarch-Butterfly-Optimization/``` execute:

```
>> python3 mbo.py

<<
MBO Algorithm is starting on function f6...
Solution found!

-0.9850740317638069 @ x=[-1.4966534005938463, -0.8278107736430631]

DONE!

```
For help
```
>> python3 mbo.py -h
<<
usage: mbo.py [-h] [-f [{f6,f7,achley,schwefel,rastrigin}]] [-d [D]] [-n [N]]
              [-ncpu [NCPU]]

Run the MBO algorithm to find a solution to a minimization problem.

optional arguments:
  -h, --help            show this help message and exit
  -f [{f6,f7,achley,schwefel,rastrigin}]
                        Minimization function
  -d [D]                Number of dimensions of the minimization function
  -n [N]                Number of repeat evaluations
  -ncpu [NCPU]          Number of CPU cores to use
```

## Authors

* **Justin van Zyl** - *Python Implementation*

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](https://github.com/justinvzyl/Monarch-Butterfly-Optimization/blob/master/LICENSE) file for details

## Acknowledgments

* Gai-Ge Wang *et al* for their research and development of the MBO algorithm [1].

## Literature

[1] *Wang G., Deb S., Cui Z, Monarch Butterfly Optimization. Neural Comput & Applic 31:1995-2014. doi 10.1007/s00521-015-1923-y*
