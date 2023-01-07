from collections import defaultdict

# global S
word_list = []
idx_list = []
orgDict = set()
diffDict = defaultdict(list)
char = list(map(chr, range(ord('a'), ord('z')+1)))  # char = [ 'a' , 'b' , ... , 'z' ]


def init(N: int, str: list) -> None:
    # global S
    # S = ''.join(str)
    global word_list, idx_list
    word_list = ''.join(str).split('_')
    idx_list.clear()
    idx = 0
    for c in str:
        idx_list.append(idx)
        if c == '_':
            idx += 1
    orgDict.clear()
    diffDict.clear()


def addDict(word: list) -> None:
    W = ''.join(word)
    orgDict.add(W)
    for i in range(len(W)):
        for c in char:
            diffDict[W[:i]+c+W[i+1:]].append(W)


def removeDict(word: list) -> None:
    W = ''.join(word)
    orgDict.remove(W)
    for i in range(len(W)):
        for c in char:
            diffDict[W[:i]+c+W[i+1:]].remove(W)


def correctWord(start: int, end: int) -> int:
    # global S
    global word_list
    newWord = []
    cnt = 0

    ret = 0
    s, e = idx_list[start], idx_list[end] + 1

    for word in word_list[s:e]:
        if word not in orgDict and diffDict[word]:
            newWord.append(min(diffDict[word]))
            cnt+=1
        else:
            newWord.append(word)
    word_list[s:e] = newWord
    # S = S[:start] + '_'.join(newWord) + S[end+1:]
    return cnt


def destroy(result: list) -> None:
    result[:] = list('_'.join(word_list))
    # result[:] = list(S)