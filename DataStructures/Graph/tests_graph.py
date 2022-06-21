from graph import Graph


graph = Graph([('A', 'B'), ('B', 'C'), ('B', 'D'),
              ('C', 'D'), ('E', 'F'), ('F', 'C')])

assert graph.find_path('A', 'C') == [
    'A', 'B', 'C'], "Should be ['A', 'B', 'C']"

graph.add('A', 'D')
assert graph.is_connected('A', 'D')

graph.remove('D')
assert not graph.is_connected('A', 'D')
