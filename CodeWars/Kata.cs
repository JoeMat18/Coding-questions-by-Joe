using System;
using System.Linq;

public class Kata
{
    public static string GoodVsEvil(string good, string evil)
    {
        int[] goodWorth = { 1, 2, 3, 3, 4, 10 };
        int[] evilWorth = { 1, 2, 2, 2, 3, 5, 10 };
        
        int[] goodCount = good.Split(' ').Select(int.Parse).ToArray();
        int[] evilCount = evil.Split(' ').Select(int.Parse).ToArray();
        

        int goodPower = goodCount.Zip(goodWorth, (count, worth) => count * worth).Sum();
        int evilPower = evilCount.Zip(evilWorth, (count, worth) => evil * worth).Sum() ;

        if (goodPower > evilPower)
        {
            return "Battle Result: Good triumphs over Evil";
        }
        else if (evilPower > goodPower)
        {
            return "Battle Result: Evil eradicates all trace of Good";
        }
        else
        {
            return "Battle Result: No victor on this battle field";
        }
    }
}



























