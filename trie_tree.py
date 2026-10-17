# trie木
# 後で勉強する．
# 377Gをハッシュで解いた(ハッシュの衝突が起きると確率でWAになる)ので，
# trie木の勉強後，trie木でも実装してみるかも．

s = input().split()
tree = {}
for t in s:
    current = tree
    for c in t:
        if c in current:
            current[c][0] += 1
        else:
            current[c] = [1, {}]
        current = current[c][1]
print(tree)








## -----------------------------------------------------------------------------------
# もしかして，こっちの方が使いやすい？(こっちは辞書だから，重複があった場合がしんどいか)
# 勉強しやすい方を選んで使うか
# 引用：https://tech.aru-zakki.com/tire-implementation-python-and-go/
class TrieNode:
    def __init__(self):
        # 辞書型の定義、キー: 文字, 値: 子ノード(TrieNode)
        self.children = {}
        # そのノードが単語の終わりかどうかを表すフラグ
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """文字列を追加する"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """完全一致検索"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word: str) -> bool:
        """文字列を削除する（フラグを落とすだけの論理削除）"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # 単語が存在しない
            node = node.children[char]

        if not node.is_end_of_word:
            return False  # そもそも登録されていない

        node.is_end_of_word = False
        return True

    def get_all_words_sorted(self) -> list[str]:
        """辞書順に全単語を取得する"""
        results = []

        def _dfs(node: TrieNode, prefix: str):
            if node.is_end_of_word:
                results.append(prefix)

            # 辞書順にするためにキーをソートして走査
            for char in sorted(node.children.keys()):
                _dfs(node.children[char], prefix + char)

        _dfs(self.root, "")
        return results

trie = Trie()

# 文字列の追加
words = ["cat", "car", "dog"]
print(f"追加する単語: {words}")
for w in words:
    trie.insert(w)

print("-" * 20)

# 検索テスト
print(f"Search 'cat': {trie.search('cat')}")
print(f"Search 'dog': {trie.search('dog')}")
print(f"Search 'do': {trie.search('do')}")

print("-" * 20)

# 辞書順リストアップ
print("辞書順の単語リスト:")
print(trie.get_all_words_sorted())

print("-" * 20)

# 削除テスト
print("Delete 'car'")
trie.delete("car")
print(f"Search 'car': {trie.search('car')}")
print(f"Search 'cat': {trie.search('cat')}")

print("-" * 20)
print("削除後の単語リスト:")
print(trie.get_all_words_sorted())