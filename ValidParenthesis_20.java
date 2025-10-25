import java.util.HashMap;
import java.util.Stack;

public class ValidParenthesis_20 {

    public static void main(String[] args) {
        new ValidParenthesis_20();
    }

    public ValidParenthesis_20() {
        System.out.println(isValid("([]"));
    }

    public boolean isValid(String s) {

        if (s.length() <= 1) {
            return false;
        } else if (s.length() == 2) {
            return s.equals("()") || s.equals("{}") || s.equals("[]");
        }

        HashMap <Character,Character> brackets = new HashMap<>();
        brackets.put('(', ')');
        brackets.put('[', ']');
        brackets.put('{', '}');

        Stack <Character> stack = new Stack<>();

        for (char bracket : s.toCharArray()) {
            if(bracket == '(' || bracket == '{' || bracket == '['){
                stack.push(bracket);
            }
            else if (brackets.containsKey(bracket) && stack.peek() == brackets.get(bracket)){
                stack.pop();
            }
            else{
                return false;
            }
        }

       return true;
    }
}
