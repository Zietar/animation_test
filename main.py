import pygame

class Animation:
    def __init__(self, sprite_sheet, frame_width, frame_height, frame_count, frame_duration, row=0):

        self.sprite_sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.row = row
        self.frames = self.load_frames()
        self.current_frame_index = 0
        self.time_since_last_frame = 0

    def load_frames(self):

        frames = []

        for i in range(self.frame_count):

            x = i * self.frame_width

            y = self.row * self.frame_height

            frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))

            # jednorazowa zmiana dla ludzika
            scaled_frame = pygame.transform.scale(frame, (self.frame_width * 6, self.frame_height * 6))
            frames.append(scaled_frame)
        
        return frames

    def update(self, delta_time):

        self.time_since_last_frame += delta_time

        if self.time_since_last_frame >= self.frame_duration:

            self.time_since_last_frame = 0

            self.current_frame_index = (self.current_frame_index + 1) % self.frame_count

    def draw(self, screen, position):
        screen.blit(self.frames[self.current_frame_index], position)

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

sprite_sheet_walk = pygame.image.load("ludzik_walk.png").convert_alpha()
sprite_sheet_attack = pygame.image.load("ludzik_attack.png").convert_alpha()

walk_animation = Animation(sprite_sheet_walk, 32, 32, 4, 125)

attack_animation = Animation(sprite_sheet_attack, 48, 48, 4, 125)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # logic

    delta_time = clock.get_time()

    walk_animation.update(delta_time)

    attack_animation.update(delta_time)

    # rendering

    screen.fill((120,120,120))

    walk_animation.draw(screen, (32, 32))

    attack_animation.draw(screen, (300, 300))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
