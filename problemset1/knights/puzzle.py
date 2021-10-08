from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    #A is knight or knave
    Or(AKnight, AKnave),
    #if A is Knight he can't be Knave and reversed
    Not(And(AKnight, AKnave)),
    #A says that he is both
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #A and B are both knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    #A and B are one of these
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    #A says that they are both knaves (must be knave)
    #B says nothing (must me knight)
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #A and B are both knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    #A and B are one of these
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    #A says that they are both knights or both  knaves
    #B says that they are different
    #if A is true then B should agree with him, not say that they are different
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #A and B are both knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    #A and B are one of these
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Biconditional(Or(AKnight, AKnave), Or(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, BKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
