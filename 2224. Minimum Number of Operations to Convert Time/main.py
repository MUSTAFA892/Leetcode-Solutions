class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = 60 * int(current[0:2]) + int(current[3:])
        correct_time = 60 * int(correct[0:2]) + int(correct[3:])
        diff = correct_time - current_time
        count = 0
        for i in [60,15,5,1]:
            count += diff // i
            diff %= i
        
        return count