import sys
from fractions import Fraction

def main():
    weight = int(sys.argv[1])
    growth = int(sys.argv[2])
    old = int(sys.argv[3])
    gender = sys.argv[4]
    koefA = sys.argv[5]

    print(Fraction(DCI(weight, growth, old, gender, koefA)))


def DCI(w: int, g: int, o: int, gender: str, k: str):
    koefs = {"A": 1.2, "B": 1.38, "C": 1.46, "D": 1.55, "E": 1.64, "F": 1.73, "G": 1.9}
    genders = {"male": 5, "female": -161}

    if gender == "m" or gender == "male":
        return (w*10 + g*6.25 - o*5 + genders["male"]) * koefs[k]
    else:
        return (w*10 + g*6.25 - o*5 + genders["female"]) * koefs[k]



if __name__ == "__main__":
    main()
