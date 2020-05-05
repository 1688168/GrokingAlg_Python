from collections import defaultdict
from collections import deque

def can_construct(originalSeq, sequences):
  result, results = [], []
  # build graph and indegree_tbl
  g = {v: set() for v in originalSeq}
  idt = {v: 0 for v in originalSeq}
  qq=deque()

  for seq in sequences:
      for ii in range(len(seq)-1):
        g[seq[ii]].add(seq[ii+1]) # build Graph, adjacency set
        idt[seq[ii+1]] += 1       # build indegree_tbl

  for k, v in idt.items():
      if v == 0:
          qq.append(k) # find all indegree 0 vertex

  # start Topological sort

  topological_recursive(g, idt, qq, result, results)

  if len(results) == 1 and results[0] == originalSeq:
      print("results: ", results)
      return True
  else:
      print("results: ", results)
      return False


def topological_recursive(g, idt, qq, result, results):
    if not qq:
        if len(result) == len(idt):
            results.append(list(result))
        else:
            print(" not a valid path: ", result)
        return

    for curr_v in qq: # in reality, when we have len(qq) > 1, we can return false, as we are looking for unique solution
        print(" g: ", g, " idt: ", idt, " qq: ", qq, " result: ", result, " results: ", results)

        qq2 = deque(qq)  # clone the qq
        qq2.remove(curr_v)

        result.append(curr_v)

        #update only one indegree table and graph


        for v in g[curr_v]: #update all the indegree for neighbors
            idt[v] -= 1
            if idt[v] == 0:
                qq2.append(v)

        topological_recursive(g, idt, qq2, result, results)

        #restore indegree table and graph
        for v in g[curr_v]:
            idt[v] += 1
        result.pop()





def main():


    print("Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))


    print("Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))

    print("Can construct: " + str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()