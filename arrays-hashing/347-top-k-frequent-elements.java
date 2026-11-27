import java.util.List;
import java.util.ArrayList;
import java.util.HashMap; // import the HashMap class

public class TopKFrequentElements_347 {

    public static void main(String[] args) {
        int nums[] = { 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5 };
        int top[] = topKFrequent(nums, 2);
        for (int i : top) {
            System.out.println(i);
        }
    }

    public static int[] topKFrequent(int[] nums, int k) {
        List<List<Integer>> freqBucket = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            freqBucket.add(new ArrayList<>());
        }
        HashMap<Integer, Integer> freqs = new HashMap<>();
        List<Integer> topK = new ArrayList<>();

        for (int num : nums) {
            if (freqs.containsKey(num)) {
                int temp = freqs.get(num);
                temp++;
                freqs.put(num, temp);
            } else {
                freqs.put(num, 1);
            }
        }

        for (Integer key : freqs.keySet()) {
            freqBucket.get(freqs.get(key)).add(key);
        }

        for (int i = freqBucket.size() - 1; i > 0; i--) {
            if (freqBucket.get(i).size() != 0 && k > 0) {
                for (int j = 0; j < freqBucket.get(i).size(); j++) {
                    topK.add(freqBucket.get(i).get(j));
                    k--;
                }
            }

        }

        int[] topKArray = new int[topK.size()];
        for (int i = 0; i < topK.size(); i++) {
            topKArray[i] = topK.get(i);
        }

        return topKArray;
    }

    public static int[] topKFrequentMyn(int[] nums, int k) {
        HashMap<Integer, Integer> freqs = new HashMap<>();
        List<Integer> freqValues = new ArrayList<>();
        List<Integer> topK = new ArrayList<>();

        for (int num : nums) {
            if (freqs.containsKey(num)) {
                int temp = freqs.get(num);
                temp++;
                freqs.put(num, temp);
            } else {
                freqs.put(num, 1);
            }
        }

        for (Integer key : freqs.keySet()) {
            freqValues.add(freqs.get(key));
        }

        while (k > 0) {
            int max = max(freqValues);

            for (Integer key : freqs.keySet()) {
                if (freqs.get(key) == max) {
                    freqs.remove(key);
                    topK.add(key);
                    break;
                }
            }

            for (int i = 0; i < freqValues.size(); i++) {
                if (freqValues.get(i) == max) {
                    freqValues.remove(i);
                    break;
                }
            }

            k--;
        }

        int[] topKArray = new int[topK.size()];
        for (int i = 0; i < topK.size(); i++) {
            topKArray[i] = topK.get(i);
        }

        return topKArray;
    }

    public static int max(List<Integer> nums) {
        int max = nums.get(0);
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

}