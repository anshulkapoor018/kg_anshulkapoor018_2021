#!/usr/bin/env python

"""
Assessment for Software Engineer Intern position at Kargo

Question:

Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.

For example, given ​s1 = abc​ and ​s2 = bcd,​ print "​true" into stdout​ since we can map each character
in "abc" to a character in "bcd".

Given ​s1 = foo​ and ​s2 = bar,​ print "f​alse"​ since the character ‘o’ cannot map to two characters.
But given ​s1 = bar a​ nd ​s2 = foo​, print "true​"​ since each character
in "bar" can be mapped to a character in "foo"
"""

__author__ = "Anshul Kapoor"


def one_to_one_mapping(string1, string2):
    if len(string1) != len(string2):
        return False
    mapping_dictionary = dict()  # To store the mapping of each character from string 1 to string 2
    for i, j in zip(string1, string2):
        if i not in mapping_dictionary:
            """ Checks if character is present in dictionary 
                and append it as a key and map its value """
            mapping_dictionary[i] = j
        else:
            """ Checks that character is already present as a 'key', 
            means it is already mapped to a Value and cannot be 
            mapped to two characters at once."""
            return False

    # print(a)
    return True


print(one_to_one_mapping("bar", "foo"))
