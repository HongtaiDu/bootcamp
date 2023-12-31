class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        st = Deque()
        st.append((0, -1))
        val = 0

        min_len = None
        left = 0
        
        for i, num in enumerate(nums):
            val += num
            t = val - k
            
            last_val = None
            while st and st[0][0] <= t:
                last_val = st[0]
                st.popleft()

            if last_val:
                if min_len is None or i-last_val[1] < min_len:
                    min_len = i-last_val[1]

            while st and st[-1][0] >= val:
                st.pop()
            st.append((val, i))

        return min_len or -1