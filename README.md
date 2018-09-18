# Blossom algorithms 

[![Travis](https://api.travis-ci.org/refraction-ray/blossom_alg.svg)](https://travis-ci.org/refraction-ray/xalpha)
[![codecov](https://codecov.io/gh/refraction-ray/blossom_alg/branch/master/graph/badge.svg)](https://codecov.io/gh/refraction-ray/blossom_alg)

Algorithms for finding matching on undirected graph to achieve max cardinality or max weight.

## Introduction

To find matching of max cardinality,  also known as perfect matching, we ask help for the famous [Edmonds' blossom algorithm](https://en.wikipedia.org/wiki/Blossom_algorithm). For finding matching with max total weight on weighted graph, in Wikipedia, it only says 

>The matching problem can be generalized by assigning weights to edges in *G* and asking for a set *M* that produces a matching of maximum (minimum) total weight. The weighted matching problem can be solved by a combinatorial algorithm that uses the unweighted Edmonds's algorithm as a subroutine.

But the weighted generalization of blossom algorithm is far more challenging than I originally expected. The principle and mechanism behind the algorithm take some time to understand, and the implementation of the ideas with all corner cases isn't an easy task (especially true for me, since I thought it is harder to understand others' implementation than just doing it by myself, so I wrote the code from scratch, only based on the paper even without any pieces of pseudocode). 

## Reference

* [Paths, Trees and Flowers (Edmonds' original work)](https://cms.math.ca/openaccess/cjm/v17/cjm1965v17.0449-0467.pdf)
* [Edmonds' Blossom Algorithm: project report](https://stanford.edu/~rezab/classes/cme323/S16/projects_reports/shoemaker_vare.pdf)
* [Edmond's Blossom Algorithm: demo and explain](https://www-m9.ma.tum.de/graph-algorithms/matchings-blossom-algorithm/index_en.html)
* [Advanced Data Structures and Algorithms](https://www.arl.wustl.edu/~jst/cse/542/)
* [Weighted Matching Lecture](https://theory.stanford.edu/~jvondrak/CS369P/lec6.pdf)
* [Maximum matching implementation](http://jorisvr.nl/article/maximum-matching)
* [Efficient Algorithms for Finding Maximum Matching in Graphs](http://www.cs.kent.edu/~dragan/GraphAn/p23-galil.pdf)