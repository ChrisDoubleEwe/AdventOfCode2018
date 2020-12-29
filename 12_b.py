with open('12_a_input.txt') as puzzle_file:
    initial = puzzle_file.readline()[15:-1]
    mappings = dict(line.strip().split(' => ') for line in puzzle_file if line.strip())

def recenter(offset, state):
    l = state.find('#')
    return (0, '') if l < 0 else (offset + l, state[l:state.rfind('#', l) + 1])

def step(offset, state):
    extended = '....' + state + '....'
    return recenter(offset - 2, ''.join(
        mappings.get(extended[i:i + 5], '.') for i in range(len(state) + 4)))

def run(n):
    seen = {}
    offset, state = recenter(0, initial)
    i = 0
    while i < n:
        seen[state] = (i, offset)
        offset, state = step(offset, state)
        i += 1
        if state in seen:
            prev_i, prev_offset = seen[state]
            offset += (n - i) // (i - prev_i) * (offset - prev_offset)
            i = n - (n - i) % (i - prev_i)
    return sum(offset + i for i, c in enumerate(state) if c == '#')

print(run(20))
print(run(50000000000))
