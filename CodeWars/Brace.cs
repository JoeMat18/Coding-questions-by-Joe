using System;
using System.Linq;
using System.Collections.Generic;

public class Brace {

    public static bool validBraces(String braces)
    {
        Dictionary<char, char> matchingBraces = new Dictionary<char, char>()
        {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

    Stack<char> stack = new Stack<char>();
    
    foreach(char ch in braces)
    {
        if (matchingBraces.ContainsValue(ch))
        {
            stack.Push(ch);
        }
        else if (matchingBraces.ContainsKey(ch))
        {
            if (stack.Count == 0 || stack.Pop() != matchingBraces[ch])
            {
                return false;
            }
        }
    }
    return stack.Count == 0;

    }
}