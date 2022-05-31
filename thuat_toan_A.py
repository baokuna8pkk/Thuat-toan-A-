def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node) 
        closed_set = set()
        g = {} # luu khoang cach tu nut bat dau
        parents = {}
 
        #khoang cach tu nut bat dau den chinh no bang 0
        g[start_node] = 0
        #start_node la nut goc khong co nut cha
        #start_node duoc dat la nut cha chinh no
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None
 
            # nut co f() thap nhat
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    # nut 'm' khong co trong first va last add vao first
                    # n dat la cha cua m
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                         
     
                    # voi moi nut  m, so sanh khoang cach cua no tu diem bat dau (g(m))
                    # tu diem dau den nut n
                    else:
                        if g[m] > g[n] + weight:
                            # update g(m)
                            g[m] = g[n] + weight
                            # change parent of m to n
                            parents[m] = n
                             
                            #neu m in closed , xoa va add vao open
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # neu nut hien tai la stop_node
            # tao lai duong di tu no den start_node
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
 
 
            # xoa n khoi open_list, va add no vao closed_list
            # boi vi tat ca hang xom cua n deu da kiem tra
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None
         
#tra ve hang xom va khoang cach cua no
#tu nut da qua
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
#xem set khoang cach heuristic da cho
#ham tra ve khoang cach heuristic cho tat ca cac nut
def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
             
        }
 
        return H_dist[n]
 
#cac gia tri g(x)
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
aStarAlgo('A', 'G')