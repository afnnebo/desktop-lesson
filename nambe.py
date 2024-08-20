First = (123)
Second = (456)
Third = (789)
name = ("First", "Second", "Third")
if name != First != Second != Third:
    print(0)
elif name == First == Second == Third:
    print(3)
elif name != First == Second == Third:
    print(2)
#
#
First = (42)
Second = (69)
Third = (42)
name = ("First", "Second", "Third")
if name != First != Second != Third or name == First != Second != Third:
    print(2)
elif name == First == Second == Third:
    print(3)
elif name != First != Second != Third:
    print(0)