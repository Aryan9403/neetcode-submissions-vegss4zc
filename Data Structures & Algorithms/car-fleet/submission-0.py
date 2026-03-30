class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        stack = []
        
        for pos,spd in cars:
            t = (target - pos) / spd

            if not stack or t > stack[-1]:
                stack.append(t)
            
            else: 

                pass

        return len(stack)
        