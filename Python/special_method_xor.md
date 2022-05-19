# Special Method XOR   
The trick is to swap two items without using any helper variables other than the index.  
Example:   
```python
>> initial_list = [1, 2, 3, 4, 5, 6]
>> swapped_list = [initial_list[i^1] for i in range(len(initial_list))]
>> swapped_list
[2, 1, 4, 3, 6, 5]
```   
The bitwise XOR with 1 makes the result be i+1 or i-1.   
```python
>> 0^1   # 0b0^0b1
1  # 0b1
>> 1^1   # 0b1^0b1
0  # 0b0
>> 2^1   # 0b10^0b1
3  # 0b11
>> 3^1   # 0b11^0b1
2  # 0b10
>> 4^1   # 0b100^0b1
5  # 0b101
>> 5^1   # 0b101^0b1
4  # 0b100
```   

I found it very fun.