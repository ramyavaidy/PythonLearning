from collections import deque

# Create a deque
dq = deque()

# Add elements to the right
dq.append(1)
dq.append(2)
dq.append(3)

# Add elements to the left
dq.appendleft(0)

# Remove elements from the right
dq.pop()

print(f"Deque after pop: {dq}")
# Remove elements from the left
dq.popleft()

# Access elements
print(f"Deque: {dq}")
print(f"Length: {len(dq)}")