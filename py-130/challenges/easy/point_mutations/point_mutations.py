"""
Write a program that can calculate the Hamming distance between two DNA strands.

A mutation is simply a mistake that occurs during the creation or copying of a nucleic acid, in particular DNA. 
Because nucleic acids are vital to cellular functions, mutations tend to cause a ripple effect throughout the cell. 
Although mutations are technically mistakes, a very rare mutation may equip the cell with a beneficial attribute. 
In fact, the macro effects of evolution are attributable to the accumulated result of beneficial microscopic mutations 
over many generations.

The simplest and most common type of nucleic acid mutation is a point mutation, which replaces one base with another 
at a single nucleotide.

By counting the number of differences between two homologous DNA strands taken from different genomes with a common 
ancestor, we get a measure of the minimum number of point mutations that could have occurred on the evolutionary path 
between the two strands.

This is called the Hamming distance.

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

The Hamming distance between these two DNA strands is 7.

The Hamming distance is only defined for sequences of equal length. 
If you have two sequences of unequal length, you should compute the Hamming distance over the shorter length.
"""

"""
P:
Given two DNA sequences (strings), compute the Hamming distance.

Rules:
    - The Hamming distance is the number of point mutations between both strings
    - A point mutation is a discrepancy in base between two strands at the same location
    - A base is A, G, C, or T
    - If both sequences are of unequal length, compute the distance over the shorter length
        - Match up both sequences by matching index 0
    - We should create a class DNA that is initialized with a string representing the DNA strand
    - The DNA class should have a method `hamming_distance` that takes in one argument, the second string

E:
AAACTAGGGG
AGGCTAGCGGTAGGAC
 ^^    ^  ------(ignored) => 3 mutations

D:
    Input: 2 strings, one from instance variable in DNA class, another passed in
    Output: Integer (number of mutations)
    Intermediate:
        - String: DNA strands of "correct" length based on len of smallest input
        - Boolean: Check if chars are same at a given index
        - Range: Iterate through indices of both strings

High-level strategies:
    - Truncate strings to the same length. Compare chars at each index per string. Count # of discrepancies between chars

A:
    - Constructor (__init__)
        - Set instance variable `strand` to value passed in
    - `hamming_distance`
        - Input: Second strand (string)
        - Set counter to 0
        - Truncate one strand based on shortest length => *truncate_strands*
        - For each idx from 0 to length of strands
            - Get chars in both strands
            - If not equal, increment counter
        - Return counter

*truncate_strands*
    - Input: 2 strings
    - Output: 2 strings (truncated as needed)
    - A:
        - Get length of shortest strand
        - Truncate each strand to match the shortest length
        - Return new strings
"""

class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, comp_strand):
        counter = 0
        strand1, strand2 = self._truncate_strands(comp_strand)
        for idx in range(len(strand1)):
            char1 = strand1[idx]
            char2 = strand2[idx]
            counter += (char1 != char2)

        return counter

    def _truncate_strands(self, comp_strand):
        len_shortest = min(len(self.strand), len(comp_strand))
        return (self.strand[0:len_shortest], comp_strand[0:len_shortest])

# Reflection
# Can use a generator with the sum function + use zip to automatically shorten the strands without a helper:
# return sum(1 for char1, char2 in zip(self.strand, comp_strand) if char1 != char2)