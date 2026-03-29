class MinStack {

    private Stack<Integer> stack;
     private Stack<Integer> min_stack;

    public MinStack() {
        stack = new Stack<>();
        min_stack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (min_stack.size() > 0) {
            int curr_min = min_stack.peek();
            if (curr_min > val) {
                min_stack.push(val);
            } else {
                min_stack.push(curr_min);
            }
        } else {
            min_stack.push(val);
        }
    }
    
    public void pop() {
        stack.pop();
        min_stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min_stack.peek();
    }
}
