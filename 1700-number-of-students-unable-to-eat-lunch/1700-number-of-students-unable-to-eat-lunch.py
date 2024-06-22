class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            elif students.count(sandwiches[0]) == 0:
                break   
            else:
                students.append(students.popleft())                
         
        return len(students)
