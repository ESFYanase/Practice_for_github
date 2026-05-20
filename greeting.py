"""
挨拶機能モジュール
"""


def greet(name):
    """指定された名前で挨拶する"""
    return f"こんにちは、{name}さん！"


def farewell(name):
    """指定された名前でお別れの挨拶をする"""
    return f"さようなら、{name}さん！"


if __name__ == "__main__":
    print(greet("太郎"))
    print(farewell("花子"))
