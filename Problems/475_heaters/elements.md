# 475. 供暖器 · 要素

1. 区间定义：在closestDistance里对heaters数组二分，区间是[left, right]=[0, heaters长度-1]，两端都闭。

2. while 条件：用left<=right，因为要精确定位到heaters[mid]与h的关系，闭区间二分标准写法。

3. 判定条件：判定条件是比较heaters[mid]和当前房子坐标h的大小：相等、大于、小于三种情况。

4. 边界收缩：heaters[mid]==h时直接返回0（距离为0）；heaters[mid]>h时right=mid-1（往左找）；heaters[mid]<h时left=mid+1（往右找），循环结束后用left和right分别取右侧/左侧最近供暖器算距离。
