class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        answer = 1
        stack = []
        stack.append(points[0])
        for i in range(1, len(points)):
            if stack[-1][0] <= points[i][0] <= stack[-1][1]:

                stack[-1][1] = min(points[i][1], stack[-1][1])
            else:
                stack.pop()
                answer += 1
                stack.append(points[i])
        return answer