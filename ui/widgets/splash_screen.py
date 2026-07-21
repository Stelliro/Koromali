# /ui/widgets/splash_screen.py
import math
import random
import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt6.QtGui import (
    QPainter, QColor, QFont, QPen, QRadialGradient, 
    QConicalGradient, QBrush, QPixmap, QPainterPath, QImage
)
from PyQt6.QtCore import (
    Qt, QTimer, QPointF, QPropertyAnimation, QEasingCurve, 
    QRect, QRectF, QSize
)
from utils.logger import log

class SplashScreen(QWidget):
    """
    A 'Core Anomaly' Splash Screen.
    
    Features:
    - Gravitational Lensing: Captures the desktop background and distorts it 
      in the center to simulate a black hole's refractive index.
    - Glitch Effects: RGB-split text and chaotic jitter.
    - Particle Horizon: An animated accretion disk.
    """
    
    # Configuration
    SIZE = 640
    HOLE_RADIUS = 80
    LENS_STRENGTH = 1.5  # Magnification of the background
    PARTICLE_COUNT = 150
    GLITCH_CHANCE = 0.15 # 15% chance to glitch per frame

    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.SplashScreen |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setFixedSize(self.SIZE, self.SIZE)

        # Center the window immediately so we know where to grab the screen
        screen_geo = QApplication.primaryScreen().geometry()
        x = (screen_geo.width() - self.SIZE) // 2
        y = (screen_geo.height() - self.SIZE) // 2
        self.move(x, y)

        # Colors - Cyberpunk / Anomaly Palette
        self.c_cyan = QColor("#00f3ff")
        self.c_magenta = QColor("#ff0055")
        self.c_void = QColor(10, 10, 15, 240) # Dark halo

        # Initialize State
        self.particles = []
        self._init_particles()
        self.rotation_angle = 0
        self.glitch_active = False
        self.bg_lens_pixmap = None

        # Try to capture the background for the warp effect
        self._capture_background_warp(x, y)

        # UI Elements
        self._setup_ui()

        # Animation Loop
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.timer.start(16) # ~60 FPS

    def _setup_ui(self):
        # Status Label (Glitched Font style)
        self.status_label = QLabel("INITIALIZING CORE...", self)
        self.status_label.setGeometry(0, self.height() - 80, self.width(), 30)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Consolas", 10)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 3)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: #a4ddff; background: transparent;")

        # Invisible cancel button (Clicking text works too)
        self.cancel_btn = QPushButton("ABORT", self)
        self.cancel_btn.setGeometry((self.width()-100)//2, self.height()-40, 100, 30)
        self.cancel_btn.setStyleSheet("color: #555; background: transparent; border: none;")
        self.cancel_btn.clicked.connect(QApplication.instance().quit)

    def _capture_background_warp(self, x, y):
        """
        Grabs the screen content behind the window to create a refraction effect.
        """
        try:
            screen = QApplication.primaryScreen()
            # Grab the area exactly behind where the 'black hole' will be
            # We grab a slightly smaller area and scale it UP to create magnification
            
            # Center of the widget
            cx, cy = self.SIZE // 2, self.SIZE // 2
            
            # The capture region size (smaller than the hole to simulate zoom)
            capture_r = int(self.HOLE_RADIUS / self.LENS_STRENGTH)
            
            # Global coordinates to grab
            gx = x + cx - capture_r
            gy = y + cy - capture_r
            gw = capture_r * 2
            gh = capture_r * 2
            
            original_pix = screen.grabWindow(0, gx, gy, gw, gh)
            
            if original_pix and not original_pix.isNull():
                # Scale it up to the hole size (Magnification effect)
                scaled_pix = original_pix.scaled(
                    self.HOLE_RADIUS * 2, 
                    self.HOLE_RADIUS * 2,
                    Qt.AspectRatioMode.IgnoreAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                
                # Create a circular mask
                final_img = QImage(scaled_pix.size(), QImage.Format.Format_ARGB32)
                final_img.fill(Qt.GlobalColor.transparent)
                
                painter = QPainter(final_img)
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                
                # Draw the circle path
                path = QPainterPath()
                path.addEllipse(0, 0, final_img.width(), final_img.height())
                painter.setClipPath(path)
                painter.drawPixmap(0, 0, scaled_pix)
                painter.end()
                
                self.bg_lens_pixmap = QPixmap.fromImage(final_img)
            else:
                log.warning("Could not grab screen for warp effect (OS restriction?).")
        except Exception as e:
            log.error(f"Warp effect initialization failed: {e}")

    def _init_particles(self):
        for _ in range(self.PARTICLE_COUNT):
            self.particles.append({
                'angle': random.uniform(0, 6.28),
                'dist': random.uniform(self.HOLE_RADIUS + 10, self.SIZE/2.5),
                'speed': random.uniform(0.02, 0.05),
                'size': random.uniform(1, 3)
            })

    def _update(self):
        self.rotation_angle += 2
        if self.rotation_angle >= 360:
            self.rotation_angle = 0
            
        # Determine glitch state
        self.glitch_active = (random.random() < self.GLITCH_CHANCE)
        
        # Update particles (Orbit mechanics)
        for p in self.particles:
            p['angle'] += p['speed']
            # Slowly spiral in
            p['dist'] -= 0.1
            if p['dist'] < self.HOLE_RADIUS:
                p['dist'] = random.uniform(self.SIZE/3, self.SIZE/2.2)
                
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        center = QPointF(self.width() / 2, self.height() / 2)
        
        # 1. Draw the "Warped" Background (The Lens)
        if self.bg_lens_pixmap:
            # Draw the lens image in the center
            lens_pos = QPointF(center.x() - self.HOLE_RADIUS, center.y() - self.HOLE_RADIUS)
            
            # Apply a slight jitter if glitching
            if self.glitch_active:
                off_x = random.randint(-2, 2)
                off_y = random.randint(-2, 2)
                lens_pos += QPointF(off_x, off_y)
                
            painter.drawPixmap(lens_pos, self.bg_lens_pixmap)

            # Draw a dark overlay on the lens to make it look "deep"
            painter.setBrush(QColor(0, 0, 0, 100))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(center, self.HOLE_RADIUS, self.HOLE_RADIUS)

        else:
            # Fallback black hole if capture failed
            painter.setBrush(QColor(0, 0, 0, 255))
            painter.drawEllipse(center, self.HOLE_RADIUS, self.HOLE_RADIUS)

        # 2. Draw Accretion Disk (Swirling gradients)
        painter.save()
        painter.translate(center)
        painter.rotate(self.rotation_angle)
        
        # Conical gradient for the swirling gas look
        conical = QConicalGradient(0, 0, 0)
        conical.setColorAt(0.0, Qt.GlobalColor.transparent)
        conical.setColorAt(0.2, self.c_cyan)
        conical.setColorAt(0.5, Qt.GlobalColor.transparent)
        conical.setColorAt(0.7, self.c_magenta)
        conical.setColorAt(1.0, Qt.GlobalColor.transparent)
        
        painter.setBrush(QBrush(conical))
        painter.setPen(Qt.PenStyle.NoPen)
        # Draw ring
        painter.drawEllipse(QPointF(0,0), self.HOLE_RADIUS + 40, self.HOLE_RADIUS + 40)
        painter.restore()

        # 3. Draw Particles
        painter.setPen(Qt.PenStyle.NoPen)
        for p in self.particles:
            x = center.x() + math.cos(p['angle']) * p['dist']
            y = center.y() + math.sin(p['angle']) * p['dist']
            
            # Color based on distance (hotter closer to core)
            alpha = int(255 * (1 - (p['dist'] / (self.SIZE/2))))
            alpha = max(0, min(255, alpha))
            
            col = self.c_cyan if p['angle'] % 2 > 1 else self.c_magenta
            col.setAlpha(alpha)
            painter.setBrush(col)
            painter.drawEllipse(QPointF(x, y), p['size'], p['size'])

        # 4. Draw Glitchy Text
        # We draw the text multiple times with offsets to create RGB split
        
        text = "KOROMALI"
        font = QFont("Impact", 48, QFont.Weight.Bold)
        if self.glitch_active:
            # Random font size change
            font.setPointSizeF(48 + random.uniform(-2, 2))
        
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 10)
        painter.setFont(font)
        
        text_rect = QRect(0, 0, self.width(), self.height())
        
        # Draw Cyan Channel (Offset Left)
        if self.glitch_active:
            painter.setPen(self.c_cyan)
            offset = random.randint(-4, -1)
            painter.drawText(text_rect.translated(offset, 0), Qt.AlignmentFlag.AlignCenter, text)
            
            # Draw Magenta Channel (Offset Right)
            painter.setPen(self.c_magenta)
            offset = random.randint(1, 4)
            painter.drawText(text_rect.translated(offset, 0), Qt.AlignmentFlag.AlignCenter, text)
        
        # Draw Main White Text
        painter.setPen(QColor(255, 255, 255, 240))
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, text)

        # 5. Random "Scanlines" or "Artifacts"
        if self.glitch_active:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            h = random.randint(2, 5)
            y = random.randint(0, self.height())
            painter.drawRect(0, y, self.width(), h)

    def set_status(self, message: str):
        self.status_label.setText(message.upper())
        QApplication.processEvents()

    def finish(self):
        log.info("Ending anomaly sequence.")
        self.timer.stop()
        self.fade = QPropertyAnimation(self, b"windowOpacity")
        self.fade.setDuration(500)
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)
        self.fade.finished.connect(self.close)
        self.fade.start()