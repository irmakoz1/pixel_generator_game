import pygame
import random
import heapq

# Constants
WIDTH, HEIGHT = 500, 500
height=300
PIXEL_SIZE = 10
ROWS, COLS = WIDTH // PIXEL_SIZE, HEIGHT // PIXEL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Informed Search Pixel Generator")
font = pygame.font.Font(None, 15)

# Button Setup
button_rect = pygame.Rect(20, HEIGHT - 50, 100, 30)
button_increment_rect = pygame.Rect(200, HEIGHT - 50, 100, 30)

# Global pixel count
pixel_limit = 1

def heuristic(x, y):
    """Example heuristic function to influence pixel placement."""
    return abs(x - ROWS // 2) + abs(y - COLS // 2)  # Manhattan distance to center

def generate_image(limit):
    """Generates an image using informed search (A* like)."""
    pixels = []
    visited = set()
    pq = []
    
    # Start from a random point
    start_x, start_y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
    heapq.heappush(pq, (0, start_x, start_y))
    
    while pq and len(pixels) < limit:
        _, x, y = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        pixels.append((x, y, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        
        # Add neighbors with heuristic priority
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in visited:
                priority = heuristic(nx, ny) + random.randint(0, 5)
                heapq.heappush(pq, (priority, nx, ny))
    
    return pixels

def draw_pixels(pixels):
    """Draws the generated pixels on the screen."""
    for x, y, color in pixels:
        pygame.draw.rect(screen, color, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def main():
    global pixel_limit
    running = True
    pixels = generate_image(pixel_limit)
    
    while running:
        screen.fill(WHITE)
        draw_pixels(pixels)
        
        # Draw buttons
        pygame.draw.rect(screen, BLACK, button_rect)
        text = font.render("New Image", True, WHITE)
        screen.blit(text, (30, HEIGHT - 45))
        
        pygame.draw.rect(screen, BLACK, button_increment_rect)
        increment_text = font.render("Increase Pixels", True, WHITE)
        screen.blit(increment_text, (210, HEIGHT - 45))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pixels = generate_image(pixel_limit)
                elif button_increment_rect.collidepoint(event.pos):
                    pixel_limit += 40
                    pixels = generate_image(pixel_limit)
    
    pygame.quit()

if __name__ == "__main__":
    main()
