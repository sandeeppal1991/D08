#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(pledge_histogram,value):
    list_of_found_keys = []
    list_of_keys = pledge_histogram.keys()
    for each_key in list_of_keys:
        if(pledge_histogram[each_key] == value):
            list_of_found_keys.append(each_key)
    return list_of_found_keys


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_new(pledge_list):
    dict_histogram = {}
    for each_word in pledge_list:
        dict_histogram[each_word] = dict_histogram.get(each_word,0) + 1
    return dict_histogram


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    with open("pledge.txt","r") as pledge:
        pledge_list = pledge.read().split()
    return pledge_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
    print(reverse_lookup_new(histogram_new(get_pledge_list()), 1))
    print(reverse_lookup_new(histogram_new(get_pledge_list()), 9))
    print(reverse_lookup_new(histogram_new(get_pledge_list()), "Python"))

if __name__ == '__main__':
    main()
