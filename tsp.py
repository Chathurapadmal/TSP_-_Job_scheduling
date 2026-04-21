import itertools

def calculate_total_distance(route, dist_matrix):
    distance = 0
    for i in range(len(route) - 1):
        distance += dist_matrix[route[i]][route[i+1]]
    distance += dist_matrix[route[-1]][route[0]] # Return to origin
    return distance

def solve_tsp_brute_force(dist_matrix):
    num_cities = len(dist_matrix)
    cities = list(range(num_cities))
    
    # Generate all permutations starting from city 0
    permutations = itertools.permutations(cities[1:])
    
    min_dist = float('inf')
    best_route = None
    
    for p in permutations:
        current_route = [0] + list(p)
        current_dist = calculate_total_distance(current_route, dist_matrix)
        
        if current_dist < min_dist:
            min_dist = current_dist
            best_route = current_route
            
    return best_route, min_dist

def get_distance_matrix_from_user():
    
    print("Find the shortest route.\n")
    
    # Get number of cities
    while True:
        try:
            num_cities = int(input("Enter the number of cities: "))
            if num_cities < 2:
                print("Please enter a number >= 2")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    
    print(f"\nEnter the distance matrix ({num_cities}x{num_cities}):")
    print("Note: Distance from city i to city j (must be symmetric for optimal results)")
    print("Diagonal elements should be 0 (distance from a city to itself)\n")
    
    matrix = []
    for i in range(num_cities):
        row = []
        for j in range(num_cities):
            while True:
                try:
                    if i == j:
                        row.append(0)
                        break
                    distance = float(input(f"Distance from city {i} to city {j}: "))
                    if distance < 0:
                        print("Distance cannot be negative. Please enter again.")
                        continue
                    row.append(distance)
                    break
                except ValueError:
                    print("Please enter a valid number")
        matrix.append(row)
    
    return matrix

# Get user input
matrix = get_distance_matrix_from_user()

# Solve TSP
print("\nSolving...")
route, dist = solve_tsp_brute_force(matrix)
print(f"\nBest Route: {route}")
print(f"Total Distance: {dist}")