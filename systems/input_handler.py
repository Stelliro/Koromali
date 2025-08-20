# /systems/input_handler.py

import pygame
from utils.vectors import Vector2

class InputHandler:
    def __init__(self):
        self.key_states = pygame.key.get_pressed()
        self.mouse_states = list(pygame.mouse.get_pressed(5))
        self.mouse_wheel_scroll: int = 0
        self.quit_event_detected: bool = False
        
        self.prev_key_states = self.key_states
        self.prev_mouse_states = self.mouse_states[:]

        self._key_map = self._initialize_key_map()

    def _initialize_key_map(self):
        """Creates a mapping from simple strings to pygame key constants."""
        key_map = {
            **{chr(c): getattr(pygame, f"K_{chr(c)}") for c in range(ord('a'), ord('z') + 1)},
            **{str(i): getattr(pygame, f"K_{i}") for i in range(10)},
            "space": pygame.K_SPACE, "escape": pygame.K_ESCAPE, "enter": pygame.K_RETURN,
            "tab": pygame.K_TAB, "backspace": pygame.K_BACKSPACE,
            "left shift": pygame.K_LSHIFT, "right shift": pygame.K_RSHIFT,
            "left ctrl": pygame.K_LCTRL, "right ctrl": pygame.K_RCTRL,
            "left alt": pygame.K_LALT, "right alt": pygame.K_RALT,
            "up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT,
        }
        for i in range(1, 13): key_map[f"f{i}"] = getattr(pygame, f"K_F{i}")
        return key_map

    def process_events(self) -> list:
        self.prev_key_states = self.key_states
        self.prev_mouse_states = list(self.mouse_states)
        
        self.mouse_wheel_scroll = 0
        self.quit_event_detected = False

        self.key_states = pygame.key.get_pressed()
        self.mouse_states = pygame.mouse.get_pressed(5)
        
        # FIX: Capture and return all events for the UI system to process.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_event_detected = True
            elif event.type == pygame.MOUSEWHEEL:
                self.mouse_wheel_scroll = event.y
        return events

    def _get_pygame_key(self, key_name: str):
        return self._key_map.get(key_name.lower())

    def is_key_down(self, key_name: str) -> bool:
        pygame_key = self._get_pygame_key(key_name)
        return bool(pygame_key and self.key_states[pygame_key])

    def is_key_pressed(self, key_name: str) -> bool:
        pygame_key = self._get_pygame_key(key_name)
        return bool(pygame_key and self.key_states[pygame_key] and not self.prev_key_states[pygame_key])

    def is_mouse_button_down(self, button_index: int) -> bool:
        return bool(0 <= button_index < len(self.mouse_states) and self.mouse_states[button_index])

    def is_mouse_button_pressed(self, button_index: int) -> bool:
        return bool(0 <= button_index < len(self.mouse_states) and self.mouse_states[button_index] and not self.prev_mouse_states[button_index])

    def get_mouse_position(self) -> Vector2:
        pos = pygame.mouse.get_pos()
        return Vector2(pos[0], pos[1])

    def get_mouse_delta(self) -> tuple[int, int]:
        return pygame.mouse.get_rel()
        
    def get_mouse_wheel_scroll(self) -> int:
        return self.mouse_wheel_scroll
        
    def clear_pressed_state(self):
        self.prev_key_states = self.key_states
        self.prev_mouse_states = list(self.mouse_states)
            
    def consume_mouse_press(self, button_index: int):
        if 0 <= button_index < len(self.prev_mouse_states):
            self.prev_mouse_states[button_index] = True