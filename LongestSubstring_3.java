

public class LongestSubstring_3 {

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("a;ljdgeral90"));
    }

    public static int lengthOfLongestSubstring(String s) {
        int endP = 0;
        int max = 0;
        String letters = "";

        while (endP < s.length()) {
            if (letters.indexOf(s.charAt(endP)) == -1) {
                letters += s.charAt(endP);
            } else {
                if (max < letters.length()) {
                    max = letters.length();
                }
                letters = letters.substring(letters.indexOf(s.charAt(endP)) + 1, letters.length()) + s.charAt(endP);
            }
            if (max < letters.length()) {
                max = letters.length();
            }
            endP++;
        }
        return max;
    }
}
