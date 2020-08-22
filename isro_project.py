cache = {}

def total_value(missions, max_budget):
  return sum([x[2] for x in missions]) if sum([x[1] for x in missions]) <= max_budget else 0

def select_missions(missions, max_budget):
  if not missions:
    return ()
  if (missions, max_budget) not in cache:
    head = missions[0]
    tail = missions[1:]
    select = (head,) + select_missions(tail, max_budget - head[1])
    unselect = select_missions(tail, max_budget)
    if total_value(select, max_budget) > total_value(unselect, max_budget):
      solution = select
    else:
      solution = unselect
    cache[(missions, max_budget)] = solution
  return cache[(missions, max_budget)]

def read_file(name="inputPS2.txt"):
  f = open(name, "r")
  projectList = []
  for line in f:
    project = line.split("/")
    projectList.append((project[0].strip(), int(project[1].strip()), int(project[2].strip())))
  f.close()
  return projectList

def write_output(solution, max_budget, fileName="outputPS2.txt"):
  f = open(fileName, "w")
  f.write("The mission that should be funded : " + ','.join(str(s[0]) for s in solution) + "\n")
  f.write("Total value : " + str(total_value(solution, max_budget)) + "\n")
  f.write("Budget remaining : " + str((100 - sum([x[1] for x in solution]))))
  f.close()

if __name__ == '__main__':
  projects = read_file("inputPS2.txt")
  max_budget = 100
  selection = select_missions(tuple(projects), max_budget)
  write_output(selection, max_budget, "outputPS2.txt")
