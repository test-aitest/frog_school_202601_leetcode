class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string has valid brackets using a stack.
        スタックを使用して、入力文字列の括弧が有効かどうかを判定します。
        """
        # Dictionary to map closing brackets to their corresponding opening brackets
        # 閉じ括弧をキー、対応する開き括弧を値とする辞書を作成します
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # Initialize an empty stack to keep track of opening brackets
        # 開き括弧を保持するための空のスタックを初期化します
        stack = []
        
        for char in s:
            # If the character is a closing bracket (it exists in our map)
            # 文字が閉じ括弧の場合（辞書のキーに存在する場合）
            if char in bracket_map:
                # Get the top element of the stack if it's not empty, otherwise use a dummy value
                # スタックが空でない場合は一番上の要素を取得し、空の場合はダミー値を使用します
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the current closing bracket
                # 取り出した開き括弧が、現在の閉じ括弧と対応しているか確認します
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                # 開き括弧の場合は、スタックに追加（プッシュ）します
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        # スタックが空であれば、すべての括弧が正しく対応していたことになります
        return not stack