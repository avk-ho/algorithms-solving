# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph

# Rectangular graph
# Starting from top left, goal is bottom right
# Cannot move up or left

# First solution
def numberOfWaysToTraverseGraph(width, height):
    def graph_crawl(nb_ways, w, h):
        print(f"width = {w} / height = {h}")
        if w < width:
            graph_crawl(nb_ways, w+1, h)
        if h < height:
            graph_crawl(nb_ways, w, h+1)
        if h == height and w == width:
            nb_ways.append(1)
            print(f"ways = {nb_ways}")
    
    nb_ways = []
    current_w = 1
    current_h = 1
    graph_crawl(nb_ways, current_w, current_h) 
        
    return len(nb_ways)

# use of a list to calculate the answer isn't ideal space-wise
# use of recursion is functional but not optimized time-wise

# w3 * h3
# 1 1 1 / 2 2 X / 3 3 X / 4 X X / 5 X X / 6 X X
# X X 1 / X 2 2 / X 3 X / 4 4 4 / 5 5 X / 6 X X
# X X 1 / X X 2 / X 3 3 / X X 4 / X 5 5 / 6 6 6

# w4 * h4
# 1 1 1 1 / 2 2 2 X / 3 3 3 X / 4 4 4 X
# X X X 1 / X X 2 2 / X X 3 X / X X 4 X
# X X X 1 / X X X 2 / X X 3 3 / X X 4 X
# X X X 1 / X X X 2 / X X X 3 / X X 4 4