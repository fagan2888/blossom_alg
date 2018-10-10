# Blossom algorithms 

[![Travis](https://api.travis-ci.org/refraction-ray/blossom_alg.svg)](https://travis-ci.org/refraction-ray/xalpha)
[![codecov](https://codecov.io/gh/refraction-ray/blossom_alg/branch/master/graph/badge.svg)](https://codecov.io/gh/refraction-ray/blossom_alg)

Algorithms for finding matching on undirected graph to achieve max cardinality or max weight.

## Introduction

To find matching of max cardinality,  also known as perfect matching, we ask help for the famous [Edmonds' blossom algorithm](https://en.wikipedia.org/wiki/Blossom_algorithm). For finding matching with max total weight on weighted graph, in Wikipedia, it only says 

>The matching problem can be generalized by assigning weights to edges in *G* and asking for a set *M* that produces a matching of maximum (minimum) total weight. The weighted matching problem can be solved by a combinatorial algorithm that uses the unweighted Edmonds's algorithm as a subroutine.

But the weighted generalization of blossom algorithm is far more challenging than I originally expected. The principle and mechanism behind the algorithm take some time to understand, and the implementation of the ideas with all corner cases isn't an easy task (especially true for me, since I thought it is harder to understand others' implementation than just doing it by myself, so I wrote the code from scratch, only based on the paper even without any pieces of pseudocode). 

## Quick Start

First of all, it is worth noting that this implementation runs in $O(n^2m)$ which is not the optimal speed one can achieve. Therefore, for product use, one can search for other libraries. This work is more educational than practical use.

```python
from blossom import find_perfect_matching
from blossom import find_maximum_matching, find_perfect_maximum_matching
from blossom import UGraph, generate_random_graph, generate_random_graph_w
find_perfect_matching(UGraph([(0,1),(1,2),(2,0)])).edge
# [(0,1)]
find_maximum_matching([(0,1,3),(1,2,2),(2,0,2)]).edge
# [(0,1)]
find_perfect_maximum_matching([(0,1,3),(1,2,2),(2,0,2)]).edge
# [(0,1)]
# this is different from only maximum matching as maximum matching is not necessary a perfect matching
# or one can generate random graphs to use
generate_random_graph(10,0.2)
generate_random_graph_w(10,0.3,100)
```

If one wants to know what is happening step by step within the algorithm, it is easy to configue the log.

```python
import logging
logger = logging.getLogger('blossom')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
```

For more info, read the docstring of relevant APIs. 

## Reference

* [Paths, Trees and Flowers (Edmonds' original work)](https://cms.math.ca/openaccess/cjm/v17/cjm1965v17.0449-0467.pdf)
* [Edmonds' Blossom Algorithm: project report](https://stanford.edu/~rezab/classes/cme323/S16/projects_reports/shoemaker_vare.pdf)
* [Edmond's Blossom Algorithm: demo and explain](https://www-m9.ma.tum.de/graph-algorithms/matchings-blossom-algorithm/index_en.html)
* [Advanced Data Structures and Algorithms](https://www.arl.wustl.edu/~jst/cse/542/)
* [Weighted Matching Lecture](https://theory.stanford.edu/~jvondrak/CS369P/lec6.pdf)
* [Maximum matching implementation](http://jorisvr.nl/article/maximum-matching)
* [Efficient Algorithms for Finding Maximum Matching in Graphs](http://www.cs.kent.edu/~dragan/GraphAn/p23-galil.pdf)