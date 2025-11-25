class Recursion:

    numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]    #[4, 12, 3, 8, 17, 12, 1, 3, 8, 7]


    def sum(self, _numbers) -> int:
        """
        Return sum of numbers using recursion.
        Follow steps:
            1. Return 0 for an empty list of numbers.
            2. Split the problem by removing the first number `n1` from the list leaving `r` as remaining list (sub-problem).
            3. Invoke `sum(r)` recursively on the remaining list.
            4. Combine the result for the sub-problem with the first number `n1`: `return n1 + sum(r)`.
        """
        if not _numbers:
            return 0
        n1 = _numbers[0]
        r = _numbers[1:]
        return n1+ self.sum(r)
   

    def fib(self, _n, memo=None) -> int:
        if memo is None:
            memo = {}
        if _n in memo:
            return memo[_n]

        if _n == 0:
            return 0
        if _n == 1:
            return 1

        memo[_n] = self.fib(_n - 1, memo) + self.fib(_n - 2, memo)
        return memo[_n]


    def fib_gen(self, _n):
        ns = list(range(_n + 1))
        fibs = [self.fib(i) for i in ns]
        yield ns, fibs


    def perm(self, _numbers) -> list:
        if len(_numbers) == 0:
            return [[]]
        if len(_numbers) == 1:
            return [[_numbers[0]]]

        result = []
        first = _numbers[0]
        rest = _numbers[1:]

        perms = self.perm(rest)
        for p in perms:
            for i in range(len(p) + 1):
                result.append(p[:i] + [first] + p[i:])
        return result


    def pset(self, _numbers) -> list:
        if len(_numbers) == 0:
            return [[]]

        first = _numbers[0]
        rest = _numbers[1:]

        subsets = self.pset(rest)

        result = []
        for s in subsets:
            result.append(s)
            result.append([first] + s)

        return result


    def find(self, _numbers, match_func) -> list:
        return [n for n in _numbers if match_func(n)]


    def find_adjacent(self, pair, _numbers, _i=0) -> list:
        if _i >= len(_numbers) - 1:
            return []
        found = []
        if _numbers[_i] == pair[0] and _numbers[_i + 1] == pair[1]:
            found.append(_i)
        return found + self.find_adjacent(pair, _numbers, _i + 1)


    def find_pairs(self, n, _numbers) -> list:
        seen = set()
        results = []
        for x in _numbers:
            y = n - x
            if y in seen:
                pair = sorted([x, y])
                if pair not in results:
                    results.append(pair)
            seen.add(x)
        return results


    def find_all_sums(self, n, _numbers) -> list:
        results = []

        def backtrack(target, i, path):
            if target == 0:
                results.append(sorted(path))
                return
            if target < 0 or i == len(_numbers):
                return

            backtrack(target - _numbers[i], i + 1, path + [_numbers[i]])
            backtrack(target, i + 1, path)

        backtrack(n, 0, [])
        unique = []
        for r in results:
            if r not in unique:
                unique.append(r)
        return unique
