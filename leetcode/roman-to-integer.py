import pyleet


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_value = roman_map[s[i]]

            # If the current numeral is smaller than the next one, it means subtraction
            if i + 1 < n and current_value < roman_map[s[i+1]]:
                total -= current_value
            else:
                total += current_value

        return total


testcases = [
    {"input": ("III"), "expected": 3},
    {"input": ("IV"), "expected": 4},
    {"input": ("IX"), "expected": 9},
    {"input": ("LVIII"), "expected": 58},
    {"input": ("MCMXCIV"), "expected": 1994}
]


results = pyleet.run(testcases)
pyleet.print_results(results)
