from typing import List

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        current_direction = "N"
        left_turn = {"N":"W","W":"S","S":"E","E":"N"}
        right_turn = {"W":"N","S":"W","E":"S","N":"E"}
        
        record_movement = []
        for instruction in instructions:
            if instruction == "G":
                record_movement.append(current_direction)
            if instruction == "L":
                current_direction = left_turn[current_direction]
            if instruction == "R":
                current_direction = right_turn[current_direction]
        if current_direction != "N":
            return True
        movement_counter = Counter(record_movement)
        if movement_counter["S"]!=movement_counter["N"] or movement_counter["W"]!=movement_counter["E"]:
            return False
        return True

sol = Solution()

print(sol.isRobotBounded())