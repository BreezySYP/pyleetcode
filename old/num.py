

from typing import Dict, List


class Solution:

    def __init__(self):
        self.indexDict: Dict[str, int] = {"type": 0, "color": 1, "num": 2}

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if not ruleKey == "type" or ruleKey == "color" or ruleKey == "name":
            raise BaseException("error")

        index = self.indexDict[ruleKey]
        return len([i for i in items if i[index] == ruleValue])


sol = Solution()
print(sol.countMatches([["phone", "blue", "pixel"], [
      "computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))
