// A Java program to solve Project Euler #70.
import java.util.*;
public class euler70 {

    static ArrayList<Integer> sieve(int n){
        //Return all primes up to n. Sieve of Eratosthenes.

        Boolean[] prime = new Boolean[n];
        Arrays.fill(prime, Boolean.TRUE);
        int p = 2;
        while (p*p <= n) {
            if (prime[p]) {
                int i = p*p;
                while(i < n) {
                    prime[i] = false;
                    i += p;
                }
            }
            p += 1;
        }
        ArrayList<Integer> primes = new ArrayList<>();
        p = 2;
        while (p < n) {
            if (prime[p]) {
                primes.add(p);
            }
            p += 1;
        }
        return primes;
    }

    static Map<Integer,ArrayList<Integer>> primeFactorsOfRange(int n){
        //Output a list of prime factors for each number from 2 to n.

        int k;
        ArrayList<Integer> v;
        ArrayList<Integer> primes = sieve(n);
        int i = 2;
        Map<Integer,ArrayList<Integer>> primeDivisors = new HashMap<>();
        while (i <= n) {
            primeDivisors.put(i,new ArrayList<Integer>());
            i += 1;
        }
        for (int prime : primes) {
            i = 2;
            while (i * prime <= n) {
                k = i * prime;
                v = primeDivisors.get(k);
                v.add(prime);
                primeDivisors.put(k,v);
                i += 1;
            }
        }
        return primeDivisors;

    }

    static Map<Integer,Integer> phis(int n) {
        //Output a list of phi(n) for 2 to n.

        Map<Integer, Integer> ps = new HashMap<>();
        Map<Integer,ArrayList<Integer>> factors = primeFactorsOfRange(n);
        for (Map.Entry<Integer,ArrayList<Integer>> mapElement : factors.entrySet()) {
            int k = mapElement.getKey();
            ArrayList<Integer> v = mapElement.getValue();
            if (v.size() == 0) {
                ps.put(k, k-1);
            } else {
                double newk = k;
                for (int factor : v) {
                    double factorFloat = (double) factor;
                    newk *= 1 - (1/factorFloat);
                }
                int newkInt = (int) newk;
                ps.put(k,newkInt);
            }   
        }
        return ps;
        }
    
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        int ans = 0;
        double minRatio = 1000000000;
        Map<Integer,Integer> ps = phis((int)Math.pow(10,7));
        for (Map.Entry<Integer,Integer> mapElement : ps.entrySet()) {
            int k = mapElement.getKey();
            int v = mapElement.getValue();
            String stringk = String.valueOf(k);
            String stringv = String.valueOf(v);
            char[] kchars = stringk.toCharArray();
            char[] vchars = stringv.toCharArray();
            Arrays.sort(kchars);
            Arrays.sort(vchars);
            stringk = new String(kchars);
            stringv = new String(vchars);
            if (stringk.equals(stringv)) {
                if ((double)k/(double)v < minRatio) {
                    minRatio = (double)k/(double)v;
                    ans = k;
                }
            }

        }
        System.out.println(ans);
        System.out.println((System.currentTimeMillis()-start));
    }
}
