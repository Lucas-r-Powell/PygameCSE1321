import pygame
import Config
import button  # A file that contains how the buttons were made
import volume_slider  # Import the volume slider
import brightness_slider # Import the brightness slider
import Main

pygame.init()

# Short delay after menu state changes
def mouse_release():
    while pygame.mouse.get_pressed()[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.time.wait(10)

# Background music
pygame.mixer.init()
pygame.mixer.music.load('game-sounds/Final Frontier.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Button sound effects
click_sound = pygame.mixer.Sound('game-sounds/enter18.mp3')
click_sound.set_volume(0.4)
alt_click_sound = pygame.mixer.Sound('game-sounds/cancel9.mp3')
alt_click_sound.set_volume(0.4)

# Display Size
windowSize = (1920, 1080)
screen = pygame.display.set_mode(windowSize)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (76,187,23)

menu_state = "main"

# Calculate offset to center based on screen resolution
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
x_offset = (screen_width - 1920) // 2
y_offset = (screen_height - 1080) // 2

# Title image
mainTitle = pygame.image.load('game-images/zombie title.png').convert_alpha()

# Load Current Image Buttons
start_img = pygame.image.load('game-images/startBtn.png').convert_alpha()
about_img = pygame.image.load('game-images/aboutBtn.png').convert_alpha()
help_img = pygame.image.load('game-images/helpBtn.png').convert_alpha()
credits_img = pygame.image.load('game-images/creditsBtn.png').convert_alpha()
settings_img = pygame.image.load('game-images/settingsBtn.png').convert_alpha()
exit_img = pygame.image.load('game-images/exitBtn.png').convert_alpha()
back_img = pygame.image.load('game-images/backBtn.png').convert_alpha()

# Upload Hover Button Image Buttons
hover_start_img = pygame.image.load('game-images/startBtn2.png').convert_alpha()
hover_about_img = pygame.image.load('game-images/aboutBtn2.png').convert_alpha()
hover_help_img = pygame.image.load('game-images/helpBtn2.png').convert_alpha()
hover_credits_img = pygame.image.load('game-images/creditsBtn2.png').convert_alpha()
hover_settings_img = pygame.image.load('game-images/settingsBtn2.png').convert_alpha()
hover_exit_img = pygame.image.load('game-images/exitBtn2.png').convert_alpha()
hover_back_img = pygame.image.load('game-images/backBtn2.png').convert_alpha()

# Create Button Instances
startBtn = button.Button(875 + x_offset, 441 + y_offset, start_img, hover_start_img, 0.8, click_sound)
aboutBtn = button.Button(863 + x_offset, 546 + y_offset, about_img, hover_about_img, 0.8, click_sound)
helpBtn = button.Button(795 + x_offset, 652 + y_offset, help_img, hover_help_img, 0.8, click_sound)
creditBtn = button.Button(860 + x_offset, 758 + y_offset, credits_img, hover_credits_img, 0.8, click_sound)
settingsBtn = button.Button(860 + x_offset, 864 + y_offset, settings_img, hover_settings_img, 0.8, click_sound)
exitBtn = button.Button(900 + x_offset, 970 + y_offset, exit_img, hover_exit_img, 0.8, alt_click_sound)
backBtn = button.Button(900 + x_offset, 970 + y_offset, back_img, hover_back_img, 0.8, alt_click_sound)

# Volume Slider Instance
volumeSlider = volume_slider.VolumeSlider(800 + x_offset, 600 + y_offset, 300, 20, pygame.mixer.music.get_volume())

# Brightness Slider Instance (lowered for spacing)
brightnessSlider = brightness_slider.BrightnessSlider(800 + x_offset, 750 + y_offset, 300, 20, 1.0)

# Font and size of text
aboutInfo = pygame.font.SysFont(None, 40)
creditsInfo = pygame.font.SysFont(None, 50)
labelFont = pygame.font.SysFont(None, 40)

# Background image and Location of Main Title
bg_og = pygame.image.load("game-images/ruins2.png").convert()
bg1 = pygame.transform.scale(bg_og, (1920, 1080))
scaleTitle = pygame.transform.scale(mainTitle, (900, 200))

# Making the menu functional
running = True
while running:
    screen.blit(bg1, (x_offset, y_offset))  # Background aligned to offset

    # Check Menu State
    if menu_state == "main":
        screen.blit(scaleTitle, (500, 200))
        if startBtn.draw(screen):
            Main.start_game() 
        if aboutBtn.draw(screen):
            menu_state = "about"
        if helpBtn.draw(screen):
            menu_state = "help"
        if creditBtn.draw(screen):
            menu_state = "credits"
        if settingsBtn.draw(screen):
            menu_state = "settings"
        if exitBtn.draw(screen):
            mouse_release()
            running = False
            pygame.time.delay(800)

    if menu_state == "about":
        if backBtn.draw(screen):
            menu_state = "main"
            mouse_release()
        lines = [
            "Collect the items on the map to use against the zombies to kill them.",
            "Every round, the number of zombies will increase by 5.",
            "Use the healing potions/medicine will regenerate",
            "your health so you can keep playing without being on the verge of death.",
            "Make it to round 5, and you win the game.",
            "Good luck!"
        ]

        line_spacing = 10
        rendered_lines = [aboutInfo.render(line, True, black) for line in lines]
        total_height = sum(text.get_height() + line_spacing for text in rendered_lines) - line_spacing
        start_y = (screen_height - total_height) // 2 + 40

        for text_surface in rendered_lines:
            text_rect = text_surface.get_rect(center=(screen_width // 2, start_y))
            screen.blit(text_surface, text_rect)
            start_y += text_surface.get_height() + line_spacing

        # About Title
        aboutTitle = pygame.font.Font(None, 60)
        aboutRender = aboutTitle.render("About", False, black)
        screen.blit(aboutRender, (890, 285))

    if menu_state == "help":
        if backBtn.draw(screen):
            menu_state = "main"
            mouse_release()

        # Help Title
        helpTitle = pygame.font.Font(None, 60)
        helpRender = helpTitle.render("How to Play", False, black)
        screen.blit(helpRender, (844, 285))

        lines = [
            "",
            "Keyboard:",
            "- W: move forward",
            "- A: move left",
            "- S: move backwards",
            "- D: move right",
            "",
            "Mouse:",
            "- (Left-Click): move the cursor around and",
            "       click on each zombie to kill them",
            "",
            "Collect medkits to gain back health."
        ]

        line_spacing = 15
        rendered_lines = [aboutInfo.render(line, True, black) for line in lines]
        total_height = sum(text.get_height() + line_spacing for text in rendered_lines) - line_spacing
        start_y = (screen_height - total_height) // 2 + 50

        for text_surface in rendered_lines:
            text_rect = text_surface.get_rect(center=(screen_width // 2, start_y))
            screen.blit(text_surface, text_rect)
            start_y += text_surface.get_height() + line_spacing

    if menu_state == "credits":
        if backBtn.draw(screen):
            menu_state = "main"
            mouse_release()
        lines = [
            "Megan Sierra",
            "Lucas Powell",
            "Kev Stolz",
            "Olani Francis",
            "Sirawdink Wakalto",
            "",
            "Background Image: unsplash.com",
            "Music: soundtaxi.com",
            "Sound effects from: https://pocket-se.info/ (Pocket Sound)"
        ]

        line_spacing = 15
        rendered_lines = [creditsInfo.render(line, False, black) for line in lines]
        total_height = sum(text.get_height() + line_spacing for text in rendered_lines) - line_spacing
        start_y = (screen_height - total_height) // 2 - 30

        for text_surface in rendered_lines:
            text_rect = text_surface.get_rect(center=(screen_width // 2, start_y))
            screen.blit(text_surface, text_rect)
            start_y += text_surface.get_height() + line_spacing

        # Credits Title
        creditsTitle = pygame.font.Font(None, 55)
        creditsRender = creditsTitle.render("Credits", False, black)
        screen.blit(creditsRender, (890, 200))

    if menu_state == "settings":
        if backBtn.draw(screen):
            menu_state = "main"
            mouse_release()

        settingsTitle = pygame.font.Font(None, 55)
        settingsRender = settingsTitle.render("Settings", False, black)
        screen.blit(settingsRender, (890, 200))

        # Draw volume slider
        volumeSlider.draw(screen)

        # Volume label
        volume_label = labelFont.render("Volume", True, black)
        screen.blit(volume_label, (volumeSlider.rect.x, volumeSlider.rect.y - 35))

        # Draw brightness slider
        brightnessSlider.draw(screen)

        # Brightness label
        brightness_label = labelFont.render("Brightness", True, black)
        screen.blit(brightness_label, (brightnessSlider.rect.x, brightnessSlider.rect.y - 35))

        settingsTitle = pygame.font.Font(None, 55)
        settingsRender = settingsTitle.render("Settings", False, black)
        screen.blit(settingsRender, (890, 200))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if menu_state == "settings":
            volumeSlider.handle_event(event)
            brightnessSlider.handle_event(event)

    brightness = brightnessSlider.get_brightness()
    if brightness < 1.0:
        overlay = pygame.Surface((1920, 1080))
        overlay.set_alpha(int((1.0 - brightness) * 255))  # 0 = full bright, 255 = dark
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (x_offset, y_offset))

    pygame.display.update()

pygame.quit()
