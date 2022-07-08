# pip3 install tabulate
from tabulate import tabulate


table = []
headers = ["#", "Report Name", "ID"]

table.append([1, "A's Report", "123456"])
table.append([2, "B's Report", "654321"])
table.append([3, "C's Report", "987654"])

print(tabulate(table,headers))