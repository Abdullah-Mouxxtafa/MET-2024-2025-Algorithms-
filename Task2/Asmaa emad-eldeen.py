conflicts = [  
    {'NumOfInterection': 30, 'Conflict_sub_id': 200, 'sub_id': 100},  
    {'NumOfInterection': 15, 'Conflict_sub_id': 300, 'sub_id': 100}  
]  

courses = [  
    {'sub_id': 100, 'level': 1},  
    {'sub_id': 200, 'level': 2},  
    {'sub_id': 300, 'level': 3}  
]  
 
def calculate_total_cost(ordering):  
    total_cost = 0  
    for course in ordering:  
        for conflict in conflicts:  
            if (course['sub_id'] == conflict['sub_id'] or  
                course['sub_id'] == conflict['Conflict_sub_id']):  
                total_cost += conflict['NumOfInterection']  
    return total_cost  
 
def generate_permutations(courses, current_permutation, all_permutations):  
    if len(current_permutation) == len(courses):  
        all_permutations.append(current_permutation.copy())  
        return  

    for course in courses:  
        if course not in current_permutation:  
            current_permutation.append(course)  
            generate_permutations(courses, current_permutation, all_permutations)  
            current_permutation.pop()  


def find_best_order(courses):  
    best_order = None  
    lowest_cost = float('inf')  
    all_permutations = []  

    generate_permutations(courses, [], all_permutations)  

    for ordering in all_permutations:  
        cost = calculate_total_cost(ordering)  
        if cost < lowest_cost:  
            lowest_cost = cost  
            best_order = ordering  
            
    return best_order, lowest_cost  

 
best_order, cost = find_best_order(courses)  

  
print("Best arrangement of courses:")  
for course in best_order:  
    print(f"Course ID: {course['sub_id']} - Level: {course['level']}")  

print(f"\nTotal cost: {cost}")