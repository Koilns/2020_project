
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort


def write_rank(result, list, name, n):
    result.write(name+" rank:\n")
    l = 31
    if len(list) < 31:
        l = len(list)
    for i in range(1, l):
        result.write(
            str(i)+": 《"+str(list[i][6]) + "》 "+str(list[i][2])+"  "+str(list[i][n])+name+"\n")
    result.write("\n")


def main():
    total_list = []
    result = open('Rank_result.txt', 'w')
    language_list = ["python", "c++", "C", "java", "objective-c",
                     "php", "basic", "ruby"]
    result.write("Rank:\n")
    for i in range(len(language_list)):
        result.write(language_list[i]+" rank:\n")
        path = language_list[i]+".txt"
        list = []
        with open(path, encoding='utf-8')as f:
            for line in f:
                list.append(eval(line))
                total_list.append(eval(line))
        view_rank = sorted(list, key=lambda list: list[3], reverse=True)
        like_rank = sorted(list, key=lambda list: list[4], reverse=True)
        comment_rank = sorted(list, key=lambda list: list[5], reverse=True)
        write_rank(result, view_rank, "view", 3)
        write_rank(result, like_rank, "like", 4)
        write_rank(result, comment_rank, "comment", 5)

    result.write("Total rank:\n")
    view_rank = sorted(
        total_list, key=lambda total_list: total_list[3], reverse=True)
    like_rank = sorted(
        total_list, key=lambda total_list: total_list[4], reverse=True)
    comment_rank = sorted(
        total_list, key=lambda total_list: total_list[5], reverse=True)
    write_rank(result, view_rank, "view", 3)
    write_rank(result, like_rank, "like", 4)
    write_rank(result, comment_rank, "comment", 5)


if __name__ == '__main__':
    main()
