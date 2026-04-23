import sys

def minion_game(string):
    if 0<len(string)<=pow(10,6):
        for i, c in enumerate(string):
            if c in ["A","E","I","O","U"]:
                kevin+=len(string)-i
            else:
                stuart+=len(string)-i
        if kevin<stuart:
            print(f"Stuart {stuart}")
        elif kevin>stuart:
            print(f"Kevin {kevin}")
        else:
            print(f"Draw")
    else:
        sys.exit()

if __name__ == '__main__':
    s = input()
    minion_game(s)
    