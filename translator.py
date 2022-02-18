class Translator:
    def __init__(self, dictionary, rev_dict):
        self.dictionary = dictionary
        self.rev_dict = rev_dict

    def translate(self, word):
        translated = word.upper()
        for k, v in self.dictionary.items():
            translated = translated.replace(k, v[0])
        return translated

    def gematria(self, word):
        gematria_sum = 0
        for char in self.translate(word):
            try:
                gematria_sum += self.rev_dict[char.upper()][1]
            except KeyError:
                pass
        return gematria_sum

    def gematria_prime(self, word, primes):
        gematria_sum = 0
        for char in self.translate(word):
            try:
                gematria_sum += primes[self.rev_dict[char.upper()][1]]
            except KeyError:
                pass
        return gematria_sum
