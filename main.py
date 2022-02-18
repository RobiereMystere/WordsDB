from database_utils import DatabaseUtils
from translator import Translator
import unidecode

if __name__ == '__main__':
    dbu = DatabaseUtils("database/oldwords.db")

    words = dbu.select("words")
    dbu.close()
    newdbu = DatabaseUtils("database/words.db")
    newdbu.execute("DELETE FROM words", [])
    newdbu.commit()
    futhork_occidental = {
        "ᚠ": ["F", 0],
        "ᚢ": ["V", 1],
        "ᚦ": ["TH", 2],
        "ᚩ": ["O", 3],
        "ᚱ": ["R", 4],
        "ᚳ": ["K", 5],
        "ᚷ": ["G", 6],
        "ᚹ": ["W", 7],
        "ᚻ": ["H", 8],
        "ᚾ": ["N", 9],
        "ᛁ": ["I", 10],
        "ᛄ": ["J", 11],
        "ᛇ": ["EO", 12],
        "ᛈ": ["P", 13],
        "ᛉ": ["X", 14],
        "ᛋ": ["S", 15],
        "ᛏ": ["T", 16],
        "ᛒ": ["B", 17],
        "ᛖ": ["E", 18],
        "ᛗ": ["M", 19],
        "ᛚ": ["L", 20],
        "ᛝ": ["NG", 21],
        "ᛟ": ["OE", 22],
        "ᛞ": ["D", 23],
        "ᚪ": ["A", 24],
        "ᚫ": ["AE", 25],
        "ᚣ": ["Y", 26],
        "ᛡ": ["IA", 27],
        "ᛠ": ["EA", 28]
    }
    occidental_futhork = {
        'ING': ['ᛝ', 21],
        'NG': ['ᛝ', 21],
        'AE': ['ᚫ', 25],
        'EO': ['ᛇ', 12],
        'OE': ['ᛟ', 22],
        'EA': ['ᛠ', 28],
        'IA': ['ᛡ', 27],
        'IO': ['ᛡ', 27],
        'TH': ['ᚦ', 2],
        'QU': ['ᚳᚹ', 7],
        'F': ['ᚠ', 0],
        'V': ['ᚢ', 1],
        'U': ['ᚢ', 1],
        'O': ['ᚩ', 3],
        'R': ['ᚱ', 4],
        'K': ['ᚳ', 5],
        'Q': ['ᚳ', 5],
        'C': ['ᚳ', 5],
        'G': ['ᚷ', 6],
        'W': ['ᚹ', 7],
        'H': ['ᚻ', 8],
        'N': ['ᚾ', 9],
        'I': ['ᛁ', 10],
        'J': ['ᛄ', 11],
        'P': ['ᛈ', 13],
        'X': ['ᛉ', 14],
        'S': ['ᛋ', 15],
        'Z': ['ᛋ', 15],
        'T': ['ᛏ', 16],
        'B': ['ᛒ', 17],
        'E': ['ᛖ', 18],
        'M': ['ᛗ', 19],
        'L': ['ᛚ', 20],
        'Y': ['ᚣ', 26],
        'D': ['ᛞ', 23],
        'A': ['ᚪ', 24]}
    primes = [2, 3, 5, 7, 11,
              13, 17, 19, 23,
              29, 31, 37, 41,
              43, 47, 53, 59,
              61, 67, 71, 73,
              79, 83, 89, 97,
              101, 103, 107,
              109, 113, 127,
              131, 137, 139,
              149, 151, 157,
              163, 167, 173,
              179, 181, 191,
              193, 197, 199]
    lines = []
    for word in words:
        w = word[1]
        lines.append(w.upper())
    with open("resources/Verifikant-WNo1.txt", "r") as f:
        lines += unidecode.unidecode(f.read().replace(".", "\n").replace(" ", "\n")).upper().split('\n')
    with open("resources/Novy_textovy_dokument_4.txt", 'r') as f:
        lines += unidecode.unidecode(f.read().replace(".", "\n").replace(" ", "\n")).upper().split('\n')
    o2f_translator = Translator(occidental_futhork, futhork_occidental)
    lines = list(set(lines))
    for line in lines:
        if len(line) > 0 and line.isalpha():
            newdbu.insert("words",
                          [newdbu.last_id("words") + 1,
                           line,
                           len(o2f_translator.translate(line)),
                           o2f_translator.gematria_prime(line, primes)])
    newdbu.commit()
    print(newdbu.select("words"))
    newdbu.close()
