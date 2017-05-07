#! python3

# You can have lists, within lists, within lists, within lists....
# An example of a two dimmensional list

x = [[5,6],[6,7],[1,2],[4,5]]
print(x[0] == [5,6])
print(x[1][1] == 7)



y = [[[5,7],[6,6]],[[6,6],[7,8]],[5,6]]
print(y[1][1][0] == 7)

# To make that list look better you can
     
z = [
    [[5,7],[6,6]],
    [[6,6],[7,8]],
    [5,6]
    ]
