import pygame

size_x, size_y = input(), input()
if size_x.isdigit() == False or size_y.isdigit() == False:
    print("Неправильный формат ввода")
size = size_x, size_y = int(size_x), int(size_y)
pygame.init()
surface = pygame.display.set_mode(size)
pygame.display.set_caption("Крест")
pygame.draw.line(surface, (255, 255, 255), (0, 0), (size_x, size_y), width=5)
pygame.draw.line(surface, (255, 255, 255), (0, size_x), (size_y, 0), width=5)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()