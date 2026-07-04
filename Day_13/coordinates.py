from math import sqrt
WORDS={
    "cat":{0.9,0.1},
    "dog":{0.8,0.2},
    "car":{0.1,0.9},
    "truck":{0.2,0.8},
}
def distance(a,b):
    """Straight- line distance between 2 points  """
    return sqrt((a[0]-b[0])**2+ (a[1]-b[1])**2)
def main():
    print("Each word is a point: \n")
    for word,vec in WORDS.items():
        print(f"{word} --> {vec}")

#compare everything to cat and sort from close to far

    target="cat"
    scores =[]
    for word,vec in WORDS.items():
        if word == target:
            continue
        scores.append((word,distance(WORDS[target],vec)))
        print(scores)
if __name__=="__main__":
    main()