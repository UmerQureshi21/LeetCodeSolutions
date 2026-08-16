import java.util.HashMap; // import the HashMap class

public class LongestConsecutiveSequence_128 {

    public static void main(String[] args) {
        int nums[] = { 100, 199, 200, 1, 3, 2 };
        int answer = longestConsecutive(nums);
        System.out.println(answer);
    }

    public static int longestConsecutive(int[] nums) {
        HashMap<Integer, Boolean> lookups = new HashMap<>();
        for (int num : nums) {
            lookups.put(num, null);
        }

        int length = 0;

        for (int num : nums) {
            if(!lookups.containsKey(num - 1)){
                int temp = num;
                int count = 0;
                while(lookups.containsKey(temp)){
                    temp++;
                    count++;
                }
                if(count > length){
                    length = count;
                }
            }
        }

        return length;
    }

    public static int longestConsecutiveTOOLSLOW(int[] nums) {
        HashMap<Integer, Boolean> hasIncrement = new HashMap<>();

        for (int num : nums) {
            if (!hasIncrement.containsKey(num)) {
                hasIncrement.put(num, false);
            }
        }

        int count = 0;
        while (hasIncrement.size() > 0) {
            for (int key : hasIncrement.keySet()) {
                for (int num : nums) {
                    if (num - 1 == key) {
                        hasIncrement.put(key, true);
                    }
                }
            }

            HashMap<Integer, Boolean> hasIncrementCopy = new HashMap<>();

            for (int key : hasIncrement.keySet()) {
                if (hasIncrement.get(key)) {
                    hasIncrementCopy.put(key + 1, false);
                }
            }

            hasIncrement = hasIncrementCopy;
            count++;
        }

        return count;
    }

}
