import sys
import unittest
import queue
import time
import resource


class Node(object):

    def __init__(self, path_to_node, search_depth, current_state, parent_node):
        self.path_to_node = path_to_node
        self.search_depth = search_depth
        self.current_state = current_state
        self.parent_node = parent_node


    def is_goal(self):
        return self.current_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]


    def queue_child_nodes(self, states, search, que, max_depth):
        # Can empty space be moved
        moves = []
        original_zero_index = self.current_state.index(0)
        original_state = list(self.current_state)
        expanded_any = False
        if original_zero_index > 2:
            up_node = Node('Up', self.search_depth + 1, list((original_state)), self)
            up_node.current_state[original_zero_index], up_node.current_state[original_zero_index - 3] = up_node.current_state[original_zero_index - 3], up_node.current_state[original_zero_index]
            if tuple(up_node.current_state) not in states: 
                moves.append(up_node)
                expanded_any = True

        if original_zero_index < 6:
            down_node = Node('Down', self.search_depth + 1, list((original_state)), self)
            down_node.current_state[original_zero_index], down_node.current_state[original_zero_index + 3] = down_node.current_state[original_zero_index + 3], down_node.current_state[original_zero_index]
            if tuple(down_node.current_state) not in states: 
                moves.append(down_node)
                expanded_any = True
                

        if original_zero_index not in [0,3,6]:
            left_node = Node('Left', self.search_depth + 1, list((original_state)), self)
            left_node.current_state[original_zero_index], left_node.current_state[original_zero_index - 1] = left_node.current_state[original_zero_index - 1], left_node.current_state[original_zero_index]
            if tuple(left_node.current_state) not in states: 
                moves.append(left_node)
                expanded_any = True

        if original_zero_index not in [2,5,8]:
            right_node = Node('Right', self.search_depth + 1, list((original_state)), self)
            right_node.current_state[original_zero_index], right_node.current_state[original_zero_index + 1] = right_node.current_state[original_zero_index + 1], right_node.current_state[original_zero_index]
            if tuple(right_node.current_state) not in states: 
                moves.append(right_node)
                expanded_any = True


        if search == 'bfs':
            for nod in moves:
                que.put(nod)
                states.add(tuple(nod.current_state))

        elif search == 'dfs':
            for nod in moves[::-1]:
                que.put(nod)
                states.add(tuple(nod.current_state))


        if self.search_depth == max_depth:
            if expanded_any:
                max_depth += 1

        return states, que, max_depth

def find_path(node, liss):

    while node.parent_node != None:
        liss.append(node.path_to_node)
        node = node.parent_node
    liss = list(liss[::-1])
    return liss


def main():
    start_time = time.time()
    SEARCH_TYPE = str(sys.argv[1])
    argument = str(sys.argv[2])
    INITIAL_STATE = []
    for c in argument:
        if c == ',':
            pass
        else:
            INITIAL_STATE.append(int(c))
    
    explored_and_frontier_states = set()
    expanded_nodes = 0
    maximum_search_depth = 0
    explored_and_frontier_states.add(tuple(INITIAL_STATE))

    if SEARCH_TYPE == 'bfs':
        frontier = queue.Queue()
        frontier.put(Node([], 0, INITIAL_STATE, None))
        while not frontier.empty():
            current_node = frontier.get()
            if current_node.is_goal():
                output_file = open('output.txt', 'w')
                output_file.write('path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nmax_search_depth: {}\nrunning_time: {}\nmax_ram_usage: {}'.format(find_path(current_node, []), len(find_path(current_node, [])), expanded_nodes, current_node.search_depth, maximum_search_depth, time.time()-start_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0))
                output_file.close()
                sys.exit()

            expanded_nodes += 1
            explored_and_frontier_states, frontier, maximum_search_depth = current_node.queue_child_nodes(explored_and_frontier_states, 'bfs', frontier, maximum_search_depth)

    elif SEARCH_TYPE == 'dfs':
        frontier = queue.LifoQueue()
        frontier.put(Node([], 0, INITIAL_STATE, None))
        while not frontier.empty():
            current_node = frontier.get()

            if current_node.is_goal(): 
                output_file = open('output.txt', 'w')
                output_file.write('path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nmax_search_depth: {}\nrunning_time: {}\nmax_ram_usage: {}'.format(find_path(current_node, []), len(find_path(current_node, [])), expanded_nodes, current_node.search_depth, maximum_search_depth, time.time()-start_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0))
                output_file.close()
                sys.exit()

            expanded_nodes += 1

            explored_and_frontier_states, frontier, maximum_search_depth = current_node.queue_child_nodes(explored_and_frontier_states, 'dfs', frontier, maximum_search_depth)



            


    else:
        pass     


if __name__ == '__main__':
    #unittest.main()
    main()