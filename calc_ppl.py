import math
import re

def Read_ngram(fd, n, P, W):
    while True:
        line = next(fd)
        line = line.strip().split()
        if len(line):
            p = float(line[0])
            tokens = line[1 : 1 + n]
            P[tuple(tokens)] = p 
            if len(line) >= 2 + n:
                W[tuple(tokens)] = float(line[1 + n])
        else:
            break

def Read_arpa(fd, P, W):
    while True:
        line = next(fd)
        line = line.strip()
        nums = re.findall(r'\\(\d+?)-grams:', line)
        if len(nums):
            try:
                Read_ngram(fd, int(nums[0]), P, W)
            except Exception as e:
                print(e)
        if line.startswith('\\end\\'):
            break

def Get_P(tokens, P, W):
    if tokens in P:
        return P[tokens]
    else:
        if len(tokens) == 1:
            return -100.0
        else:
            return Get_P(tokens[1:], P, W) + W.get(tokens[:-1], 0.0)

def Calc_tokens_lgp(tokens, P, W, ngrams=3):
    n = len(tokens)
    log_P = 0.0
    for i in range(1, n):
        l = max(0, i - ngrams + 1)
        p = Get_P(tokens[l : i + 1], P, W)
        print(tokens[l : i + 1], p)
        log_P += p
    return log_P / (n - 1)

def Calc_sentence_ppl(sentence, P, W, ngrams=3):
    tokens = ('<s>',) + tuple(sentence) + ('</s>',)
    log_10_p = Calc_tokens_lgp(tokens, P, W, ngrams)
    ppl = math.exp(-1.0 * math.log(10) * log_10_p)
    return ppl

if __name__ == '__main__':
    fin = open('./cs382_1.arpa', 'r', encoding='utf8')
    P = dict()
    W = dict()
    Read_arpa(fin, P, W)
    print(len(P), len(W))
    print(P)
    print(W)
    fin.close()
    while True:
        sentence = input().strip()
        print(Calc_sentence_ppl(sentence, P, W))
