import sys
sys.path.insert(0, "../")

from blossom import find_perfect_matching
from blossom import find_maximum_matching
from blossom import UGraph, generate_random_graph, generate_random_graph_w

test_uwgraph = []
test_uwgraph.append( [(0,1),(1,2),(0,2),(4,1),(1,3),(4,3),(3,6),(5,3),(5,6),(5,9),(9,12),(12,11),(11,10),(2,7),(7,8)] )
test_uwgraph.append( [(0,1),(1,2),(0,2),(1,3),(2,4)] )
test_uwgraph.append( [(0, 7),(0, 14),(1, 7),(1, 13),(2, 5),(2, 7),(2, 8),(2, 11),(2, 13),(3, 5),(3, 11),(3, 14),(5, 8),
                      (5, 11),(5, 13),(6, 7),(11, 12),(11, 13)] )

test_wgraph = []
answer_graph = []
test_wgraph.append([])
answer_graph.append([])
test_wgraph.append( [(0,1,1)] )
answer_graph.append([(0,1)])
test_wgraph.append( [(0,1,8),(1,2,0),(2,3,8),(3,4,9),(4,0,8)] )
answer_graph.append( [(3, 4), (0, 1)] )
test_wgraph.append( [(1,2,3.1), (2,3,2.7), (1,3,3.0), (1,4,1.4) ] )
answer_graph.append( [(1,4),(2,3)] )
test_wgraph.append( [(1,2,2), (1,3,-2), (2,3,1), (2,4,-1), (3,4,-6)] )
answer_graph.append( [(1,2)] )
test_wgraph.append( [ (1,2,19), (1,3,20), (1,8,8), (2,3,25), (2,4,18), (3,5,18), (4,5,13), (4,7,7), (5,6,7) ] )
answer_graph.append( [(5, 6), (4, 7), (1, 8), (2, 3)] )
test_wgraph.append( [ (1,2,45), (1,5,45), (2,3,50), (3,4,45), (4,5,50), (1,6,30), (3,9,35), (4,8,35), (5,7,26), (9,10,5) ] )
answer_graph.append( [(1, 6), (2, 3), (4, 8), (5, 7), (9, 10)] )
test_wgraph.append( [ (1,2,8), (1,3,9), (2,3,10), (3,4,7), (1,6,5), (4,5,6) ] )
answer_graph.append( [(4, 5), (1, 6), (2, 3)] )
test_wgraph.append( [ (1,2,9), (1,3,8), (2,3,10), (1,4,5), (4,5,3), (3,6,4) ] )
answer_graph.append( [(4, 5), (3, 6), (1, 2)] )
test_wgraph.append( [(5,7,13),(5,1,10),(1,7,20.5),(1,2,17),(1,0,9),(0,2,15),(2,3,8),(2,6,10),(3,6,13),(5,11,2)] )
answer_graph.append( [(0, 2), (3, 6), (5, 11), (1, 7)] )
test_wgraph.append( [(0,1,8),(0,2,5),(1,2,10),(0,4,10),(3,4,10),(6,4,7),(5,6,10),(1,5,8),(1,3,5),(2,3,9)] )
answer_graph.append( [(5, 6), (1, 2), (0, 4)] )
test_wgraph.append( [(0,1,10),(1,2,7),(1,3,8),(2,3,9),(2,4,8),(4,6,7),(6,7,8),(5,6,11),(1,5,5)] )
answer_graph.append( [(5, 6), (0, 1), (2, 3)] )

def correct_check(graph, match, remain = None):
    if remain is None:
        if len(graph.vertex) %2 == 0:
            remain = 0
        else:
            remain = 1

    for e in match.edge:
        assert e in graph.edge
    assert len(match.edge) == (len(graph.vertex) - remain)/2

def test_uw():
    for ug in test_uwgraph:
        match = find_perfect_matching(UGraph(ug))
        correct_check(UGraph(ug), match)
    random_uwgraph = []
    for i in range(30):
        random_uwgraph.append(generate_random_graph(37, density=0.12))
        find_perfect_matching(random_uwgraph[i])

def test_w():
    for i in range(len(test_wgraph)):
        assert set(find_maximum_matching(test_wgraph[i],debug = True).edge) == set(answer_graph[i])
    random_wgraph = []
    for i in range(30):
        random_wgraph.append(generate_random_graph_w(33, density=0.23, window=11))
        find_maximum_matching(random_wgraph[i].rep, debug = True)
