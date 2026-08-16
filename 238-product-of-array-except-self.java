class ProductOfArrayExceptSelf_238 {

    public static void main(String[] args) {
        int nums[] = { 5, 7, 2, 3 };
        int answer[] = productExceptSelf(nums);
        for (int i : answer) {
            System.out.println(i);
        }
    }

    public static int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] prefixProds = new int[nums.length];
        int[] suffixProds = new int[nums.length];

        int preProd = 1;
        int sufProd = 1;
        for (int i = 0; i < nums.length; i++) {
            preProd *= nums[i];
            prefixProds[i] = preProd;
            sufProd *= nums[nums.length - 1 - i];
            suffixProds[nums.length - 1 - i] = sufProd;
        }

        for (int i = 0; i < nums.length; i++) {
            if (i - 1 > -1 && i + 1 < nums.length) {
                answer[i] = prefixProds[i - 1] * suffixProds[i + 1];
            } else if (i == 0) {
                answer[i] = suffixProds[i + 1];
            } else {
                answer[i] = prefixProds[i - 1];
            }
        }

        return answer;
    }

    public static int[] productExceptSelfDivisionOperator(int[] nums) {
        int[] answer = new int[nums.length];

        int zero_count = 0;
        int all_prod = 1;
        for (int num : nums) {
            if (num == 0) {
                zero_count++;
            } else {
                all_prod *= num;
            }
        }

        if (zero_count > 1) {
            return answer;
        } else if (zero_count == 1) {
            for (int i = 0; i < answer.length; i++) {
                if (nums[i] == 0) {
                    answer[i] = all_prod;
                }
            }
        } else {
            for (int i = 0; i < answer.length; i++) {
                answer[i] = all_prod / nums[i];
            }
        }

        return answer;
    }
}
