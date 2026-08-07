class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # expected is the increasing order of the heights array
        # heights is the actual order
        # return the number of mismatched heights

        # sort the heights array, then compare the original arr to this
        # for any heights that don't match, add one to the index
        indices = 0

        expected = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                indices += 1

        return indices
