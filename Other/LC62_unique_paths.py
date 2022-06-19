class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Everytime choose right or down
        # m-1 down, n-1 right, totally m+n-2 choices
        # same as m-1 red balls, n-1 blue balls, totally m+n-2 slots, how many different place methods
        # assume we place m-1 red balls on table, and we want to insert blues balls to the n intervals
        # that's (m+n-2)!/((m-1)!(n-1)!)
        return int(factorial(m+n-2)/(factorial(m-1) * factorial(n-1)))