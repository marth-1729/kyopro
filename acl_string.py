from atcoder import string

"""
link : https://github.com/marth-1729/kyopro/blob/main/acl_string.py
ここのコードを改変・コピペで使用．
"""

S = input()
"""
suffix array:
・input  : 長さnの文字列 S
・output : 長さnの配列，S[i : ]のlistをsortしたときのindex

ex : 
S = "abacb" のとき，S[i : ]は以下のようになる．
["abacb", "bacb", "acb", "cb", "b"]
これをsortすると，
["abacb", "acb", "b", "bacb", "cb"]
が得られるので，各S[i : ]がsort後のlistのどのindexにあるかを対応付けたものが返る．
今回の場合は，
[0, 2, 4, 1, 3]
"""
# print(["abacb", "bacb", "acb", "cb", "b"])
# l = ["abacb", "bacb", "acb", "cb", "b"]
# l.sort()
# print(l)
sa = string.suffix_array(S)
print(sa)

"""
lcp array:
・input  : 長さnの文字列 S, Sのsuffix array
・output : 長さn - 1の配列，
        S[i : ]のリストをsortしたlistのj番目とj + 1番目の文字列のLCP(最長共通接頭辞)

ex : 
S = "abacb" のとき，
["abacb", "acb", "b", "bacb", "cb"]
がS[i : ]のリストをsortしたlistに該当するが，lcp arrayとして以下が返される．
[1, 0, 1, 0]

0番目の要素 : "abacb"と"acb"の共通接頭辞は"a"
1番目の要素 : "acb"と"b"の共通接頭辞は""
2番目の要素 : "b"と"bacb"の共通接頭辞は"b"
3番目の要素 : "bacb"と"cb"の共通接頭辞は""
"""
print(string.lcp_array(S, sa))

# 他にもz-アルゴリズムというのがあるらしいけど，よくわかってない．(内部はよくわからんけど，返す値は簡単)
"""
z_algorithm
・input  : 長さnの文字列 S
・output : 長さnの配列，
        SとS[i:]のLCPを返す．
"""
print(string.z_algorithm(S))
