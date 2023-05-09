import heapq

def astar(start, goal, h_func, successors_func):
    
    start_g = 0
    start_h = h_func(start)
    start_f = start_g + start_h
    start_node = (start_f, start_g, start)
    
    open_list = [start_node]
    closed_set = set()
    came_from = {}
    
    while open_list:
        current_node = heapq.heappop(open_list)[2]
        
        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path
        
        closed_set.add(current_node)
        
        successors = successors_func(current_node)
        
        for successor in successors:
            if successor in closed_set:
                continue
            
            tentative_g = start_g + 1
            
            in_open_list = False
            for node in open_list:
                if successor == node[2]:
                    in_open_list = True
                    break
            
            if not in_open_list:
                successor_g = tentative_g
                successor_h = h_func(successor)
                successor_f = successor_g + successor_h
                heapq.heappush(open_list, (successor_f, successor_g, successor))
            
    return None
