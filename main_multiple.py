from pacman import pacman

if __name__ == '__main__':
    no_of_tests = 10
    for i in range(1, no_of_tests + 1):
        my_str = 'test%d.txt' % (i)
        final_pos_x, final_pos_y, coins_collected = pacman(my_str)
        print "---- Test no %d : ----\nThe final position is (%d, %d).\nThe total no. of coins collected are %d.\n" % (i, final_pos_x, final_pos_y, coins_collected)
