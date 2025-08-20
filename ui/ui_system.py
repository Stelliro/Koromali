# /ui/ui_system.py

import pygame
import json
import os
import re
from utils.logger import logger
from utils.color import Color
from utils.vectors import Vector2
import game.components as C

class UISystem:
    """
    A robust UI system that uses Pygame for all 2D drawing. It loads layouts
    and themes from JSON files, handles events, and renders the entire UI
    to a single surface that is then drawn by the UIRenderer.
    """

    def __init__(self, engine):
        self.engine = engine
        self.screen_surface = None
        self.theme = None
        self.fonts = {}
        self.screens = {}
        self.active_screen_id = None
        self.actions = {}

    def initialize(self):
        """Initializes the UI system, surface, and loads all assets."""
        logger.info("Initializing New UI System...")
        w, h = self.engine.platform.get_window_size()
        self.screen_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        self.load_theme('assets/ui/themes/default.json')
        self.load_layouts('assets/ui/layouts')
        logger.info("New UI System Initialized.")

    def load_theme(self, path):
        """Loads a JSON theme file that defines the UI's appearance."""
        try:
            with open(path, 'r') as f:
                self.theme = json.load(f)
            logger.info(f"Loaded UI theme: {self.theme['name']}")
            font_path = self.theme.get("fonts", {}).get("default") or "assets/ui/fonts/Prototype.ttf"
            if os.path.exists(font_path):
                for size in [18, 22, 24, 32, 48, 72]:
                    self.fonts[size] = pygame.font.Font(font_path, size)
            else:
                 logger.warning(f"Default UI font not found at {font_path}. Using Pygame default.")
                 for size in [18, 22, 24, 32, 48, 72]:
                    self.fonts[size] = pygame.font.Font(None, size)
        except Exception as e:
            logger.error(f"Failed to load UI theme: {e}")

    def load_layouts(self, path):
        """Loads all UI layout JSON files from a directory."""
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                try:
                    with open(os.path.join(path, filename), 'r') as f:
                        layout_data = json.load(f)
                        screen_id = layout_data['id']
                        self.screens[screen_id] = self._parse_layout(layout_data)
                        logger.info(f"Loaded UI layout: {screen_id}")
                except Exception as e:
                    logger.error(f"Failed to parse UI layout {filename}: {e}")

    def _parse_layout(self, layout_data):
        """Recursively parses layout data and creates widget instances."""
        elements = []
        for element_data in layout_data.get('elements', []):
            element_type = element_data['type']
            element_class = WIDGET_MAP.get(element_type)
            if element_class:
                element = element_class(self, element_data)
                if hasattr(element, 'children') and 'elements' in element_data:
                    element.children = self._parse_layout(element_data)
                elements.append(element)
        return elements
        
    def register_action(self, action_name, function):
        """Allows states to register callable functions for UI events."""
        self.actions[action_name] = function

    def set_active_screen(self, screen_id):
        self.active_screen_id = screen_id
        logger.debug(f"UI Active screen set to: {screen_id}")

    def handle_events(self, events):
        """Passes Pygame events to the active UI screen."""
        if self.active_screen_id and self.active_screen_id in self.screens and events is not None:
            for element in self.screens[self.active_screen_id]:
                element.handle_event(events)

    def begin_frame(self):
        """Clears the UI surface for the new frame."""
        self.screen_surface.fill((0, 0, 0, 0))

    def get_surface(self) -> pygame.Surface:
        """Returns the final UI surface for the renderer to composite."""
        return self.screen_surface

    def render_screen(self, screen_id, **context):
        """Renders all elements of a specific screen."""
        if screen_id in self.screens:
            for element in self.screens[screen_id]:
                element.render(self.screen_surface, self.theme, self.fonts, self.actions, context)

# --- BASE WIDGET CLASS ---
class UIElement:
    def __init__(self, ui_system, data):
        self.ui = ui_system
        self.id = data.get('id')
        self.style = self.ui.theme['styles'].get(data.get('style', 'default'), {})
        self.rect = self._calculate_rect(data['rect'])
        self.context_key = data.get('context_key')

    def _calculate_rect(self, rect_data):
        w_surf, h_surf = self.ui.screen_surface.get_size()
        x, y, w, h = rect_data

        # Robust parsing for width and height (pixels or percentage)
        if isinstance(w, str): w = float(w[:-1]) * w_surf / 100 if '%' in w else int(re.sub(r'[^-\d]', '', w))
        if isinstance(h, str): h = float(h[:-1]) * h_surf / 100 if '%' in h else int(re.sub(r'[^-\d]', '', h))

        # Robust parsing for position (center, absolute, or relative to edge)
        if isinstance(x, str):
            if x == 'center': x = (w_surf - w) / 2
            elif '-' in x: parts = x.split('-'); x = w_surf - w - int(parts[1])
            else: x = int(x)
        if isinstance(y, str):
            if y == 'center': y = (h_surf - h) / 2
            elif '-' in y: parts = y.split('-'); y = h_surf - h - int(parts[1])
            else: y = int(y)
        
        return pygame.Rect(x, y, w, h)
        
    def render(self, surface, theme, fonts, actions, context): pass
    def handle_event(self, events): pass

# --- WIDGET IMPLEMENTATIONS ---
class Panel(UIElement):
    def __init__(self, ui_system, data):
        super().__init__(ui_system, data)
        self.color = Color(*data.get('color', self.ui.theme['colors']['primary']))
        self.children = []

    def render(self, surface, theme, fonts, actions, context):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=4)
        for child in self.children:
            child.render(surface, theme, fonts, actions, context)
            
    def handle_event(self, events):
        for child in self.children:
            child.handle_event(events)

class Label(UIElement):
    def __init__(self, ui_system, data):
        super().__init__(ui_system, data)
        self.text = data['text']
        self.font_size = self.style.get('font_size', 24)
        self.color = Color(*self.ui.theme['colors'][self.style.get('color', 'text')])
        self.text_align = data.get('text_align', 'center')

    def render(self, surface, theme, fonts, actions, context):
        text_to_render = context.get(self.context_key, self.text)
        font = fonts.get(self.font_size, fonts[24])
        text_surf = font.render(text_to_render, True, self.color)
        
        pos = text_surf.get_rect(center=self.rect.center)
        if self.text_align == 'left': pos.midleft = self.rect.midleft
        elif self.text_align == 'right': pos.midright = self.rect.midright
        surface.blit(text_surf, pos)

class Button(Label):
    def __init__(self, ui_system, data):
        super().__init__(ui_system, data)
        self.action_name = data.get('action')
        self.action_args = data.get('action_args', [])
        self.is_hovered = False

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_hovered and self.action_name in self.ui.actions:
                    self.ui.actions[self.action_name](*self.action_args)

    def render(self, surface, theme, fonts, actions, context):
        border_color = theme['colors']['highlight'] if self.is_hovered else theme['colors']['accent']
        bg_color = theme['colors']['secondary'] if self.is_hovered else theme['colors']['primary']
        
        pygame.draw.rect(surface, bg_color, self.rect, border_radius=4)
        pygame.draw.rect(surface, border_color, self.rect, width=self.style.get('border_width', 2), border_radius=4)
        
        super().render(surface, theme, fonts, actions, context)

class DynamicListPanel(Panel):
    def __init__(self, ui_system, data):
        super().__init__(ui_system, data)
        self.data_source_key = data['data_source']
        self.element_template = data['element_template']
        
    def render(self, surface, theme, fonts, actions, context):
        list_data = context.get(self.data_source_key, [])
        y_offset = 0
        for item_data in list_data:
            template = self.element_template.copy()
            template['text'] = item_data['text']
            template['action'] = item_data['action_name']
            template['action_args'] = item_data['action_args']
            
            h = int(template['height'].replace('px', ''))
            m = template.get('margin_y', 0)
            
            template['rect'] = [self.rect.x, self.rect.y + y_offset, self.rect.width, h]
            
            element_class = WIDGET_MAP.get(template['type'])
            if element_class:
                element = element_class(self.ui, template)
                element.render(surface, theme, fonts, actions, context)

            y_offset += h + m
            
    def handle_event(self, events):
         # This part needs to be dynamic too if list items are interactive
         pass
         
# Map string types from JSON to widget classes
WIDGET_MAP = {
    "Panel": Panel,
    "Label": Label,
    "Button": Button,
    "DynamicListPanel": DynamicListPanel
}