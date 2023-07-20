'''
一个酒店里有 n 个房间，这些房间用二维整数数组 rooms 表示，其中 rooms[i] = [roomIdi, sizei] 表示有一个房间号为 roomIdi 的房间且它的面积为 sizei 。每一个房间号 roomIdi 保证是 独一无二 的。

同时给你 k 个查询，用二维数组 queries 表示，其中 queries[j] = [preferredj, minSizej] 。第 j 个查询的答案是满足如下条件的房间 id ：

房间的面积 至少 为 minSizej ，且
abs(id - preferredj) 的值 最小 ，其中 abs(x) 是 x 的绝对值。
如果差的绝对值有 相等 的，选择 最小 的 id 。如果 没有满足条件的房间 ，答案为 -1 。

请你返回长度为 k 的数组 answer ，其中 answer[j] 为第 j 个查询的结果。

 

示例 1：

输入：rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
输出：[3,-1,3]
解释：查询的答案如下：
查询 [3,1] ：房间 3 的面积为 2 ，大于等于 1 ，且号码是最接近 3 的，为 abs(3 - 3) = 0 ，所以答案为 3 。
查询 [3,3] ：没有房间的面积至少为 3 ，所以答案为 -1 。
查询 [5,2] ：房间 3 的面积为 2 ，大于等于 2 ，且号码是最接近 5 的，为 abs(3 - 5) = 2 ，所以答案为 3 。
示例 2：

输入：rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
输出：[2,1,3]
解释：查询的答案如下：
查询 [2,3] ：房间 2 的面积为 3 ，大于等于 3 ，且号码是最接近的，为 abs(2 - 2) = 0 ，所以答案为 2 。
查询 [2,4] ：房间 1 和 3 的面积都至少为 4 ，答案为 1 因为它房间编号更小。
查询 [2,5] ：房间 3 是唯一面积大于等于 5 的，所以答案为 3 。
 

提示：

n == rooms.length
1 <= n <= 105
k == queries.length
1 <= k <= 104
1 <= roomIdi, preferredj <= 107
1 <= sizei, minSizej <= 107

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/closest-room
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import Dict, List


class PickedId:
    def __init__(self, id: int, picked: bool):
        self._id = id
        self._picked = picked

    def get_picked(self):
        return self._picked

    def set_picked(self, value):
        self._picked = value

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # roomDict = {}
        # for room in rooms:
        #     roomDict[room[0]] = room[1]

        minQuerySize = min([q[1] for q in queries])
        roomsAsc = sorted(rooms, key=lambda x:x[1], reverse=False)

        sizeRooms = {}

        for room in roomsAsc:
            if room[1] > minQuerySize:
                sizeRooms.setdefault(room[1], [[]])
                sizeRooms[room[1]].append(PickedId(room[0], False))

        picked = [-1] * len(queries)

        for i in range(len(queries)):
            for size, rooms in sizeRooms.items():
                if queries[i][1] <= size:
                    for room in rooms:
                        if room.get == 0:
                            room[1] = 1
                            picked[i] = room[0]

        return picked

sol = Solution()

print(sol.closestRoom(rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]))