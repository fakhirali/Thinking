'''
NOTES

There are premises
There are conclusions that are derived from the premises
The premises may have evidence associated with them.
Or the premises may be derived from other premises.

There are statements.
They can be premises to other statements.
They can be conclusions from other statements.

There could be counterarguments.
Statements that refute other statements.

The app will probably have a graph like structure.
The nodes will be statements.
The edges will be the relationships between the statements.

A decision:
It has a title and description that explains what we are trying
to get at.


'''
import graphviz


class Statement:
    def __init__(self, text):
        self.text = text
        self.supports = []  # these should also be statements
        self.refutes = []

    def __repr__(self):
        return self.text


class Decision:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.statements = []

def make_graph(statements):
    g = graphviz.Digraph('G', filename='hello.gv')
    for s in statements:
        g.node(s.text)
        for c in s.supports:
            g.edge(s.text, c.text)
        for r in s.refutes:
            g.edge(s.text, r.text, color='red')
    return g


if __name__ == '__main__':
    statments = []
    s1 = Statement('all humans are mortal')
    s2 = Statement('socrates is a human')
    s3 = Statement('socrates is mortal')
    s1.supports.append(s3)
    s2.refutes.append(s3)
    statements = [s1, s2, s3]
    graph = make_graph(statements)
    graph.view()
