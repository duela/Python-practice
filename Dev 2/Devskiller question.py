# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 04:00:57 2022

@author: yinku

MasterMind is a game for two players. One of them, Designer, selects a secret code. The other, Breaker, tries to break it. A code is no more than a row of colored dots. At the beginning of a game, the players agree upon the length N that a code must have and upon the colors that may occur in a code.

In order to break the code, Breaker makes a number of guesses, each guess itself being a code. After each guess Designer gives a hint, stating to what extent the guess matches his secret code.

In this problem you will be given a secret code s1 . . . sn and a guess g1 . . . gn, and the method you implement will have to determine the hint. A hint consists of a pair of numbers determined as follows.

A match is a pair (i, j), 1 ≤ i ≤ n and 1 ≤ j ≤ n, such that si = gj . Match (i, j) is called strong when i = j, and is called weak otherwise.

The hint is a tuple that consists of the number of strong matches followed by the number of weak matches. Note that these numbers are uniquely determined by the secret code and the guess. If the hint turns out to be (n, 0), then the guess is identical to the secret code.

The signature of your function should be:

You may implement other functions called by your  function if you wish.

Input Spec
Your method should take two inputs. The first is the secret code presented as a list of N integers.

Example:

Each of these integers is limited to the range 1 to 9.

The second input is a guess Which is also represented as N integers, each in the range 1 to 9.

Example:

Output Spec
The method should output the hint that that would be generated for the guess. The hint will be a tuple representing a pair of integers. Example:

Note: If the user provides a list containing a number outside of the 1-9 range (either for the secret code or guess), the output should be .

Sample Input & Output
Sample number	Input (List[int], List[int])	Output (tuple)
1		


"""

