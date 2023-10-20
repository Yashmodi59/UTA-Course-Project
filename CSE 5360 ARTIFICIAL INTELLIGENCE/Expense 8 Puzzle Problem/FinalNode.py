class Node:
    def __init__(self, state, move, cost, depth, hueristic, parent):
        self.state = state
        self.move = move
        self.cost = cost
        self.depth = depth
        self.hueristic = hueristic
        self.parent = parent

    def __lt__(self, other):
        return (self.state, self.hueristic, self.depth, self.move, self.cost) < (
            other.state, other.hueristic, other.depth, other.move, other.cost)

    def __repr__(self):
        return "%s %s %s %s %s %s" % (self.state, self.move, self.cost, self.depth, self.hueristic, self.parent)

    def __str__(self):
        return "< state = %s, action = {%s}, g(n) = %s, d = %s, f(n) = %s, parent = Pointer to -> {%s} >" % (
            self.state, self.move, self.cost, self.depth, self.hueristic, self.parent)