def hanoi(n, SOURCE, AUX, DEST):
    if n == 1:
        DEST.insert(0, SOURCE.pop(0))
        return
    hanoi(n - 1, SOURCE, DEST, AUX)
    print("=============================")
    print(f"SOURCE : {SOURCE}")
    print(f"AUX : {AUX}")
    print(f"DEST : {DEST}")
    print("=============================")
    DEST.insert(0, SOURCE.pop(0))
    hanoi(n - 1, AUX, SOURCE, DEST)


if __name__ == "__main__":
    n = 3
    A = [i for i in range(1, n + 1)]
    B = []
    C = []
    hanoi(n, A, B, C)
    print("Final : ")
    print(f"A : {A}")
    print(f"B : {B}")
    print(f"C : {C}")
