# 203. Remove Linked List Elements
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class linked_list():
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        current = self.head

        if self.head == None:
            self.head = new_node
            return
        while current.next != None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        if current == None:
            print('List is empty')
            return self.head
        while current != None:
            print(current.val)
            current = current.next
        # print(current.val)

    def removeElements(self, head, val):
        # if head != None:
        current = self.head

        if self.head == None:
            print('there is nothing to delete!')
            return head
        temp = current.next

        while temp != None:
            if current.val == val:
                current = temp
                temp = temp.next
                self.head = current
                continue
            if temp.val == val:
                temp = temp.next
                current.next = temp
                continue

            temp = temp.next
            current = current.next
        if current.val == val:
            self.head = None

        return head

        # current = self.head
        # temp = current.next
        #
        # if current.next == None:
        #     return None
        # else:
        #     while temp != None:
        #         if temp.val == val:
        #             temp = temp.next
        #             current.next = temp
        #             continue
        #         temp = temp.next
        #         current = current.next


# new_list = linked_list()
# # new_list.display()
# new_list.append(4)
# new_list.append(5)
head  = [1,2,6,3,4,5,6]
val = 6
# head  = [1]
# val = 1
# head  = []
# val = 1
# head = [1,2]
# val = 1
# head  = [7,7,7,7]
# val = 7
new_list = linked_list()
# new_list.append(1)
# new_list.append(2)

# new_list.append(7)
# new_list.append(7)
# new_list.append(7)
# new_list.append(7)

new_list.append(1)
new_list.append(2)
new_list.append(6)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.append(6)

new_list.removeElements(head, val)
new_list.display()