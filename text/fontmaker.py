import pygame

pygame.init()
canvas = pygame.display.set_mode((100, 100))
pygame.mouse.set_visible(False)
char_set = "QWERTYUIOP ASDFGHJKL ZXCVBNM \
1234567890-= !$%^&*()_+"
char_set += "[]{} ;'#:@~ ,./<>?\"\\"
font_dictionary = dict()
for letter in char_set:  # main dictionary creation loop
    canvas.fill((0, 0, 0))  # clear the canvas
    fontObj = pygame.font.Font(
        '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 9)
    textSurface = fontObj.render(
        letter, True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurface.get_rect()
    canvas.blit(textSurface, textRectObj)
    pygame.display.update()  # display the letter
    letter_data = []
    for y in range(8):  # check each row of
        # the letter on canvas
        letter_row = []
        for x in range(8):
            # each x position of letter on canvas
            colour = canvas.get_at((x, y + 2))
            if colour[0] > 200:
                letter_row.append(1)
            elif colour[0] > 100:
                letter_row.append(0.75)
            elif colour[0]:
                letter_row.append(0.15)
            else:
                letter_row.append(0)
            letter_data.append(letter_row)
        for x in range(7, -1, -1):  # Trim excess space on right of letter
            column = [letter_data[y][x] for y in range(8)]
            if max(column) == 0:
                for i in range(8):
                    del letter_data[i][x]
    font_dictionary[letter] = letter_data
font_dictionary[' '] = [[0] * 4] * 8  # space gets trimmed to empty otherwise
font_dictionary['@'] = [[0, 1, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1],
                        [1, 1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0],
                        [0] * 7]
pygame.quit()
print(font_dictionary)
