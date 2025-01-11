from PyQt5.QtCore import QStandardPaths

# Application Constants
APP_NAME = 'Solar'
APP_VERSION = 'sdpyqt0.0.0.2-bt'
ORGANIZATION_NAME = 'Solar'
APPLICATION_NAME = 'Browser'

# Default Settings
DEFAULT_LANGUAGE = 'en'
DEFAULT_SEARCH_ENGINE = 'Google'
DEFAULT_HOMEPAGE = 'https://www.google.com'
DEFAULT_DOWNLOAD_LOCATION = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)

# Default Shortcuts
DEFAULT_SHORTCUTS = {
    'back': 'Alt+Left',
    'forward': 'Alt+Right',
    'reload': 'Ctrl+R',
    'home': 'Alt+Home',
    'close_tab': 'Ctrl+W',
    'new_tab': 'Ctrl+T',
    'quit': 'Ctrl+Q'
}

# Search Engines
SEARCH_ENGINES = {
    'Google': 'https://www.google.com/search?q=',
    'DuckDuckGo': 'https://duckduckgo.com/?q=',
    'Bing': 'https://www.bing.com/search?q=',
    'Yandex': 'https://yandex.com/search/?text='
}

# UI Constants
MINIMUM_WINDOW_SIZE = (1000, 800)
TAB_MINIMUM_WIDTH = 100
TAB_PREFERRED_WIDTH = 240
ICON_SIZE = 16
ANIMATION_DURATION = 250

# Style Constants
STYLE_SHEETS = {
    'main_window': """
        QMainWindow {
            background-color: white;
        }
    """,
    'tab_button': """
        QPushButton {
            background-color: #f5f5f5;
            border: none;
            border-radius: 8px;
            padding: 4px 8px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #ebebeb;
        }
    """,
    'url_bar': """
        QLineEdit {
            border: none;
            background: transparent;
            padding: 4px;
            font-size: 13px;
            selection-background-color: #cce8ff;
        }
    """,
    'menu': """
        QMenu {
            background-color: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 5px;
        }
        QMenu::item {
            color: black;
            background-color: transparent;
            padding: 8px 25px;
            margin: 2px 5px;
            border-radius: 4px;
            font-size: 13px;
        }
        QMenu::item:selected {
            background-color: #f0f0f0;
        }
        QMenu::separator {
            height: 1px;
            background-color: #e0e0e0;
            margin: 5px 15px;
        }
    """
} 