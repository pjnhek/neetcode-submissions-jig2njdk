class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # main idea here is to actually compute the time it takes 
        # for a car that is closest to the target first then iterate
        # through the remaining. if the current car's time to target
        # is greater than the previous car then that means its not 
        # in the same fleet, else its part of the fleet and we pop
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)
        stack = []
        for p, s in pos_speed:
            time_to_target = (target-p)/s
            stack.append(time_to_target)
            print(time_to_target)
            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)

