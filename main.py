from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with all 1s (the first and last elements)
        row = [1] * (rowIndex + 1)
        
        # Calculate the values in reverse order
        for i in range(1, rowIndex):
            # Update the row from the end to the start
            # This prevents overwriting values we still need to use
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row


