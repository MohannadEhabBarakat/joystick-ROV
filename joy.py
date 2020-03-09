import pygame
pygame.init()

def send(name, value):
    print(name, ":" ,value)

def main():

    running = True

    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                #send("Analog", event.value)
                print(event)
                j=pygame.joystick.Joystick(0)
                print (j.get_axis(0))
                print (j.get_axis(1))
            elif event.type == pygame.JOYHATMOTION:
                send("Hat",event.value)
            elif event.type == pygame.JOYBUTTONDOWN:
                send("Button",event.button)

#01025545898

    pygame.quit()

main()
