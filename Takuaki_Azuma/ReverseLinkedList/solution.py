# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverses a singly linked list iteratively.
        単一連結リストを反復処理（ループ）で反転させます。
        """
        # 'prev' will keep track of the node before 'curr'. Initially, there's nothing before head.
        # 'prev' は現在（curr）の1つ前のノードを指します。最初は先頭（head）の前に何もないので None です。
        prev = None
        
        # 'curr' is the node we are currently processing.
        # 'curr' は現在処理しているノードです。
        curr = head
        
        while curr:
            # 1. Temporarily store the next node
            # 1. 次のノードを一時的に保存しておきます（接続を切る前に）
            next_node = curr.next
            
            # 2. Reverse the link: point 'curr.next' to the previous node
            # 2. 矢印（リンク）を逆にします：'curr.next' を前のノード（prev）に向けます
            curr.next = prev
            
            # 3. Move 'prev' forward to the current node
            # 3. 'prev' を現在のノード（curr）に進めます
            prev = curr
            
            # 4. Move 'curr' forward to the next node (using the saved reference)
            # 4. 'curr' を保存しておいた次のノード（next_node）に進めます
            curr = next_node
            
        # At the end, 'prev' will be the new head of the reversed list.
        # ループ終了時、'prev' が反転したリストの新しい先頭になります。
        return prev

