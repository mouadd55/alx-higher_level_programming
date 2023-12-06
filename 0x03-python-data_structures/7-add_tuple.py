#!/usr/bin/python3
def add_tuple(tuple1=(), tuple2=()):
    tuple1 = tuple1 + (0, 0)
    tuple2 = tuple2 + (0, 0)
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
