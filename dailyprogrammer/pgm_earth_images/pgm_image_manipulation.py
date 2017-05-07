    import sys
    import math
    ### transformaitons, input pgm file -> output pgm file
    ### take in ogm file and run suggested transformaitons

    # Open file and read image height and width
    # make list of lists where each list is a row of png values
    # have methods set up for dealing with the original 4
    # iterate through input commands and run on list
    # write new image to new file

    BRIGHTEN_VALUE = 25

    def main():
        original = sys.argv[2]
        new = sys.argv[3]
        origianl_file = open('{}'.format(original), 'r')
        first_line = origianl_file.readline()
        pgm_verify, width, height, max_pgm_value = first_line.split()
        width, height, max_pgm_value = int(width), int(height), int(max_pgm_value)
        if pgm_verify != 'P2':
            return 'Could not find PGM file tag'
        color_values = list()
        for row in range(height):
            color_values.append(list())
            for column in range(width):
                color_values[row].append(origianl_file.readline().strip())
        origianl_file.close()
        operations = sys.argv[1]
        for letter in operations:
            if letter == 'H':
                width, height, color_values = flip_horizontal(width, height, color_values)
            elif letter == 'V':
                width, height, color_values = flip_vertical(width, height, color_values)
            elif letter == 'R':
                width, height, color_values = rotate_90_right(width, height, color_values)
            elif letter == 'L':
                width, height, color_values = rotate_90_left(width, height, color_values)
            elif letter == 'E':
                width, height, color_values = enlarge(width, height, color_values)
            elif letter == 'S':
                width, height, color_values = shrink(width, height, color_values)
            elif letter == 'N':
                width, height, color_values = negative(width, height, color_values, max_pgm_value)
            elif letter == 'B':
                width, height,  color_values = brighten(width,height, color_values, max_pgm_value)
            elif letter == 'D':
                width, height, color_values = darken(width, height, color_values)
        new_file = open("{}".format(new), 'w')
        new_file.write('P2 {} {} {}\n'.format(width, height, max_pgm_value))
        for i in range(height):
            for a in range(width):
                new_file.write('{}\n'.format(color_values[i][a]))
        new_file.close()



    def flip_horizontal(width, height, color_values):
        for row in range(height):
            for value in range(math.floor(width/2)):
                color_values[row][value], color_values[row][width-1-value] = color_values[row][width-1-value], color_values[row][value]
        return width, height, color_values


    def flip_vertical(width, height, color_values):
        for row in range(math.floor(height/2)):
            color_values[row], color_values[height-row-1] = color_values[height-row-1], color_values[row]
        return width, height, color_values


    def rotate_90_right(width, height, color_values):
        new_values = list()
        for column in range(width):
            new_values.append(list())
            for row in range(height):
                new_values[column].append(color_values[height-row-1][column])
        return height, width, new_values

    def rotate_90_left(width, height, color_values):
        new_values = list()
        for column in range(width):
            new_values.append(list())
            for row in range(height):
                new_values[column].append(color_values[row][width - column - 1])
        return height, width, new_values

    def enlarge(width, height, color_values):
        for row in range(height):
            color_values[row] = [val for val in color_values[row] for _ in (0,1)]
        color_values = [val for val in color_values for _ in (0,1)]
        width *= 2
        height *= 2
        return width, height, color_values

    def shrink(width, height, color_values):
        for row in range(height):
            color_values[row] = color_values[row][::2]
        color_values = color_values[::2]
        width, height = math.ceil(width/2), math.ceil(height/2)
        return width, height, color_values 

    def negative(width, height, color_values, max_pgm_value):
        for row in range(height):
            for value in range(width):
                color_values[row][value] = abs(max_pgm_value - int(color_values[row][value]))
        return width, height, color_values

    def brighten(width, height, color_values, max_pgm_value):
        for row in range(height):
            for value in range(width):
                if (BRIGHTEN_VALUE + int(color_values[row][value])) > max_pgm_value:
                    color_values[row][value] = max_pgm_value
                else:
                    color_values[row][value] = BRIGHTEN_VALUE + int(color_values[row][value])
        return width, height, color_values

    def darken(width, height, color_values):
        for row in range(height):
            for value in range(width):
                if (int(color_values[row][value]) - BRIGHTEN_VALUE) < 0:
                    color_values[row][value] = 0
                else:
                    color_values[row][value] = int(color_values[row][value]) - BRIGHTEN_VALUE
        return width, height, color_values    
                



    if __name__ == '__main__':
        main()