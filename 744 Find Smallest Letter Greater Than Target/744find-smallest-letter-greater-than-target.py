class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        result = ""
        
        while (low <= high):
            mid = low + (high - low) // 2
            
            if (letters[mid] > target):
                result = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
        
        if (result != ""):
            return result
        return letters[0]