import collections
from data_store import MOCK_WEB

def bfs(start_node):
    """Breadth-First Search: Level-order exploration."""
    # Optimization: Use a set for O(1) lookup speed
    visited = set()
    frontier = collections.deque([start_node])
    
    while frontier:
        yield list(frontier), list(visited), f"Current Frontier: {list(frontier)}"
        
        current = frontier.popleft()
        
        if current not in visited:
            visited.add(current)
            yield list(frontier), list(visited), f"Visiting: {current}"
            
            neighbors = MOCK_WEB.get(current, {}).get("links", [])
            for neighbor in neighbors:
                # Efficiency: Check both visited and frontier to avoid duplicates
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)
            
            yield list(frontier), list(visited), f"Found {len(neighbors)} links on {current}"

def dfs(start_node):
    """Depth-First Search: Path-first exploration."""
    visited = set()
    frontier = [start_node] 
    
    while frontier:
        yield frontier, list(visited), f"Current Stack: {frontier}"
        
        current = frontier.pop()
        
        if current not in visited:
            visited.add(current)
            yield frontier, list(visited), f"Visiting: {current}"
            
            neighbors = MOCK_WEB.get(current, {}).get("links", [])
            for neighbor in reversed(neighbors):
                # FIX: Added 'neighbor not in frontier' to prevent redundant processing
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)
            
            yield frontier, list(visited), f"Following deep path from {current}..."

def dls(start_node, limit):
    """
    Practical Depth-Limited Search: 
    Includes cycle prevention (visited set) for web safety.
    """
    visited = set()
    # Stores (node, depth)
    frontier = [(start_node, 0)]
    
    while frontier:
        current_frontier_nodes = [node for node, depth in frontier]
        yield current_frontier_nodes, list(visited), f"Frontier (Nodes & Depths): {frontier}"
        
        current, depth = frontier.pop()
        
        if current not in visited:
            visited.add(current)
            yield current_frontier_nodes, list(visited), f"Visiting {current} at depth {depth}"
            
            if depth < limit:
                neighbors = MOCK_WEB.get(current, {}).get("links", [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        frontier.append((neighbor, depth + 1))
                yield current_frontier_nodes, list(visited), f"Expanding links at depth {depth + 1}"
            else:
                yield current_frontier_nodes, list(visited), f"Depth limit ({limit}) reached at {current}."