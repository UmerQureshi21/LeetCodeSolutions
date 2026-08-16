import java.util.List;
import java.util.ArrayList;
import java.util.HashMap; // import the HashMap class

class GroupAnagrams_49 {

    // public List<List<String>> groupAnagrams(String[] strs) {

    // List<List<String>> anagrams = new ArrayList<>();

    // HashMap<String, List<String>> sorted_words = new HashMap<String,
    // List<String>>();

    // for (String word : strs) {
    // String sorted_word = "";
    // char[] chars = word.toCharArray();
    // Arrays.sort(chars);
    // for (char c : chars) {
    // sorted_word += c;
    // }
    // if (sorted_words.containsKey(sorted_word)) {
    // List<String> idk = new ArrayList<>();
    // idk = sorted_words.get(sorted_word);
    // idk.add(word);
    // sorted_words.put(sorted_word, idk);
    // } else {
    // List<String> idk = new ArrayList<>();
    // idk.add(word);
    // sorted_words.put(sorted_word, idk);
    // }
    // }

    // for(List<String> anagram_list: sorted_words.values()){
    // anagrams.add(anagram_list);
    // }

    // // HashMap<HashMap<Character,Integer>,String[]> letterCounts = new HashMap<
    // // HashMap<Character,Integer>, String[]>();

    // // for (String word : strs) {
    // // HashMap<Character, Integer> letterCount = new HashMap<Character,
    // Integer>();
    // // for (int i = 0; i < word.length(); i++) {
    // // char letter = word.charAt(i);
    // // if (letterCount.containsKey(letter)) {
    // // letterCount.put(letter, letterCount.get(letter) + 1);
    // // } else {
    // // letterCount.put(letter, 1);
    // // }
    // // }
    // // letterCounts.put(letterCount,[""]);
    // // }

    // return anagrams;
    // }

    public static void main(String[] args) {
        String[] idk = { "ate", "eat", "tan", "nat", "bat", "tea" };

        System.out.println(groupAnagrams(idk));
    }

    //
    public static List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> groups = new HashMap<String, List<String>>();

        for (String word : strs) {
            int[] count = new int[26];
            for (char letter : word.toCharArray()) {
                count[(int) letter - (int) 'a']++;
            }
            char[] count_string_representation = new char[26];
            for(int i =0; i < count.length;i++){
                count_string_representation[i] = (char) (count[i] + 48);
            }
            String freqs = new String(count_string_representation);

            if (groups.containsKey(freqs)) {
                List<String> words = groups.get(freqs);
                words.add(word);

                groups.put(freqs, words);
            } else {
                List<String> words = new ArrayList<String>();
                words.add(word);
                groups.put(freqs, words);
            }
        }

        return new ArrayList<>(groups.values());

    }

}
