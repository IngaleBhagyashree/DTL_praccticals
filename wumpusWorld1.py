# Improved Wumpus World (Agent tries to reach gold safely)

GRID = 4

# Environment
wumpus = (2, 0)
pits = {(0, 2), (2, 2), (3, 3)}
gold = (2, 1)

# Agent knowledge
safe_cells = set()
visited = set()
possible_pit = set()
possible_wumpus = set()

# Start position
agent_pos = (0, 0)
safe_cells.add(agent_pos)


def neighbors(cell):
    x, y = cell
    n = []
    if x > 0: n.append((x-1, y))
    if x < GRID-1: n.append((x+1, y))
    if y > 0: n.append((x, y-1))
    if y < GRID-1: n.append((x, y+1))
    return n


def perceive(cell):
    percepts = []
    for n in neighbors(cell):
        if n in pits:
            percepts.append("Breeze")
        if n == wumpus:
            percepts.append("Stench")
    return percepts


def infer(cell, percepts):
    adj = neighbors(cell)

    # If no Breeze → adjacent cells safe from pits
    if "Breeze" not in percepts:
        for a in adj:
            safe_cells.add(a)
            possible_pit.discard(a)
    else:
        for a in adj:
            if a not in safe_cells:
                possible_pit.add(a)

    # If no Stench → adjacent cells safe from wumpus
    if "Stench" not in percepts:
        for a in adj:
            safe_cells.add(a)
            possible_wumpus.discard(a)
    else:
        for a in adj:
            if a not in safe_cells:
                possible_wumpus.add(a)


def choose_move(cell):
    for n in neighbors(cell):
        if n in safe_cells and n not in visited:
            return n
    return None


print("=== Wumpus World Simulation ===\n")

for step in range(20):
    print(f"Step {step+1}")
    print("Agent at:", agent_pos)

    # Check death
    if agent_pos in pits:
        print("Agent fell into a PIT! Game Over.")
        break

    if agent_pos == wumpus:
        print("Agent eaten by WUMPUS! Game Over.")
        break

    # Check gold
    if agent_pos == gold:
        print("Agent found the GOLD!")
        break

    visited.add(agent_pos)

    percepts = perceive(agent_pos)
    print("Percepts:", percepts if percepts else "None")

    infer(agent_pos, percepts)

    move = choose_move(agent_pos)

    if move:
        print("Moving to:", move, "\n")
        agent_pos = move
    else:
        print("No safe move available. Stopping.\n")
        break


print("\nVisited:", visited)
print("Safe cells:", safe_cells)
print("Possible pits:", possible_pit)
print("Possible wumpus:", possible_wumpus)# Improved Wumpus World (Agent tries to reach gold safely)

GRID = 4

# Environment
wumpus = (2, 0)
pits = {(0, 2), (2, 2), (3, 3)}
gold = (2, 1)

# Agent knowledge
safe_cells = set()
visited = set()
possible_pit = set()
possible_wumpus = set()

# Start position
agent_pos = (0, 0)
safe_cells.add(agent_pos)


def neighbors(cell):
    x, y = cell
    n = []
    if x > 0: n.append((x-1, y))
    if x < GRID-1: n.append((x+1, y))
    if y > 0: n.append((x, y-1))
    if y < GRID-1: n.append((x, y+1))
    return n


def perceive(cell):
    percepts = []
    for n in neighbors(cell):
        if n in pits:
            percepts.append("Breeze")
        if n == wumpus:
            percepts.append("Stench")
    return percepts


def infer(cell, percepts):
    adj = neighbors(cell)

    # If no Breeze → adjacent cells safe from pits
    if "Breeze" not in percepts:
        for a in adj:
            safe_cells.add(a)
            possible_pit.discard(a)
    else:
        for a in adj:
            if a not in safe_cells:
                possible_pit.add(a)

    # If no Stench → adjacent cells safe from wumpus
    if "Stench" not in percepts:
        for a in adj:
            safe_cells.add(a)
            possible_wumpus.discard(a)
    else:
        for a in adj:
            if a not in safe_cells:
                possible_wumpus.add(a)


def choose_move(cell):
    for n in neighbors(cell):
        if n in safe_cells and n not in visited:
            return n
    return None


print("=== Wumpus World Simulation ===\n")

for step in range(20):
    print(f"Step {step+1}")
    print("Agent at:", agent_pos)

    # Check death
    if agent_pos in pits:
        print("Agent fell into a PIT! Game Over.")
        break

    if agent_pos == wumpus:
        print("Agent eaten by WUMPUS! Game Over.")
        break

    # Check gold
    if agent_pos == gold:
        print("Agent found the GOLD!")
        break

    visited.add(agent_pos)

    percepts = perceive(agent_pos)
    print("Percepts:", percepts if percepts else "None")

    infer(agent_pos, percepts)

    move = choose_move(agent_pos)

    if move:
        print("Moving to:", move, "\n")
        agent_pos = move
    else:
        print("No safe move available. Stopping.\n")
        break


print("\nVisited:", visited)
print("Safe cells:", safe_cells)
print("Possible pits:", possible_pit)
print("Possible wumpus:", possible_wumpus)