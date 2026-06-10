class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        lenStudent = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] >0:
                lenStudent -= 1
                count[s] -= 1
            else:
                break
            
        return lenStudent            