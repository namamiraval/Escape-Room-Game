import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room - Sci-Fi Horror")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)  # Sky Blue
HIGHLIGHT = (0, 255, 0)  # Green highlight for selection
RED = (255, 0, 0)  
GREEN = (0, 255, 0)

# Font settings
font = pygame.font.Font(None, 40)

# Load and resize images
room1 = pygame.image.load("room1.png")
room1 = pygame.transform.scale(room1, (WIDTH, HEIGHT))  

room1_puzzle = pygame.image.load("room1_puzzle.png")
room1_puzzle = pygame.transform.scale(room1_puzzle, (WIDTH, HEIGHT))  

room2 = pygame.image.load("room2.png")
room2 = pygame.transform.scale(room2, (WIDTH, HEIGHT))  

room2_puzzle = pygame.image.load("room2_puzzle.png")
room2_puzzle = pygame.transform.scale(room2_puzzle, (WIDTH, HEIGHT))  

# Load Evolution Puzzle Images
human_stages = [
    pygame.image.load("stage1_primitive.png"),
    pygame.image.load("stage2_modern.png"),
    pygame.image.load("stage3_mutated.png"),
    pygame.image.load("stage4_alien.png"),
]
# Resize images for consistent display
human_stages = [pygame.transform.scale(img, (120, 160)) for img in human_stages]

# Evolution Puzzle Images
def evolution_puzzle():
    shuffled_positions = [(150, 250), (300, 250), (450, 250), (600, 250)]
    random.shuffle(shuffled_positions)

    correct_order = [0, 1, 2, 3]  
    clicked_order = []

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(room1_puzzle, (0, 0))  

        # Draw black semi-transparent box for text
        rect_surface = pygame.Surface((700, 60))  
        rect_surface.set_alpha(200)  
        rect_surface.fill(BLACK)
        screen.blit(rect_surface, (50, 50))  # Positioned at the top

        # Render text
        text = font.render("Click the images in the correct order of human evolution.", True, BLUE)
        text_rect = text.get_rect(center=(WIDTH // 2, 80))
        screen.blit(text, text_rect)

        positions_dict = {}
        for i, pos in enumerate(shuffled_positions):
            screen.blit(human_stages[i], pos)
            positions_dict[i] = pos  

            if i in clicked_order:
                pygame.draw.rect(screen, HIGHLIGHT, (pos[0] - 5, pos[1] - 5, 130, 170), 3)  

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                for i, pos in positions_dict.items():
                    rect = pygame.Rect(pos[0], pos[1], 120, 160)
                    if rect.collidepoint(x, y) and i not in clicked_order:
                        clicked_order.append(i)

                        if clicked_order != correct_order[: len(clicked_order)]:
                            clicked_order = []
                            break

                        if clicked_order == correct_order:
                            print("Puzzle Solved! Door Unlocks!")
                            return  

# Intro messages
intro_messages =
[
    "You wake up in a cold, sterile room.",
    "Your head is spinning. The air smells metallic.",
    "You have no memory of how you got here...",
    "But you know one thing – you need to escape.",
    "You spot a strange alien control panel nearby."
]

# Display Intro Screen
def intro_screen():
    for message in intro_messages:
        screen.fill(BLACK)
        screen.blit(room1, (0, 0))

        # Draw a black semi-transparent box
        rect_surface = pygame.Surface((700, 60))  
        rect_surface.set_alpha(200)  # Set transparency (0 = fully transparent, 255 = fully opaque)
        rect_surface.fill(BLACK)
        screen.blit(rect_surface, (50, HEIGHT // 2 - 30))  # Centered rectangle

        # Render text
        text = font.render(message, True, BLUE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()
        time.sleep(5)

    # Final instruction
    screen.fill(BLACK)
    screen.blit(room1, (0, 0))

    rect_surface = pygame.Surface((300, 50))
    rect_surface.set_alpha(200)
    rect_surface.fill(BLACK)
    screen.blit(rect_surface, (WIDTH // 2 - 150, HEIGHT // 2 + 30))

    text = font.render("Click to Continue", True, BLUE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(text, text_rect)
    
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  
 

# Room 1 - Evolution Puzzle
def evolution_puzzle():
    shuffled_positions = [(150, 250), (300, 250), (450, 250), (600, 250)]
    random.shuffle(shuffled_positions)

    correct_order = [0, 1, 2, 3]  # Correct order of human evolution
    clicked_order = []

    answer_correct = False
    error_message = ""

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(room1_puzzle, (0, 0))  # Background Image

        # Render Evolution Images
        positions_dict = {}
        for i, pos in enumerate(shuffled_positions):
            screen.blit(human_stages[i], pos)
            positions_dict[i] = pos  
            if i in clicked_order:
                pygame.draw.rect(screen, HIGHLIGHT, (pos[0] - 5, pos[1] - 5, 130, 170), 3)  # Highlight selected

        # Instruction Text with Black Box
        text = font.render("Click the images in the correct order of human evolution.", True, BLUE)
        text_rect = text.get_rect(center=(WIDTH // 2, 70))
        box_rect = text_rect.inflate(20, 10)  
        pygame.draw.rect(screen, BLACK, box_rect)  
        screen.blit(text, text_rect)

        # Display Success Message
        if answer_correct:
            success_text = font.render("Correct! The door unlocks!", True, HIGHLIGHT)
            success_rect = success_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
            pygame.draw.rect(screen, BLACK, success_rect.inflate(40, 20))
            screen.blit(success_text, success_rect)
            pygame.display.flip()
            time.sleep(2)  # Show message for 2 seconds
            return  

        # Display Error Message
        if error_message:
            error_text = font.render(error_message, True, (255, 0, 0))  # Red color for error
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
            pygame.draw.rect(screen, BLACK, error_rect.inflate(40, 20))
            screen.blit(error_text, error_rect)

        pygame.display.flip()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                for i, pos in positions_dict.items():
                    rect = pygame.Rect(pos[0], pos[1], 120, 160)
                    if rect.collidepoint(x, y) and i not in clicked_order:
                        clicked_order.append(i)

                        if clicked_order != correct_order[: len(clicked_order)]:
                            error_message = "Wrong order. Try again."
                            clicked_order = []  
                            break

                        if clicked_order == correct_order:
                            answer_correct = True  
 
# Room 2 - Riddle Challenge
def riddle_puzzle():
    question = "I can be cracked, made, told, and played. What am I?"
    options = ["A) A Code", "B) A Joke", "C) A Mirror", "D) A Puzzle"]
    correct_answer = 1  # Correct answer is "B) A Joke"

    selected_option = None
    answer_correct = False
    error_message = ""

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(room2_puzzle, (0, 0))  # Background Image

        # Riddle text
        text_surface = font.render(question, True, BLUE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 100))

        # Black Box behind the riddle text
        padding_x = 20  
        padding_y = 10  
        box_rect = pygame.Rect(
            text_rect.left - padding_x,
            text_rect.top - padding_y,
            text_rect.width + (padding_x * 2),
            text_rect.height + (padding_y * 2),
        )
        pygame.draw.rect(screen, BLACK, box_rect)  # Draw black box
        screen.blit(text_surface, text_rect)  # Render text on top

        # Answer choices
        option_positions = [(WIDTH // 2, 250), (WIDTH // 2, 330), (WIDTH // 2, 410), (WIDTH // 2, 490)]
        for i, option in enumerate(options):
            color = HIGHLIGHT if selected_option == i else BLUE
            option_text = font.render(option, True, color)
            option_rect = option_text.get_rect(center=option_positions[i])

            # Black Box behind the option text
            box_rect = pygame.Rect(
                option_rect.left - padding_x,
                option_rect.top - padding_y,
                option_rect.width + (padding_x * 2),
                option_rect.height + (padding_y * 2), )
            pygame.draw.rect(screen, BLACK, box_rect)  # Draw black box
            screen.blit(option_text, option_rect)  # Render text on top

        # Display Success Message
        if answer_correct:
            success_text = font.render("Correct! The door unlocks!", True, HIGHLIGHT)
            success_rect = success_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
            pygame.draw.rect(screen, BLACK, success_rect.inflate(40, 20))
            screen.blit(success_text, success_rect)
            pygame.display.flip()
            time.sleep(2)  # Show message for 2 seconds
            return  

        # Display Error Message
        if error_message:
            error_text = font.render(error_message, True, (255, 0, 0))  # Red color for error
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
            pygame.draw.rect(screen, BLACK, error_rect.inflate(40, 20))
            screen.blit(error_text, error_rect)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, pos in enumerate(option_positions):
                    text_width, text_height = font.size(options[i])
                    rect = pygame.Rect(pos[0] - text_width // 2, pos[1] - text_height // 2, text_width, text_height)
                    if rect.collidepoint(x, y):
                        selected_option = i
                        if i == correct_answer:
                            answer_correct = True  
                        else:
                            error_message = "Wrong answer. Try again."

# Room 3 Background
room3_puzzle = pygame.image.load("room3_puzzle.png")
room3_puzzle = pygame.transform.scale(room3_puzzle, (WIDTH, HEIGHT))

'''# List of possible words for the puzzle
word_choices = ["ESCAPE", "ALIEN", "VOID", "CRYPT", "SPACE"]
'''

# Load the exit door open image
door_open = pygame.image.load("door_open.png")
door_open = pygame.transform.scale(door_open, (WIDTH, HEIGHT))

# Room 3 - Word Lock Puzzle
def word_lock_puzzle():
    word = "ESCAPE"  # The word for the puzzle
    correct_code = sum(ord(char) for char in word)  # ASCII sum
    user_input = ""

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(room3_puzzle, (0, 0))  

        # Black box behind text
        pygame.draw.rect(screen, BLACK, (80, 30, 640, 180))
        pygame.draw.rect(screen, BLUE, (80, 30, 640, 180), 3)

        # Display instructions
        instruction_text = font.render("Find the ASCII values of each letter", True, BLUE)
        instruction_text2 = font.render("Add them together to get the code", True, BLUE)
        screen.blit(instruction_text, (100, 50))
        screen.blit(instruction_text2, (100, 80))

        # Display the word lock challenge
        text = font.render(f"Enter ASCII Sum for: {word}", True, BLUE)
        screen.blit(text, (100, 120))

        # Display user input
        input_text = font.render(user_input, True, WHITE)
        screen.blit(input_text, (100, 160))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check answer when Enter is pressed
                    if user_input.isdigit() and int(user_input) == correct_code:
                        # Show "Door Unlocked!" message
                        pygame.draw.rect(screen, BLACK, (100, 250, 600, 80))
                        pygame.draw.rect(screen, BLUE, (100, 250, 600, 80), 3)
                        msg_text = font.render("Door Unlocked! You are free!", True, BLUE)
                        screen.blit(msg_text, (120, 270))
                        pygame.display.flip()
                        pygame.time.delay(2000)

                        # Display the exit door open image
                        screen.fill(BLACK)
                        screen.blit(door_open, (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(3000)  

                        return 
                    
                    else:
                        # Show error message
                        pygame.draw.rect(screen, BLACK, (100, 250, 600, 80))
                        pygame.draw.rect(screen, BLUE, (100, 250, 600, 80), 3)
                        msg_text = font.render("Incorrect Code. Try Again.", True, BLUE)
                        screen.blit(msg_text, (120, 270))
                        pygame.display.flip()
                        pygame.time.delay(2000)  

                    user_input = ""  # Reset input after error

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  # Remove last character
                else:
                    user_input += event.unicode  # Add typed character

# Game Flow
intro_screen()
evolution_puzzle()
riddle_puzzle()
word_lock_puzzle()
pygame.quit()
