import copy
from queue import PriorityQueue, Queue, LifoQueue
from collections import deque
from FinalNode import Node
import FinalUtilty


class Search:
    def __init__(self, start_state, goal_state, dump_flag):
        self.start_state = start_state
        self.goal_state = goal_state
        self.dump_flag = dump_flag

    def helper_function(self, name, max_depth):
        start_state = Node(self.start_state, 0, 0, 0, FinalUtilty.heuristic_expense(self.start_state, self.goal_state),
                           None)
        fringe = []
        closed = []
        nodes_explored = 0
        nodes_generated = 1
        node_poped = 0
        max_fringe_size = 0
        not_all_child_explored = []
        fringe.append(start_state)
        while fringe:
            nod = fringe.pop(-1)
            not_all_child_explored = fringe

            actual_state = nod

            node_poped += 1
            if actual_state.state == self.goal_state:
                solution = FinalUtilty.get_solution_path(actual_state)

                print("Solution path: ")
                for step in solution:
                    print(step)
                print("Nodes expanded: ", nodes_explored)
                print("Nodes Popped: ", node_poped)
                print("Nodes generated: ", nodes_generated)
                print("Max fringe size: ", max_fringe_size)
                print(f"Solution found at depth {actual_state.depth} with cost {actual_state.cost}")
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'Goal node is {nod} \n')
                        f.write(f'Solution Path: \n')
                        for step in solution:
                            f.write(str(step))
                        f.write(f'Nodes expanded: {nodes_explored} \n')
                        f.write(f'Nodes Popped: {node_poped} \n')
                        f.write(f'Nodes generated: {nodes_generated}\n')
                        f.write(f'Max fringe size: {max_fringe_size}\n')
                        f.write(f"Solution found at depth {actual_state.depth} with cost {actual_state.cost}\n")

                return "Result Found"
            else:
                if actual_state.depth == max_depth:
                    closed.append(actual_state.state)
                if actual_state.depth < max_depth:
                    if actual_state.state not in closed:
                        closed.append(actual_state.state)
                        nodes_explored += 1
                        if self.dump_flag:
                            with open(name, 'a') as f:
                                f.write(f'\nGenerating Successor to < :{actual_state} \n')

                        x, y = FinalUtilty.find_pos_of_data(actual_state.state, 0)
                        count_succ = 0
                        neighbourhood_pos = FinalUtilty.get_neighbourhood_pos(x, y)
                        for p, q in neighbourhood_pos:
                            temp_matrix = copy.deepcopy(actual_state.state)
                            g_cost = temp_matrix[p][q]
                            temp_matrix[p][q], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[p][q]
                            action = FinalUtilty.get_move((p, q), (x, y))
                            child_node = Node(temp_matrix, "Move " + str(g_cost) + " " + action,
                                              g_cost,
                                              actual_state.depth + 1, FinalUtilty.heuristic_expense(temp_matrix,
                                                                                                    self.goal_state),
                                              actual_state)
                            nodes_generated += 1
                            count_succ += 1
                            fringe.append(child_node)

                        if self.dump_flag:
                            with open(name, 'a') as f:
                                f.write(f'{count_succ} successors generated \n')
                                cc = ''
                                for i in closed:
                                    cc += str(i) + ", "
                                f.write(f'Closed: {cc} \n')
                                f.write(f'fringe: \n')
                                for v in fringe:
                                    f.write(f'{v} \n')
                    max_fringe_size = max(max_fringe_size,len(fringe))
                    # else:
                    #     while fringe:
                    #         parent_node = actual_state.parent
                    #         if parent_node is None:
                    #             break
                    #         if parent_node in not_all_child_explored:
                    #             fringe.remove(actual_state)
                    #             fringe.append(parent_node)
                    #             actual_state = parent_node
                    #             # break
                    #         actual_state = parent_node

            # if len(fringe) == 0:
            #     print("\n Left traversal Finished \n")
            #     while actual_state.parent is not None:
            #         actual_state = actual_state.parent
            #         if actual_state.state not in closed:
            #             fringe.append(actual_state)
            #             break
            #
            # print("\n Left traversal Finished \n")
            # while actual_state.parent is not None:
            #     actual_state = actual_state.parent
            #     if actual_state.state not in closed:
            #         fringe.append(actual_state)
            #         break

        return "No solution found"

    def uniformCostSearch(self, name):
        fringe = PriorityQueue(0)
        closed = []
        nodes_explored = 0
        nodes_generated = 1
        node_poped = 0
        max_fringe_size = 0

        start_state = Node(self.start_state, 0, 0, 0, FinalUtilty.heuristic_expense(self.start_state, self.goal_state),
                           None)
        fringe.put((start_state.cost, start_state))

        while True:
            actual_state = fringe.get()[1]
            node_poped += 1
            if actual_state.state == self.goal_state:
                solution = FinalUtilty.get_solution_path(actual_state)

                print("Solution path: ")
                for step in solution:
                    print(step)
                print("Nodes expanded: ", nodes_explored)
                print("Nodes Popped: ", node_poped)
                print("Nodes generated: ", nodes_generated)
                print("Max fringe size: ", max_fringe_size)
                print(f"Solution found at depth {actual_state.depth} with cost {actual_state.cost}")
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'\n Goal node is {fringe.get()} \n')
                        f.write(f'Solution Path: \n')
                        for step in solution:
                            f.write(str(step))
                        f.write(f'Nodes expanded: {nodes_explored} \n')
                        f.write(f'Nodes Popped: {node_poped} \n')
                        f.write(f'Nodes generated: {nodes_generated} \n')
                        f.write(f'Max fringe size: {max_fringe_size} \n')

                return
            elif actual_state.state not in closed:
                closed.append(actual_state.state)
                nodes_explored += 1
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'\n Generating Successor to < :{actual_state} \n')

                x, y = FinalUtilty.find_pos_of_data(actual_state.state, 0)
                count_succ = 0
                neighbourhood_pos = FinalUtilty.get_neighbourhood_pos(x, y)
                for p, q in neighbourhood_pos:
                    temp_matrix = copy.deepcopy(actual_state.state)
                    g_cost = temp_matrix[p][q]
                    temp_matrix[p][q], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[p][q]
                    action = FinalUtilty.get_move((p, q), (x, y))
                    count_succ += 1
                    child_node = Node(temp_matrix, "Move " + str(g_cost) + " " + action, actual_state.cost + g_cost,
                                      actual_state.depth + 1, FinalUtilty.heuristic_expense(temp_matrix,
                                                                                            self.goal_state),
                                      actual_state)
                    nodes_generated += 1
                    fringe.put((child_node.cost, child_node))

                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'{count_succ} successors generated \n')
                        cc = ''
                        for i in closed:
                            cc += str(i)
                        f.write(f'Closed: {cc} \n')
                        f.write(f'fringe: \n')
                        for v in fringe.queue:
                            f.write(f'{v} \n')
                max_fringe_size = max(max_fringe_size, fringe.qsize())
        return None

    def breadthFirstSearch(self, name):
        fringe = Queue()
        closed = []
        nodes_explored = 0
        nodes_generated = 1
        node_poped = 0
        max_fringe_size = 0

        start_state = Node(self.start_state, 0, 0, 0, FinalUtilty.heuristic_expense(self.start_state, self.goal_state),
                           None)
        fringe.put(start_state)
        while not fringe.empty():
            actual_state = fringe.get()
            node_poped += 1
            if actual_state.state == self.goal_state:
                solution = FinalUtilty.get_solution_path(actual_state)

                print("Solution path: ")
                for step in solution:
                    print(step)
                print("Nodes expanded: ", nodes_explored)
                print("Nodes Popped: ", node_poped)
                print("Nodes generated: ", nodes_generated)
                print("Max fringe size: ", max_fringe_size)
                print(f"Solution found at depth {actual_state.depth} with cost {actual_state.cost}")
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'Goal node is {fringe.get()} \n')
                        f.write(f'Solution Path:')
                        for step in solution:
                            f.write(str(step))
                        f.write(f'Nodes expanded: {nodes_explored}')
                        f.write(f'Nodes Popped: {node_poped}')
                        f.write(f'Nodes generated: {nodes_generated}')
                        f.write(f'Max fringe size: {max_fringe_size}')

                return
            else:
                if actual_state.state not in closed:
                    closed.append(actual_state.state)
                    nodes_explored += 1
                    if self.dump_flag:
                        with open(name, 'a') as f:
                            f.write(f'Generating Successor to < :{actual_state} \n')

                    x, y = FinalUtilty.find_pos_of_data(actual_state.state, 0)
                    count_succ = 0
                    neighbourhood_pos = FinalUtilty.get_neighbourhood_pos(x, y)
                    for p, q in neighbourhood_pos:
                        temp_matrix = copy.deepcopy(actual_state.state)
                        g_cost = temp_matrix[p][q]
                        temp_matrix[p][q], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[p][q]
                        action = FinalUtilty.get_move((p, q), (x, y))
                        count_succ += 1
                        nodes_generated += 1
                        child_node = Node(temp_matrix, "Move " + str(g_cost) + " " + action, g_cost,
                                          actual_state.depth + 1, FinalUtilty.heuristic_expense(temp_matrix,
                                                                                                self.goal_state),
                                          actual_state)
                        if child_node.state not in fringe.queue:
                            fringe.put(child_node)

                    if self.dump_flag:
                        with open(name, 'a') as f:
                            f.write(f'{count_succ} successors generated \n')
                            cc = ''
                            for i in closed:
                                cc += str(i)
                            f.write(f'Closed: {cc} \n')
                            f.write(f'fringe: \n')

                            for v in fringe.queue:
                                f.write(f'{v} \n')
                    max_fringe_size = max(max_fringe_size, fringe.qsize())
        return None

    def iteratingDeepeningSearch(self, name):
        max_depth = 1
        result = "No solution found"
        while result == "No solution found":
            if self.dump_flag:
                with open(name, 'a') as f:
                    f.write(f'\n Max Depth = {max_depth} Reached \n')
            print("Max Depth: ", max_depth)
            result = self.helper_function(name, max_depth)
            if result == "Result found":
                print("Result found")
                break
            max_depth += 1
        return

    def depthFirstSearch(self, name):
        start_state = Node(self.start_state, 0, 0, 0, FinalUtilty.heuristic_expense(self.start_state, self.goal_state),
                           None)
        fringe = []
        closed = []
        nodes_explored = 0
        nodes_generated = 1
        node_poped = 0
        max_fringe_size = 0
        not_all_child_explored = []
        fringe.append(start_state)
        while fringe:
            nod = fringe.pop(-1)
            actual_state = nod
            not_all_child_explored = fringe
            node_poped += 1
            if actual_state.state == self.goal_state:
                solution = FinalUtilty.get_solution_path(actual_state)

                print("Solution path: ")
                for step in solution:
                    print(step)
                print("Nodes expanded: ", nodes_explored)
                print("Nodes Popped: ", node_poped)
                print("Nodes generated: ", nodes_generated)
                print("Max fringe size: ", max_fringe_size)
                print(f"Solution found at depth {actual_state.depth} with cost {actual_state.cost}")
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'Goal node is {nod} \n')
                        f.write(f'Solution Path:')
                        for step in solution:
                            f.write(str(step))
                        f.write(f'Nodes expanded: {nodes_explored} \n')
                        f.write(f'Nodes Popped: {node_poped} \n')
                        f.write(f'Nodes generated: {nodes_generated} \n')
                        f.write(f'Max fringe size: {max_fringe_size} \n')

                return
            else:
                if actual_state.state not in closed:
                    closed.append(actual_state.state)
                    nodes_explored += 1
                    if self.dump_flag:
                        with open(name, 'a') as f:
                            f.write(f'\nGenerating Successor to < :{nod} \n')

                    x, y = FinalUtilty.find_pos_of_data(actual_state.state, 0)
                    count_succ = 0
                    neighbourhood_pos = FinalUtilty.get_neighbourhood_pos(x, y)
                    for p, q in neighbourhood_pos:
                        temp_matrix = copy.deepcopy(actual_state.state)
                        g_cost = temp_matrix[p][q]
                        temp_matrix[p][q], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[p][q]
                        action = FinalUtilty.get_move((p, q), (x, y))
                        count_succ += 1
                        child_node = Node(temp_matrix, "Move " + str(g_cost) + " " + action, g_cost,
                                          actual_state.depth + 1, FinalUtilty.heuristic_expense(temp_matrix,
                                                                                                self.goal_state),
                                          actual_state)
                        nodes_generated += 1
                        fringe.append(child_node)

                    if self.dump_flag:
                        with open(name, 'a') as f:
                            f.write(f'{count_succ} successors generated \n')
                            cc = ''
                            for i in closed:
                                cc += str(i) + ', '
                            f.write(f'Closed: {cc} \n')
                            f.write(f'fringe: \n')
                            for v in fringe:
                                f.write(f'{v} \n')
            #     else:
            #         # Backtracking
            #         while fringe:
            #             parent_node = actual_state.parent
            #             if parent_node is None:
            #                 break
            #             if parent_node in not_all_child_explored:
            #                 fringe.remove(actual_state)
            #                 fringe.append(parent_node)
            #                 actual_state = parent_node
            #                 break
            #             actual_state = parent_node
            #
            # if len(fringe) == 0:
            #     print("\n Left traversal Finished \n")
            #     while actual_state.parent is not None:
            #         actual_state = actual_state.parent
            #         if actual_state.state not in closed:
            #             fringe.append(actual_state)
            #             break
        return None

    def depthLimitedSearch(self, name):
        max_depth = int(input("Please Enter the depth limit:"))
        if self.dump_flag:
            with open(name, 'a') as f:
                f.write(f'\n Depth Limit Search for depth = {max_depth} \n')

        result = self.helper_function(name, max_depth)
        print(result)

        return

    def greedySearch(self, name):
        fringe = PriorityQueue(0)
        closed = []
        nodes_explored = 0
        nodes_generated = 1
        node_poped = 0
        max_fringe_size = 0

        start_state = Node(self.start_state, 0, 0, 0, FinalUtilty.heuristic_expense(self.start_state, self.goal_state),
                           None)
        fringe.put((start_state.cost, start_state))

        while True:
            actual_state = fringe.get()[1]
            node_poped += 1
            if actual_state.state == self.goal_state:
                solution = FinalUtilty.get_solution_path(actual_state)

                print("Solution path: ")
                for step in solution:
                    print(step)
                print("Nodes expanded: ", nodes_explored)
                print("Nodes Popped: ", node_poped)
                print("Nodes generated: ", nodes_generated)
                print("Max fringe size: ", max_fringe_size)
                print(f"Solution found at depth {actual_state.depth} with cost {actual_state.parent.hueristic}")
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'Goal node is {fringe.get()} \n')
                        f.write(f'Solution Path:\n')
                        for step in solution:
                            f.write(str(step) + "\n")
                        f.write(f'Nodes expanded: {nodes_explored}' + "\n")
                        f.write(f'Nodes Popped: {node_poped}' + "\n")
                        f.write(f'Nodes generated: {nodes_generated}' + "\n")
                        f.write(f'Max fringe size: {max_fringe_size}' + "\n")

                return
            elif actual_state.state not in closed:
                closed.append(actual_state.state)
                nodes_explored += 1
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'\n Generating Successor to < :{actual_state} \n')

                x, y = FinalUtilty.find_pos_of_data(actual_state.state, 0)
                count_succ = 0
                neighbourhood_pos = FinalUtilty.get_neighbourhood_pos(x, y)
                for p, q in neighbourhood_pos:
                    nodes_generated += 1
                    temp_matrix = copy.deepcopy(actual_state.state)
                    g_cost = temp_matrix[p][q]
                    temp_matrix[p][q], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[p][q]
                    action = FinalUtilty.get_move((p, q), (x, y))
                    count_succ += 1
                    child_node = Node(temp_matrix, "Move " + str(g_cost) + " " + action, g_cost,
                                      actual_state.depth + 1,
                                      FinalUtilty.heuristic_expense(temp_matrix, self.goal_state),
                                      actual_state)
                    fringe.put((FinalUtilty.heuristic_expense(temp_matrix, self.goal_state), child_node))

                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'\n {count_succ} successors generated \n')
                        cc = ''
                        for i in closed:
                            cc += str(i)
                        f.write(f'Closed: {cc} \n')
                        for v in fringe.queue:
                            f.write(f'fringe: {v} \n')
                max_fringe_size = max(max_fringe_size, fringe.qsize())
        return None

    def aStarSearch(self, name):
        fringe = PriorityQueue(0)
        closed = []
        nodes_explored = 0
        nodes_generated = 1
        node_poped = 0
        max_fringe_size = 0

        start_state = Node(self.start_state, 0, 0, 0, FinalUtilty.heuristic_expense(self.start_state, self.goal_state),
                           None)
        fringe.put((start_state.hueristic, start_state))

        while True:
            actual_state = fringe.get()[1]
            node_poped += 1
            if actual_state.state == self.goal_state:
                solution = FinalUtilty.get_solution_path(actual_state)

                print("Solution path: ")
                for step in solution:
                    print(step)
                print("Nodes expanded: ", nodes_explored)
                print("Nodes Popped: ", node_poped)
                print("Nodes generated: ", nodes_generated)
                print("Max fringe size: ", max_fringe_size)
                print(f"Solution found at depth {actual_state.depth} with cost {actual_state.cost}")
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'Goal node is {fringe.get()} \n')
                        f.write(f'Solution Path:')
                        for step in solution:
                            f.write(str(step))
                        f.write(f'Nodes expanded: {nodes_explored}\n')
                        f.write(f'Nodes Popped: {node_poped}\n')
                        f.write(f'Nodes generated: {nodes_generated}\n')
                        f.write(f'Max fringe size: {max_fringe_size}\n')

                return
            elif actual_state.state not in closed:
                closed.append(actual_state.state)
                nodes_explored += 1
                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'\n Generating Successor to < :{actual_state} \n')

                x, y = FinalUtilty.find_pos_of_data(actual_state.state, 0)
                count_succ = 0
                neighbourhood_pos = FinalUtilty.get_neighbourhood_pos(x, y)
                for p, q in neighbourhood_pos:
                    nodes_generated += 1
                    temp_matrix = copy.deepcopy(actual_state.state)
                    g_cost = temp_matrix[p][q]
                    temp_matrix[p][q], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[p][q]
                    action = FinalUtilty.get_move((p, q), (x, y))
                    count_succ += 1
                    child_node = Node(temp_matrix, "Move " + str(g_cost) + " " + action, actual_state.cost + g_cost,
                                      actual_state.depth + 1, FinalUtilty.heuristic_expense(temp_matrix,
                                                                                            self.goal_state) + g_cost + actual_state.cost,
                                      actual_state)
                    fringe.put((child_node.hueristic, child_node))

                if self.dump_flag:
                    with open(name, 'a') as f:
                        f.write(f'\n {count_succ} successors generated \n')
                        cc = ''
                        for i in closed:
                            cc += str(i)
                        f.write(f'Closed: {cc} \n')
                        f.write(f'fringe: \n')
                        for v in fringe.queue:
                            f.write(f'{v} \n')
                max_fringe_size = max(max_fringe_size, fringe.qsize())
        return None
