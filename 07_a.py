import re

with open("07_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

tasks = []
depends = dict()
done = dict()

for row in content:
  print row
  task = row
  task=(row.split(' '))[1]
  dependency=(row.split(' '))[7]
  print task + " -> " + dependency
  tasks.append(task)
  tasks.append(dependency)
  done[task] = 0
  if dependency in depends:
    current_depends = depends[dependency]
    current_depends.append(task)
    depends[dependency] = current_depends
  else:
    current_depends = []
    current_depends.append(task)
    depends[dependency] = current_depends
  if task in depends:
    dummy = 1
  else:
    depends[task] = []

tasks = sorted(set(tasks))
print tasks
print depends
print done

# Go through tasks to work out order
task_order = ''

while True:
  print "Start iteration"
  print tasks
  print depends
  print done
  # Which tasks can be done?
  available_tasks = []
  for task in tasks:
    print "Checking whether task can be done: " + task
    if depends[task] == None:
      print "TASK xxx" + task + " CAN BE DONE"
      available_tasks.append(task)
    else:
      if len(depends[task]) == 0:
        print "TASK " + task + " CAN BE DONE"
        available_tasks.append(task)

  #Sort alphabetically
  available_tasks = sorted(set(available_tasks))

  if len(available_tasks) == 0:
    print "Finished"
    print task_order
    exit()

  do_task = available_tasks[0]
  print "Doing task " + do_task
  task_order = task_order + do_task
  tasks.remove(do_task)

  # Remove done tasks from other tasks dependencies
  done[do_task] = 1
  for task in tasks:
    deps = depends[task]
    if deps != None:
      if do_task in deps:
        print "  Dependencies for task " + task + " : " + str(deps)
        deps.remove(do_task)
        print "  New dependencies for task " + task + " : " + str(deps)
        depends[task] = deps
  
