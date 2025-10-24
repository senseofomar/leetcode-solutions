# Two Pointers
def merge_two_lists(list1, list2):
    dummy = ListNode()  # placeholder node at start
    tail = dummy  # tail always points to last node in merged list

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next  # move tail forward

    # Attach remaining nodes (only one list may have leftovers)
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next  # skip dummy and return real head

# Recursive approach
def merge_two_lists2(self, list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2