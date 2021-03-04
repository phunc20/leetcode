# Subtilité
Ton `set_sol.py` a beau l'air d'être tout simple, est-ce que tu peux en analyser la complexité en terme de
- espace
- et temps ?

## Complexity
- `range(n)` complexity
  - [https://stackoverflow.com/questions/31227536/what-is-the-difference-between-range0-2-and-listrange0-2](https://stackoverflow.com/questions/31227536/what-is-the-difference-between-range0-2-and-listrange0-2)
- `set(L)` complexity, where `L` is a Python list
  - [https://realpython.com/python-data-structures/](https://realpython.com/python-data-structures/)
- set difference complexity
  - [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
- `pop()` complexity
  - [https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations](https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations)

```python
def missingNumber(nums):
    # O(1)
    n = len(nums)
    # O(n) + O(n) + O(n) + O(1)
    return (set(range(n+1)) - set(nums)).pop()
```
