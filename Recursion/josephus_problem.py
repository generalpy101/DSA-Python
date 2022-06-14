"""
Problem : 
    We have people sitting in circle and we have to kill every kth person in a circular manner.
    Numbering starts from 0 and person also counts himself.
    eg : if we have 6 person, first person to be killed will be (k-1)th person i.e 2nd person
    We have to find last survivor.
"""


def josephus(persons, k, current=0):
    if len(persons) == 1:
        return
    to_kill = (current + k) % len(persons) - 1
    if to_kill < 0:
        to_kill = len(persons) - 1
    # print(current, to_kill, len(persons))
    print(f"Person {persons[to_kill]} eliminated")
    persons.pop(to_kill)
    josephus(persons, k, to_kill)


def josephus_without_arr(n, k):
    if n == 1:
        return 0
    return (josephus_without_arr(n - 1, k) + k) % n


if __name__ == "__main__":
    n = 5
    k = 3
    persons = [i for i in range(n)]
    josephus(persons, k)
    print(persons)
    print("==========================")
    print(josephus_without_arr(n, k))