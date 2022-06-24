/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> seen = new HashSet<>();
        for (ListNode p = headA; p != null; p = p.next) {
            seen.add(p);
        }
        for (ListNode p = headB; p != null; p = p.next) {
            if (seen.contains(p)) {
                return p;
            }
        }
        return null;
    }
}