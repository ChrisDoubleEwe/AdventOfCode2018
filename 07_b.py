import re

with open("07_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

tasks = []
depends = dict()
done = dict()

for row in content:
  task = row
  task=(row.split(' '))[1]
  dependency=(row.split(' '))[7]
  tasks.append(task)
  tasks.append(dependency)
  done[task] = 0
  done[dependency] = 0

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
#print "Tasks: " + str(tasks)
#print "Depends: " + str(depends)
#print "Done: " + str(done)

# Go through tasks to work out order
task_order = ''

# START DOING WORK
seconds = -1
workers = []
num_workers = 5
for w in range(0,num_workers):
  worker = []
  workers.append(worker)
#print "Workers: " + str(workers)

def finish(do_task):
  # TASK IS NOW DONE
  tasks.remove(do_task)
  # Remove done tasks from other tasks dependencies
  done[do_task] = 2
  for task in tasks:
    deps = depends[task]
    if deps != None:
      if do_task in deps:
        deps.remove(do_task)
        depends[task] = deps

 
while True:
  #print "START ITERATION"
  #print "Done: " + str(done)
  #print "Tasks: " + str(tasks)


  seconds += 1

  # Which tasks can be done?
  available_tasks = []
  for task in tasks:
    if done[task] == 0:
      if depends[task] == None:
        #print "TASK xxx" + task + " CAN BE DONE"
        available_tasks.append(task)
      else:
        if len(depends[task]) == 0:
          #print "TASK " + task + " CAN BE DONE"
          available_tasks.append(task)

  
  #Sort alphabetically
  available_tasks = sorted(set(available_tasks))

  # Assign tasks to workers
  #print "Available tasks: " + str(available_tasks)
  #print "Workers " + str(workers)
  for w in range(0,num_workers):
    if workers[w] == []:
      if available_tasks != []:
        assign_task = available_tasks[0]
        #print "  Assigning task " + assign_task + " to worker " + str(w)
        work = []
        task_number = ord(assign_task) - 64 + 60
        #print "    TASK NUMBER = " + str(task_number)
        for i in range(0, task_number):
          work.append(assign_task)
        workers[w] = work
        available_tasks = available_tasks[1:]
        done[assign_task] = 1

  # Any workers that are currently working, do work:
  #print "Workers " + str(workers)
  print str(seconds) + "    ",
  for w in range(0,num_workers):
    if workers[w] != []:
      task_list = workers[w]
      this_task = task_list.pop(0)
      if task_list == []:
        finish(this_task)
      print this_task + "     ",
    else:
      print ".     ",
  print " "

  # When all tasks are done, stop
  all_done = 1
  for x in done.keys():
    if done[x] != 2:
      all_done = 0
  if all_done == 1:
    print str(seconds+1) + "    ",
    for w in range(0,num_workers):
      if workers[w] != []:
        task_list = workers[w]
        this_task = task_list.pop(0)
        if task_list == []:
          finish(this_task)
        print this_task + "     ",
      else:
        print ".     ",
    print " "
    exit()
