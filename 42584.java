package com.company;

import java.util.Stack;

public class Main {

    public static void main(String[] args) {
//	    int[] prices = {1, 2, 3, 2, 3};
//        int[] prices = {5, 4, 3, 2, 1};
        int[] prices = {1, 2, 3, 2, 1, 2, 3, 2};

	    Solution s = new Solution();

	    int[] result = s.solution(prices);
	    for(int r : result){
            System.out.printf("%d ",r);
        }
    }
}

class Solution {
    static class Tuple {
        Integer i, v;

        Tuple(Integer a, Integer b){
            this.i = a;
            this.v = b;
        }
    }

    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        Stack<Tuple> stack = new Stack<Tuple>();
        for(int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && stack.peek().v > prices[i]){
                Tuple t = stack.pop();

                answer[t.i] = i - t.i;

                System.out.printf("%d %d\n", i, t.i);
            }

            stack.push(new Tuple(i, prices[i]));
        }

        while (!stack.empty()){
            Tuple t = stack.pop();

            answer[t.i] = prices.length - t.i - 1;
        }

        return answer;
    }
}