import sys

def imt(weight: int, growth: float) -> float:
    return weight/(growth**2)

def main():
    weights = []
    growths = []

    for n, a in enumerate(sys.argv):
        if n % 2 != 0:
            weights.append(int(a))
        else:
            if n != 0:
                growths.append(float(a))

    if len(weights) != len(growths):
        print("Something wrong")

    for n in range(len(weights)):
        w = weights[n]
        g = growths[n]
        print(f"Weight: {w} Growth: {g} IMT:",round(imt(w, g), 3))


if __name__ == "__main__":
    main()


