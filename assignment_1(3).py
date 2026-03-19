
def grade(score):
    return "A" if score >= 70 else "B" if score >= 60 else "C" if score >= 50 else "D" if score >= 40 else "F"
score = int(input("Score (0‑100): "))
if 0 <= score <= 100:
    print("Grade:", grade(score))
else:
    print("Invalid score.")