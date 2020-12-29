from datetime import datetime

import numpy as np
import parse

# Parse data
times, events = [], []
with open("04_a_input.txt") as infile:
    for line in infile.readlines():
        time, event = parse.parse("[{}] {}", line)
        dt = datetime.strptime(time, '%Y-%m-%d %H:%M')
        times.append(dt)
        events.append(event)

# Sort data
times, events = map(list, zip(*sorted(zip(times, events))))

# Calculate number of times each guard is asleep each minute
guard_sleeps = {}
current_guard_id = None
current_asleep_time = None
for time, event in zip(times, events):
    guard_id = parse.parse("Guard #{} begins shift", event)
    if guard_id is not None:
        current_guard_id, = guard_id
        current_guard_id = int(current_guard_id)
    elif event == "falls asleep":
        current_asleep_time = time
    elif event == "wakes up":
        wakeup_minute = time.minute
        asleep_minute = current_asleep_time.minute
        guard_sleep = np.array(60)
        guard_sleep[asleep_minute:wakeup_minute] = 1
        if current_guard_id in guard_sleeps:
            guard_sleeps[current_guard_id] += guard_sleep
        else:
            guard_sleeps[current_guard_id] = guard_sleep

# Strategy 1
max_sleep_sum = 0
max_sleep = None
sleepy_guard_id = None
for guard_id, sleeps in guard_sleeps.items():
    if sum(sleeps) > max_sleep_sum:
        max_sleep_sum = sum(sleeps)
        max_sleep = sleeps
        sleepy_guard_id = guard_id
print(sleepy_guard_id * np.argmax(max_sleep))

# Strategy 2
max_sleep_for_minute = 0
sleepy_minute = None
sleepy_guard_id = None
for guard_id, sleeps in guard_sleeps.items():
    minute = np.argmax(sleeps)
    sleep_for_minute = sleeps[minute]
    if sleep_for_minute > max_sleep_for_minute:
        max_sleep_for_minute = sleep_for_minute
        sleepy_minute = minute
        sleepy_guard_id = guard_id
print(sleepy_guard_id * sleepy_minute)

