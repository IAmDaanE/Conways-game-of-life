import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conways game of life")
clock = pygame.time.Clock()

cell_size = 20

num_hor_cells = int(WINDOW_WIDTH / cell_size)
num_vert_cells = int(WINDOW_HEIGHT / cell_size)

cells = []
for i in range(int(WINDOW_WIDTH / cell_size)):
    cells.append([])
    for j in range(int(WINDOW_HEIGHT / cell_size)):
        cells[i].append(False)

current_mode = "selecting"

running = True

def count_surrounding_cells(x, y):
    count = 0

    if y != 0:
        if cells[x][y - 1]:
            count += 1
    if y != num_vert_cells - 1:
        if cells[x][y + 1]:
            count += 1
    if x != 0:
        if cells[x - 1][y]:
            count += 1
    if x != num_hor_cells - 1:
        if cells[x + 1][y]:
            count += 1

    if y != 0 and x != 0:
        if cells[x - 1][y - 1]:
            count += 1
    if y != 0 and x != num_hor_cells - 1:
        if cells[x + 1][y - 1]:
            count += 1
    if y != num_vert_cells - 1 and x != 0:
        if cells[x - 1][y + 1]:
            count += 1
    if y != num_vert_cells - 1 and x != num_hor_cells - 1:
        if cells[x + 1][y + 1]:
            count += 1

    return count

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_mode == "selecting":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                cells[int(x / cell_size)][int(y / cell_size)] ^= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print("lkdjqmlsdkjmqsdlkj")
                    current_mode = "simulating"
    
    if current_mode == "simulating":
        for q in range(len(cells)):
            for p in range(num_vert_cells):
                if not cells[q][p] and count_surrounding_cells(q, p) == 3:
                    cells[q][p] = True
                if cells[q][p]:
                    if count_surrounding_cells(q, p) < 2:
                        cells[q][p] = False
                    elif count_surrounding_cells(q, p) > 3:
                        cells[q][p] = False

    if True: #displaying
        screen.fill((255,255,255))

        for i in range(int(WINDOW_WIDTH / cell_size)):
            pygame.draw.rect(screen, (0,0,0), (i * cell_size, 0, 1, WINDOW_HEIGHT))
        pygame.draw.rect(screen, (0,0,0), (799, 0, 1, WINDOW_HEIGHT))

        for j in range(int(WINDOW_HEIGHT / cell_size)):
            pygame.draw.rect(screen, (0,0,0), (0, j * cell_size, WINDOW_WIDTH, 1))
        pygame.draw.rect(screen, (0,0,0), (0, 599, WINDOW_WIDTH, 1))

        for q in range(len(cells)):
            for p in range(int(WINDOW_HEIGHT / cell_size)):
                if cells[q][p]:
                    pygame.draw.rect(screen, (0,0,0), (q * cell_size, p * cell_size, cell_size, cell_size))              
    pygame.display.update()
    if current_mode == "simulating":
        clock.tick(14)
    else:
        clock.tick(60)