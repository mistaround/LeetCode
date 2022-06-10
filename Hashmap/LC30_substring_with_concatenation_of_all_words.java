import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

// Algorithm

// Initialize some variables:
// n as the length of s.
// k as the length of words
// wordLength as the length of each word in words.
// substringSize as wordLength * k, which represents the size of each valid substring.
// wordsCount as a hash table that tracks how many times a word occurs in words.
// answer as an array that will hold the starting index of every valid substring

// Create a function slidingWindow that takes an index left and starts a sliding window from left:
    // Initialize a hash table wordsFound that will keep track of how many times a word appears in our window. Also, an integer wordsUsed = 0 to keep track of how many words are in our window, and a boolean excessWord = false that indicates if our window is currently holding an excess word, such as a third "foo" if words = ["foo", "foo"].
    // Iterate using the right bound of our window, right. Start iteration at left, until n, wordLength at a time. At each iteration:
        // We are dealing with a word sub = s.substring(right, right + wordLength). If sub is not in wordsCount, then we must reset the window. Clear our hash table wordsFound, and reset our variables wordsUsed = 0 and excessWord = false. Move left to the next index we will handle, which will be right + wordLength.
        // Otherwise, if sub is in wordsCount, we can continue with our window. First, check if our window is beyond max size or has an excess word. So long as either of these conditions are true, move left over while appropriately updating our hash table, integer and boolean variables.
        // Now, we can handle sub. Increment its value in wordsFound, and then compare its value in wordsFound to its value in wordsCount. If the value is less than or equal, then we can make use of this word in a valid substring - increment wordsUsed. Otherwise, it is an excess word, and we should set excessWord = true.
        // At the end of it all, if we have wordsUsed == k without any excess words, then we have a valid substring. Add left to answer.

// Call slidingWindow with each index from 0 to wordLength. Return answer once finished.

class Solution {
    HashMap<String, Integer> wordsCount = new HashMap<>();
    int n;
    int k;
    int wordLength;
    int substringLength;

    private void sildingWindow(int left, String s, List<Integer> ans) {
        HashMap<String, Integer> wordsFound = new HashMap<>();
        int wordsUsed = 0;
        boolean excessed = false;
        
        for (int right = left; right <= n - wordLength; right += wordLength) {
            String sub = s.substring(right, right + wordLength);
            if (wordsCount.containsKey(sub)) {
                while (right - left == substringLength || excessed) {
                    String head = s.substring(left, left + wordLength);
                    wordsFound.put(head, wordsFound.get(head) - 1);
                    left += wordLength;
                    
                    if (wordsFound.get(head) >= wordsCount.get(head)) {
                        excessed = false;
                    } else {
                        wordsUsed --;
                    }
                }
                
                wordsFound.put(sub, wordsFound.getOrDefault(sub, 0) + 1);
                if (wordsFound.get(sub) <= wordsCount.get(sub)) {
                    wordsUsed ++;
                } else {
                    excessed = true;
                }

                if (wordsUsed == k && !excessed) {
                    ans.add(left);
                }
            } else {
                wordsUsed = 0;
                excessed = false;
                wordsFound.clear();
                left = right + wordLength;
            }
        }
    }

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans = new ArrayList<>();
        n = s.length();
        k = words.length;
        wordLength = words[0].length();
        substringLength = wordLength * k;

        for (String word : words) {
            wordsCount.put(word, wordsCount.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i< wordLength; i++) {
            sildingWindow(i, s, ans);
        }

        return ans;
    }
}