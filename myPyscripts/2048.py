#! python3

# game on webpage: 'https://gabrielecirulli.github.io/2048/'
# play the game automatically by the program, with very simple strategy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome()
dr.get('https://gabrielecirulli.github.io/2048/')
#dr.maximize_window()

htmlElem = dr.find_element_by_css_selector('html')
overMsg = dr.find_element_by_css_selector('.game-message')

key = Keys.LEFT
count = 0
while not overMsg.is_displayed():
    tiles = dr.find_elements_by_css_selector('.tile')

    # build the model of tiles
    # matrix = [[0 for col in range(4)] for row in range(4)]
    # or
    matrix = [[0] * 4 for row in range(4)]
    
    for tile in tiles:
        # tileclass example:
        # 'tile tile-2 tile-position-1-2 tile-new'
        tileclass = tile.get_attribute('class')
#        print(tileclass, end = '  >>  ')

        # tileclasses example:
        # ['tile', 'tile-2', 'tile-position-1-2', 'tile-new']
        tileclasses = tileclass.split()
#        print(tileclasses[1], tileclasses[2])

        # tileclasses[1] indicates the number in the tile,
        # like 'tile-2'. need to split it, take the 2nd element
        # and convert the 2nd element to digit 
        number = int(tileclasses[1].split('-')[1])

        # tileclasses[2], like 'tile-position-1-2', indicates
        # the position: column(=1) and row(=2)
        position = tileclasses[2].split('-')
        col = int(position[2])
        row = int(position[3])
        matrix[row-1][col-1] = number
#        print('column=', col,' row=', row,' is', number)
        
# print the matrix and pause for observation
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
    input('Press any key to continue ...')

# TODO: key determination.
# at the moment, simply change key in sequence: UP-RIGHT-DOWN-LEFT
    if key == Keys.UP:
        key = Keys.RIGHT
    elif key == Keys.RIGHT:
        key = Keys.DOWN
    elif key == Keys.DOWN:
        key = Keys.LEFT
    elif key == Keys.LEFT:
        key = Keys.UP

    htmlElem.send_keys(key)
    count = count + 1

#dr.quit()
