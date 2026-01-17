# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into one.
        2つのソート済み連結リストを1つにマージします。
        """
        # Create a dummy node to simplify the process of building the new list.
        # 新しいリストを作成する際、コードを簡略化するために「ダミーノード」を使います。
        dummy = ListNode()
        
        # 'tail' will keep track of the last node in the merged list.
        # 'tail' はマージ後のリストの末尾を常に指します。
        tail = dummy
        
        # Iterate as long as both lists have nodes.
        # 両方のリストにノードが残っている間、繰り返します。
        while list1 and list2:
            # Attach the smaller node to our merged list.
            # 値が小さい方のノードを、マージリストの末尾に繋ぎます。
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move the tail pointer forward.
            # tail を新しく追加されたノードに進めます。
            tail = tail.next
            
        # If one list is exhausted, attach the remaining nodes of the other list.
        # 片方のリストが空になったら、もう片方の残りのノードをすべて末尾に繋ぎます。
        tail.next = list1 or list2
        
        # Return the head of the merged list (skipping the dummy node).
        # ダミーノードの次からが本番のリストなので、dummy.next を返します。
        return dummy.next
