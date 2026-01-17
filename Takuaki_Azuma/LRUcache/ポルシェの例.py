"""
ポルシェ911の例で理解するクラスとオブジェクト、__init__

あなたの理解をコードで表現してみましょう！
"""

class Porsche911:
    """
    ポルシェ911の設計図（クラス）
    
    この設計図には、どんなポルシェ911でも共通の特徴が書かれています。
    でも、実際の車は1台1台違うスペックを持ちます。
    """
    
    def __init__(self, color: str, horsepower: int, price: int):
        """
        ポルシェ1号機を作る時に実行されるメソッド
        
        引数（スペック）:
            color: 色（例: "レッド"）
            horsepower: 馬力（例: 450）
            price: 価格（例: 15000000）
        
        このメソッドが実行されると、実際のポルシェ1号機が完成します！
        """
        # スペックを保存（この車の特徴を記録）
        self.color = color           # この車の色
        self.horsepower = horsepower # この車の馬力
        self.price = price           # この車の価格
        
        # 車を作る時に必要なパーツを準備
        self.engine_status = "停止"  # エンジンの状態
        self.mileage = 0             # 走行距離
        self.owner = None            # オーナー（まだ誰も持っていない）
        
        print(f"🏎️ ポルシェ911が完成しました！")
        print(f"   色: {self.color}")
        print(f"   馬力: {self.horsepower}hp")
        print(f"   価格: {self.price:,}円")
    
    def start_engine(self):
        """エンジンをかける（オブジェクト作成後に使えるメソッド）"""
        self.engine_status = "稼働中"
        print(f"🚗 {self.color}のポルシェ911のエンジンがかかりました！")
    
    def drive(self, km: int):
        """走る（オブジェクト作成後に使えるメソッド）"""
        if self.engine_status == "停止":
            print("エンジンをかけてください！")
            return
        
        self.mileage += km
        print(f"🚗 {km}km走りました！総走行距離: {self.mileage}km")


# ============================================
# 実際にポルシェを作ってみる
# ============================================

print("=" * 60)
print("【ステップ1】設計図（クラス）は既に存在している")
print("=" * 60)
print("Porsche911という設計図があります。")
print("でも、まだ実際の車はありません。\n")

print("=" * 60)
print("【ステップ2】1号機のスペックを決める")
print("=" * 60)
print("1号機のスペック:")
print("  - 色: レッド")
print("  - 馬力: 450hp")
print("  - 価格: 15,000,000円\n")

print("=" * 60)
print("【ステップ3】実際にポルシェ1号機を作る（オブジェクト作成）")
print("=" * 60)
print("この瞬間、__init__メソッドが自動的に実行されます！\n")

# ここでオブジェクトが作成される！
# この瞬間、__init__(self, "レッド", 450, 15000000) が実行される
car1 = Porsche911("レッド", 450, 15000000)

print("\n" + "=" * 60)
print("【ステップ4】1号機が完成！これで使えます")
print("=" * 60)
print("car1という名前のポルシェ911が完成しました。")
print("これから、この車を使うことができます。\n")

# オブジェクト作成後、メソッドを使える
car1.start_engine()
car1.drive(100)

print("\n" + "=" * 60)
print("【ステップ5】2号機も作れる！")
print("=" * 60)
print("同じ設計図（クラス）を使って、別のスペックの車を作れます。\n")

# 2号機を作る（別のスペック）
# この瞬間、また__init__が実行される（2号機用に）
car2 = Porsche911("ブルー", 500, 18000000)

print("\n" + "=" * 60)
print("【まとめ】")
print("=" * 60)
print("✅ クラス（Porsche911）= 設計図")
print("✅ オブジェクト（car1, car2）= 実際の車")
print("✅ __init__ = 車を作る時に実行される処理")
print("✅ 引数（color, horsepower, price）= スペック")
print("\n")
print("car1とcar2は、同じ設計図から作られましたが、")
print("それぞれ違うスペックを持っています！")
print(f"car1の色: {car1.color}, 馬力: {car1.horsepower}hp")
print(f"car2の色: {car2.color}, 馬力: {car2.horsepower}hp")

