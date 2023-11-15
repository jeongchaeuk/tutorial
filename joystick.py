"""joystick.py example."""

import pygame

pygame.init()

def indent(text, level=0, space=4):
    return (" " * space * level) + text


def main():
    size = (500, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Joystick example")

    clock = pygame.Clock()

    font = pygame.font.SysFont('d2coding', 18)
    wraplength = size[0] - 20

    # This dict can be left as-is, since pygame-ce will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    done = False
    while not done:
        # Possible joystick events:
        # JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION
        # JOYBUTTONDOWN, JOYBUTTONUP,
        # JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Joystick `{event.button}` button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.5, 200):
                        print(f'Rumble effect played on joystick '
                              f'{event.instance_id}')

            if event.type == pygame.JOYBUTTONUP:
                print(f"Joystick `{event.button}` button released.")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts
                # for every joystick, filling up the list without
                # needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connected.")

            if event.type == pygame.JOYDEVICEREMOVED:
                if event.instance_id in joysticks:
                    del joysticks[event.instance_id]
                    print(f"Joystick {event.instance_id} disconnected.")
                else:
                    print(f'Tried to disconnect Joystick '
                          f'{event.instance_id}, but couldn\'t find it '
                          f'in the joystick list.')

        screen.fill((255, 255, 255))

        level = 0
        lines = []

        # Get count of joysticks.
        line = f'Number of joysticks: {pygame.joystick.get_count()}'
        lines.append(indent(line, level))
        level += 1

        # For each joystick:
        for joystick in joysticks.values():
            line = f"Joystick {joystick.get_instance_id()}"
            lines.append(indent(line, level))
            level += 1

            # Get the name from the OS for the controller/joystick.
            line = f'Joystick name: {joystick.get_name()}'
            lines.append(indent(line, level))

            line = f'GUID: {joystick.get_guid()}'
            lines.append(indent(line, level))

            line = f'Joystick\'s power level: {joystick.get_power_level()}'
            lines.append(indent(line, level))

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other. Triggers count as axes.
            num_axes = joystick.get_numaxes()
            line = f'Number of axes: {num_axes}'
            lines.append(indent(line, level))
            level += 1

            for i in range(num_axes):
                pos = joystick.get_axis(i)
                line = f'Axis {i} value: {pos:>6.4f}'
                lines.append(indent(line, level))
            level -= 1

            num_buttons = joystick.get_numbuttons()
            line = f'Number of buttons: {num_buttons}'
            lines.append(indent(line, level))
            level += 1

            for i in range(num_buttons):
                state = joystick.get_button(i)
                line = f'Button {i:>2} value: {state}'
                lines.append(indent(line, level))
            level -= 1

            num_hats = joystick.get_numhats()
            line = f'Number of hats: {num_hats}'
            lines.append(indent(line, level))
            level += 1

            # Hat position. All or nothing for direction, not a float like
            # get_axis(). Position is a tuple of int values (x, y).
            for i in range(num_hats):
                pos = joystick.get_hat(i)
                line = f'Hat {i} value: {str(pos)}'
                lines.append(indent(line, level))
            level -= 2

        # draw the accumulated text
        screen.blit(
            font.render("\n".join(lines), True, "black", "white", wraplength),
            (10, 10))

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        clock.tick(30)


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
