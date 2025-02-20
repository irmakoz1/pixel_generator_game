Pixel generation game using heuristic search algorithm:


How it works:

![Game image](hs_pixel_gen.png)


Algorithm starts from a single pixel and expands outward, choosing new pixels based on priority. This is similar to how A search* finds the shortest path in a maze.

Step-by-Step Process:
Start from a random pixel (e.g., (x, y) = (5, 5))
Push the pixel into a priority queue (heapq)
Expand to neighboring pixels (up, down, left, right)
Prioritize which pixel to expand next using a heuristic function
Repeat until enough pixels are drawn

Pixels are sorted by priority using heapq (a min-heap in Python):

heapq.heappush(pq, (priority, x, y)):
The lower the priority number, the sooner a pixel gets processed.
The heuristic function helps determine priority.


The Heuristic Function uses Manhattan distance:
A heuristic guides the search, deciding which pixel to expand next.

Manhattan Distance Formula:

def heuristic(x, y):
    return abs(x - ROWS // 2) + abs(y - COLS // 2)

This measures how far (x, y) is from the center of the grid.
It’s called Manhattan distance because it’s like moving on a grid (no diagonal moves).

**Pixels closer to the center get processed first.
This makes pixels spread outward in a structured way, instead of randomly.


The Expansion Process:
start_x, start_y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
heapq.heappush(pq, (0, start_x, start_y))

Picks a random start pixel, then adds it to the priority queue with priority 0.


 Process the Highest Priority Pixel:
_, x, y = heapq.heappop(pq)
Removes the pixel with the lowest priority. This ensures structured growth.

Expand to Neighboring Pixels:
Looks at neighbors (up, down, left, right). If not visited, it calculates:

for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nx, ny = x + dx, y + dy
    if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in visited:
        priority = heuristic(nx, ny) + random.randint(0, 5)
        heapq.heappush(pq, (priority, nx, ny))



Heuristic function: Determines distance from center.

priority = heuristic(nx, ny) + random.randint(0, 5)
Random factor (random.randint(0, 5)): Adds some randomness so it's not too predictable.
Pushes new pixels into the priority queue.

Visualization: How It Expands
If the center is the goal, pixels expand outward in a controlled way.
        -  -  -  -  -  
        -  X  X  X  -  
        -  X  O  X  -  
        -  X  X  X  -  
        -  -  -  -  -  
The center pixel "O" starts first.
The closest pixels "X" get priority and expand first.
Further pixels "-" are processed later.
