#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length(); // Length of the input string
        int maxLength = 0; // Length of the longest substring without repeating characters
        unordered_set<char> charSet; // Set to store unique characters in the current substring
        int left = 0; // Pointer to the left end of the current substring
        
        // Loop through the string from left to right
        for (int right = 0; right < n; right++) {
            // If the current character is not in the set, add it to the set
            // and update the maxLength if necessary
            if (charSet.count(s[right]) == 0) {
                charSet.insert(s[right]);
                maxLength = max(maxLength, right - left + 1);
            } else {
                // If the current character is already in the set, remove characters
                // from the left end of the substring until the current character is not
                // in the set anymore
                while (charSet.count(s[right])) {
                    charSet.erase(s[left]);
                    left++;
                }
                // Add the current character to the set
                charSet.insert(s[right]);
            }
        }
        
        return maxLength; // Return the length of the longest substring without repeating characters
    }
};
