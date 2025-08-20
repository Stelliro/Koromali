# /ui/widgets/splash_screen.py
import math
import random
import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QRadialGradient, QMovie, QPixmap
from PyQt6.QtCore import Qt, QTimer, QPointF, QPropertyAnimation, QEasingCurve, QRect, QSize
from utils.logger import log
from utils.helpers import get_base_path


class SplashScreen(QWidget):
    """
    An animated, frameless splash screen visualizing a "Core Anomaly" as a
    violent, warping black hole directly on the desktop.
    """
    PARTICLE_COUNT = 3000
    GRAVITY_STRENGTH = 2000.0
    RESET_RADIUS = 15.0
    JITTER_INTENSITY = 4.0

    def __init__(self):
        super().__init__()
        self.fade_animation = None
        self.setWindowFlags(
            Qt.WindowType.SplashScreen |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.setFixedSize(600, 600) # Increased size for better quality
        self.particles = []
        self.ripples = []

        self.color_text_glow = QColor("#ff073a")
        self.color_status_text = QColor("#8a93a0")
        self.color_black_hole = QColor(0, 0, 0, 255)
        self.color_accretion_disk = QColor("#ff073a")
        self.color_warp_ring = QColor("#a4ddff")

        self._setup_ui_elements()
        self._initialize_particles()

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self._update_animation)
        self.animation_timer.start(16) # ~60 FPS

    def _setup_ui_elements(self):
        self.status_label = QLabel("INITIALIZING ANOMALY...", self)
        self.status_label.setGeometry(0, self.height() - 70, self.width(), 20)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Share Tech Mono", 12))
        self.status_label.setStyleSheet(f"color: {self.color_status_text.name()}; background-color: transparent; letter-spacing: 2px;")

        self.cancel_button = QPushButton("CANCEL", self)
        self.cancel_button.setGeometry((self.width() - 100) // 2, self.height() - 45, 100, 25)
        self.cancel_button.setFont(QFont("Share Tech Mono", 10))
        self.cancel_button.setStyleSheet(f"""
            QPushButton {{
                color: {self.color_status_text.name()};
                background-color: transparent;
                border: 1px solid {self.color_status_text.name()};
                border-radius: 4px;
                letter-spacing: 1px;
            }}
            QPushButton:hover {{
                background-color: #ff073a;
                color: #ffffff;
                border-color: #ff073a;
            }}
        """)
        self.cancel_button.clicked.connect(QApplication.instance().quit)

    def _initialize_particles(self):
        center = QPointF(self.width() / 2, self.height() / 2)
        max_dist = self.width() / 2
        for _ in range(self.PARTICLE_COUNT):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(self.RESET_RADIUS, max_dist)
            self.particles.append({
                'pos': QPointF(center.x() + math.cos(angle) * radius, center.y() + math.sin(angle) * radius),
                'vel': QPointF(0, 0)
            })

    def _update_animation(self):
        center = QPointF(self.width() / 2, self.height() / 2)
        for p in self.particles:
            force_vector = center - p['pos']
            distance_sq = QPointF.dotProduct(force_vector, force_vector)

            if distance_sq < self.RESET_RADIUS ** 2:
                angle = random.uniform(0, 2 * math.pi)
                edge_x = center.x() + math.cos(angle) * (self.width() / 2)
                edge_y = center.y() + math.sin(angle) * (self.height() / 2)
                p['pos'] = QPointF(edge_x, edge_y)
                p['vel'] = QPointF(0, 0)
                continue

            gravity = self.GRAVITY_STRENGTH / (distance_sq + 1)
            force_vector /= math.sqrt(distance_sq) if distance_sq > 0 else 1
            p['vel'] += force_vector * gravity
            p['pos'] += p['vel']

        if random.randint(0, 8) == 0:
            self.ripples.append({'radius': 25, 'opacity': 50})

        new_ripples = []
        for r in self.ripples:
            r['radius'] += 1.5
            r['opacity'] -= 0.5
            if r['opacity'] > 0:
                new_ripples.append(r)
        self.ripples = new_ripples
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        center_point = QPointF(self.width() / 2, self.height() / 2)

        # Draw a soft outer glow for the whole effect
        outer_glow_gradient = QRadialGradient(center_point, self.width() / 2)
        outer_glow_gradient.setColorAt(0.3, QColor(255, 7, 58, 20))
        outer_glow_gradient.setColorAt(1, Qt.GlobalColor.transparent)
        painter.fillRect(self.rect(), outer_glow_gradient)

        painter.setBrush(Qt.BrushStyle.NoBrush)
        for r in self.ripples:
            pen = QPen(self.color_warp_ring)
            pen.setWidthF(max(0.5, 3 - r['radius'] / 100.0))
            color = QColor(self.color_warp_ring)
            color.setAlpha(int(r['opacity']))
            pen.setColor(color)
            painter.setPen(pen)
            painter.drawEllipse(center_point, r['radius'], r['radius'])

        disk_gradient = QRadialGradient(center_point, 60)
        disk_gradient.setColorAt(0.2, self.color_accretion_disk)
        disk_gradient.setColorAt(1, Qt.GlobalColor.transparent)
        painter.setBrush(disk_gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(center_point, 60, 60)

        painter.setBrush(self.color_black_hole)
        painter.drawEllipse(center_point, 25, 25)

        painter.setPen(Qt.PenStyle.NoPen)
        for p in self.particles:
            painter.setBrush(QColor(255, 255, 255, 120))
            painter.drawEllipse(p['pos'], 1, 1)

        font = QFont("Share Tech Mono", 64, QFont.Weight.Bold) # Increased font size
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 10)
        painter.setFont(font)
        text_rect = self.rect()

        glow_offset_x = random.uniform(-self.JITTER_INTENSITY, self.JITTER_INTENSITY)
        glow_offset_y = random.uniform(-self.JITTER_INTENSITY, self.JITTER_INTENSITY)
        painter.setPen(self.color_text_glow)
        painter.drawText(text_rect.translated(int(glow_offset_x), int(glow_offset_y)), Qt.AlignmentFlag.AlignCenter,
                         "KOROMALI")

        main_offset_x = random.uniform(-self.JITTER_INTENSITY / 2, self.JITTER_INTENSITY / 2)
        main_offset_y = random.uniform(-self.JITTER_INTENSITY / 2, self.JITTER_INTENSITY / 2)
        painter.setPen(QColor("#00e5ff"))
        painter.drawText(text_rect.translated(int(main_offset_x), int(main_offset_y)), Qt.AlignmentFlag.AlignCenter,
                         "KOROMALI")

    def set_status(self, message: str):
        self.status_label.setText(message.upper())
        QApplication.processEvents()

    def finish(self):
        log.info("Splash screen finish sequence initiated.")
        self.animation_timer.stop()

        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(800) # Increased duration for a smoother fade
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)
        self.fade_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.fade_animation.finished.connect(self._on_fade_finished)

        # A timer to ensure the splash is visible for a minimum duration
        # before the fade-out starts.
        QTimer.singleShot(2500, self.fade_animation.start)
        log.info("Splash screen fade-out animation scheduled.")

    def _on_fade_finished(self):
        """This slot is called when the fade-out animation is complete."""
        log.info("Splash fade-out finished. Deleting widget now.")
        self.deleteLater()