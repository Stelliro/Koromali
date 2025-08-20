# /plugins/web_browser/browser_widget.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QFrame, QLabel
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon
import qtawesome as qta
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log

try:
    from PyQt6.QtWebEngineWidgets import QWebEngineView
    from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineSettings
    WEB_ENGINE_AVAILABLE = True
except ImportError:
    WEB_ENGINE_AVAILABLE = False


class BrowserWidget(QWidget):
    def __init__(self, api: KoromaliPluginAPI):
        super().__init__()
        self.api = api
        self.theme_manager = api.get_manager("theme")
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        if not WEB_ENGINE_AVAILABLE:
            self._setup_error_ui()
            return

        self._setup_browser_ui()
        self._connect_signals()
        self.update_theme()

    def _setup_error_ui(self):
        """Sets up a placeholder UI when PyQtWebEngine is not installed."""
        error_label = QLabel(
            "<b>PyQtWebEngine is not installed.</b><br>"
            "Please install it to use the browser feature:<br>"
            "<code>pip install PyQt6-WebEngine</code>"
        )
        error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        error_label.setOpenExternalLinks(True)
        self.main_layout.addWidget(error_label)

    def _setup_browser_ui(self):
        """Sets up the full browser UI when dependencies are met."""
        # Toolbar
        toolbar = QFrame()
        toolbar.setObjectName("BrowserToolbar")
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(5, 5, 5, 5)

        self.back_button = QPushButton()
        self.forward_button = QPushButton()
        self.reload_button = QPushButton()
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL and press Enter")

        toolbar_layout.addWidget(self.back_button)
        toolbar_layout.addWidget(self.forward_button)
        toolbar_layout.addWidget(self.reload_button)
        toolbar_layout.addWidget(self.address_bar, 1)

        # Web View
        self.view = QWebEngineView()
        
        # Create an off-the-record profile for private browsing. This ensures
        # no history, cookies, or cache are written to disk.
        self.profile = QWebEngineProfile(f"private_profile_{id(self)}", self) # Unique profile
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies)
        self.profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.NoCache)
        
        page = QWebEnginePage(self.profile, self)
        self.view.setPage(page)
        
        # Apply strict privacy and security settings. This browser is based on
        # Chromium (via QtWebEngine) and cannot use Firefox extensions. However,
        # we can configure it to be as private as possible.
        settings = self.view.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.DnsPrefetchingEnabled, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebRTCPublicInterfacesOnly, True)

        self.view.setUrl(QUrl("https://duckduckgo.com"))

        # Privacy Status Bar
        privacy_bar = QFrame()
        privacy_bar.setObjectName("BrowserPrivacyBar")
        privacy_layout = QHBoxLayout(privacy_bar)
        privacy_layout.setContentsMargins(5, 2, 5, 2)
        privacy_icon = QLabel()
        privacy_icon.setPixmap(qta.icon('mdi.shield-lock-outline', color='grey').pixmap(14, 14))
        privacy_label = QLabel("Private Browsing Session (History and data are not saved)")
        privacy_label.setObjectName("BrowserPrivacyLabel")
        privacy_layout.addWidget(privacy_icon)
        privacy_layout.addWidget(privacy_label)
        privacy_layout.addStretch()

        self.main_layout.addWidget(toolbar)
        self.main_layout.addWidget(self.view, 1)
        self.main_layout.addWidget(privacy_bar)

    def _connect_signals(self):
        if not WEB_ENGINE_AVAILABLE:
            return
            
        self.back_button.clicked.connect(self.view.back)
        self.forward_button.clicked.connect(self.view.forward)
        self.reload_button.clicked.connect(self.view.reload)
        self.address_bar.returnPressed.connect(self._navigate_to_url)
        
        self.view.urlChanged.connect(self._update_address_bar)
        self.view.loadStarted.connect(self._on_load_started)
        self.view.loadFinished.connect(self._on_load_finished)

    def _navigate_to_url(self):
        url_text = self.address_bar.text()
        if not url_text.startswith(('http://', 'https://')):
            url_text = 'https://' + url_text
        self.view.setUrl(QUrl(url_text))

    def _update_address_bar(self, url: QUrl):
        self.address_bar.setText(url.toString())
        self.back_button.setEnabled(self.view.history().canGoBack())
        self.forward_button.setEnabled(self.view.history().canGoForward())

    def _on_load_started(self):
        self.reload_button.setIcon(qta.icon('mdi.close', color='grey'))
        try: self.reload_button.clicked.disconnect()
        except TypeError: pass
        self.reload_button.clicked.connect(self.view.stop)

    def _on_load_finished(self):
        self.reload_button.setIcon(qta.icon('mdi.reload', color='grey'))
        try: self.reload_button.clicked.disconnect()
        except TypeError: pass
        self.reload_button.clicked.connect(self.view.reload)
        self._update_address_bar(self.view.url())

    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        toolbar_bg = colors.get('sidebar.background', '#252526')
        border = colors.get('input.border', '#3c3c3c')
        privacy_bar_bg = colors.get('statusbar.background', '#007acc')
        privacy_bar_fg = colors.get('statusbar.foreground', '#ffffff')
        privacy_label_fg = colors.get('syntax.comment', '#808080')

        self.setStyleSheet(f"""
            #BrowserToolbar {{
                background-color: {toolbar_bg};
                border-bottom: 1px solid {border};
            }}
            #BrowserPrivacyBar {{
                background-color: {toolbar_bg};
                border-top: 1px solid {border};
            }}
            #BrowserPrivacyLabel {{
                color: {privacy_label_fg};
                font-size: 9pt;
            }}
        """)
        
        if WEB_ENGINE_AVAILABLE:
            self.back_button.setIcon(qta.icon('mdi.arrow-left', color='grey'))
            self.forward_button.setIcon(qta.icon('mdi.arrow-right', color='grey'))
            self.reload_button.setIcon(qta.icon('mdi.reload', color='grey'))