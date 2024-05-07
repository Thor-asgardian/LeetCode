public class Solution {
    public String reversePrefix(String word, char ch) {
        int j = word.indexOf(ch);
        if (j != -1) {
            return new StringBuilder(word.substring(0, j + 1)).reverse().toString() + word.substring(j + 1);
        }
        return word;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        // Example usage
        String word = "abcdefg";
        char ch = 'd';
        String reversed = solution.reversePrefix(word, ch);
        System.out.println(reversed); // Output: "dcbaefg"
    }
}
