import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QDialog,
    QTabWidget, QCheckBox, QGroupBox, QRadioButton, QComboBox, QMessageBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt, QMimeData, QSettings, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QDrag

translations = {
    'tr': {
        'settings': 'Ayarlar',
        'general': 'Genel',
        'general_settings': 'Genel Ayarlar',
        'startup': 'Başlangıç',
        'startup_settings': 'Başlangıç Ayarları',
        'search': 'Arama',
        'search_settings': 'Arama Ayarları',
        'privacy': 'Gizlilik',
        'privacy_security': 'Gizlilik ve Güvenlik',
        'language': 'Dil',
        'language_settings': 'Dil Ayarları',
        'save_settings': 'Ayarları Kaydet',
        'settings_saved': 'Ayarlar kaydedildi!',
        'show_on_startup': 'Başlangıçta Göster',
        'default_search': 'Varsayılan Arama Motoru',
        'clear_data': 'Tarama Verilerini Temizle',
        'preferred_language': 'Tercih Edilen Dil:',
        'language_restart_note': 'Not: Dil değişikliğinin tamamen uygulanması için tarayıcıyı yeniden başlatmanız gerekebilir.'
    },
    'en': {
        'settings': 'Settings',
        'general': 'General',
        'general_settings': 'General Settings',
        'startup': 'Startup',
        'startup_settings': 'Startup Settings',
        'search': 'Search',
        'search_settings': 'Search Settings',
        'privacy': 'Privacy',
        'privacy_security': 'Privacy and Security',
        'language': 'Language',
        'language_settings': 'Language Settings',
        'save_settings': 'Save Settings',
        'settings_saved': 'Settings saved!',
        'show_on_startup': 'Show on Startup',
        'default_search': 'Default Search Engine',
        'clear_data': 'Clear Browsing Data',
        'preferred_language': 'Preferred Language:',
        'language_restart_note': 'Note: Browser restart may be required for language changes to take full effect.'
    }
}

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        title = QLabel("Settings (not working)")
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
                background-color: white;
            }
        """)
        self.layout.addWidget(title)
        
        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)  
        
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: none;
                background: white;
            }
            QTabWidget::tab-bar {
                alignment: left;
            }
            QTabBar::tab {
                padding: 15px 30px;
                min-width: 200px;
                text-align: left;
                background: #f0f0f0;
                border: none;
                border-right: 2px solid transparent;
            }
            QTabBar::tab:hover {
                background: #e0e0e0;
            }
            QTabBar::tab:selected {
                background: white;
                border-right: 2px solid #0078D4;
                color: #0078D4;
            }
        """)
        
        self.setup_general_settings()
        self.setup_startup_settings()
        self.setup_search_settings()
        self.setup_privacy_settings()
        
        container_layout.addWidget(self.tab_widget)
        self.layout.addWidget(container)

    def setup_general_settings(self):
        general_widget = QWidget()
        layout = QVBoxLayout(general_widget)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(20)
        
        header = QLabel("General settings")
        header.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(header)
        
        settings = [
            ("Default browser", "Set the Solar as a default browser", False),
            ("Ask on leave", "Always ask to close browser", False),
            ("Save tabs", "Save the last tabs while closing browser.", False)
        ]
        
        for title, description, default_state in settings:
            setting_widget = QWidget()
            setting_layout = QVBoxLayout(setting_widget)
            setting_layout.setContentsMargins(0, 0, 0, 0)
            
            switch = QCheckBox(title)
            switch.setChecked(default_state)
            description_label = QLabel(description)
            description_label.setStyleSheet("color: #666; font-size: 12px;")
            
            setting_layout.addWidget(switch)
            setting_layout.addWidget(description_label)
            
            layout.addWidget(setting_widget)
        
        layout.addStretch()
        self.tab_widget.addTab(general_widget, "Genel")

    def setup_startup_settings(self):
        startup_widget = QWidget()
        layout = QVBoxLayout(startup_widget)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(20)
        
        header = QLabel("Start Settings")
        header.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(header)
        
        group = QGroupBox("Show on start:")
        group_layout = QVBoxLayout()
        
        options = [
            ("New tab", True),
            ("Web page", False),
            ("From last page(s)", False)
        ]
        
        for text, checked in options:
            radio = QRadioButton(text)
            radio.setChecked(checked)
            group_layout.addWidget(radio)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
        
        url_container = QWidget()
        url_layout = QHBoxLayout(url_container)
        url_layout.setContentsMargins(0, 0, 0, 0)
        
        url_input = QLineEdit()
        url_input.setPlaceholderText("https://")
        url_input.setEnabled(False)
        
        url_layout.addWidget(QLabel("URL:"))
        url_layout.addWidget(url_input)
        
        layout.addWidget(url_container)
        layout.addStretch()
        
        self.tab_widget.addTab(startup_widget, "Start")

    def setup_search_settings(self):
        search_widget = QWidget()
        layout = QVBoxLayout(search_widget)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(20)
        
        header = QLabel("Search Settings")
        header.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(header)
        
        group = QGroupBox("Default search engine")
        group_layout = QVBoxLayout()
        
        engines = [
            ("Google", True),
            ("DuckDuckGo", False),
            ("Yandex", False)
        ]
        
        for engine, checked in engines:
            radio = QRadioButton(engine)
            radio.setChecked(checked)
            group_layout.addWidget(radio)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
        
        suggestions = QCheckBox("Show search suggestions")
        suggestions.setChecked(True)
        layout.addWidget(suggestions)
        
        layout.addStretch()
        self.tab_widget.addTab(search_widget, "Search")

    def setup_privacy_settings(self):
        privacy_widget = QWidget()
        layout = QVBoxLayout(privacy_widget)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(20)
        
        header = QLabel("Gizlilik ve Güvenlik")
        header.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(header)
        
        settings = [
            ("Accept the cookies", "Give access to use cookies the web sites you entered.", False),
            ("Do Not Track", "Send 'Do not follow' request.", False),
            ("Pop-up blocker", "Block the pop-up windows", False),
            ("Install", "Do not ask location to install everytime", False),
            ("Location access", "Give access to use location the web sites you entered.", False)
        ]
        
        for title, description, default_state in settings:
            setting_widget = QWidget()
            setting_layout = QVBoxLayout(setting_widget)
            setting_layout.setContentsMargins(0, 0, 0, 0)
            
            switch = QCheckBox(title)
            switch.setChecked(default_state)
            description_label = QLabel(description)
            description_label.setStyleSheet("color: #666; font-size: 12px;")
            
            setting_layout.addWidget(switch)
            setting_layout.addWidget(description_label)
            
            layout.addWidget(setting_widget)
        
        clear_btn = QPushButton("Clear search history.")
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #0078D4;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #106EBE;
            }
        """)
        
        layout.addSpacing(20)
        layout.addWidget(clear_btn)
        layout.addStretch()
        
        self.tab_widget.addTab(privacy_widget, "Privacy")

class TabButton(QPushButton):
    def __init__(self, title, favicon, close_callback, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.minimum_width = 40 
        self.preferred_width = 200  
        self.setFixedHeight(30)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid white;
                border-radius: 4px;
                padding: 4px 5px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(2,2,2,2)
        self.main_layout.setSpacing(2)
        self.setLayout(self.main_layout)

        self.favicon = QLabel()
        if favicon:
            self.favicon.setPixmap(favicon.scaled(20, 20))
        else:
            self.favicon.setPixmap(QPixmap("favicon.png").scaled(20, 20))
        self.favicon.setFixedSize(20, 20)
        self.main_layout.addWidget(self.favicon)

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size: 11px;")
        self.main_layout.addWidget(self.title_label)

        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(20, 20)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 14px;
                color: #666;
            }
            QPushButton:hover {
                background-color: #ff4444;
                color: white;
                border-radius: 2px;
            }
        """)
        self.close_btn.clicked.connect(close_callback)
        self.main_layout.addWidget(self.close_btn)

        self.setFixedWidth(self.preferred_width)

    def updateWidth(self, available_width):
        new_width = min(max(self.minimum_width, available_width), self.preferred_width)
        self.setFixedWidth(new_width)
        
        if new_width <= self.minimum_width:
            self.title_label.hide()
            self.close_btn.hide()
        else:
            self.title_label.show()
            self.close_btn.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if not hasattr(self, 'drag_start_pos'):
            return
            
        if (event.pos() - self.drag_start_pos).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText('tab_drag')
        drag.setMimeData(mime_data)
        
        drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText() and event.mimeData().text() == 'tab_drag':
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasText() and event.mimeData().text() == 'tab_drag':
            source_tab = event.source()
            if source_tab != self:
                browser = self.window()
                source_idx = browser.get_tab_index(source_tab)
                target_idx = browser.get_tab_index(self)
                browser.move_tab(source_idx, target_idx)


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs = []
        self.current_tab = None

        self.show_warning()

    def show_warning(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)  
        msg.setWindowTitle("Warning")
        msg.setText("This is a warning message. Solar Browser Python Edition is in development stage. Even though it uses PyQtWebEngine, all the things you do is in your own responsibility. DO NOT ENTER your bank account or something IMPORTANT. Thanks for your attention.")
        msg.setInformativeText("Did you understand?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        response = msg.exec_()
        if response == QMessageBox.No:
            sys.exit()


        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)

        self.setup_top_bar(layout)
        self.setup_navigation_bar(layout)
        self.setup_web_container(layout)

        self.add_new_tab()
        self.setMinimumSize(1000, 800)

        self.drag_pos = None
        self.setWindowFlag(Qt.FramelessWindowHint)

    def setup_top_bar(self, parent_layout):
        top_bar = QWidget()
        top_bar.setFixedHeight(40)
        top_bar.setStyleSheet("background-color: #f0f0f0;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(5,0,5,0)
        top_layout.setSpacing(2)

        tab_container_wrapper = QWidget()
        tab_container_layout = QVBoxLayout(tab_container_wrapper)
        tab_container_layout.setContentsMargins(0,0,0,0)
        
        self.tab_container = QWidget()
        self.tab_layout = QHBoxLayout(self.tab_container)
        self.tab_layout.setContentsMargins(0,0,0,0)
        self.tab_layout.setSpacing(2)
        self.tab_layout.setAlignment(Qt.AlignLeft)
        
        tab_container_layout.addStretch()
        tab_container_layout.addWidget(self.tab_container)
        tab_container_layout.addStretch()
        
        top_layout.addWidget(tab_container_wrapper, stretch=1)

        window_controls = QWidget()
        window_layout = QHBoxLayout(window_controls)
        window_layout.setContentsMargins(0,0,0,0)
        window_layout.setSpacing(0)

        min_btn = QPushButton("−")
        max_btn = QPushButton("□")
        close_btn = QPushButton("×")
        
        for btn in [min_btn, max_btn, close_btn]:
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #ddd;
                }
            """)
            window_layout.addWidget(btn)

        min_btn.clicked.connect(self.showMinimized)
        max_btn.clicked.connect(self.toggle_maximize)
        close_btn.clicked.connect(self.close)
        
        top_layout.addWidget(window_controls)
        parent_layout.addWidget(top_bar)

    def setup_navigation_bar(self, parent_layout):
        nav_panel = QWidget()
        nav_panel.setFixedHeight(35)
        nav_layout = QHBoxLayout(nav_panel)
        nav_layout.setContentsMargins(5,0,5,0)
        nav_panel.setStyleSheet("background-color: white")

        nav_buttons = [
            ("←", self.go_back),
            ("→", self.go_forward),
            ("↻", self.reload_page)
        ]

        for btn_text, callback in nav_buttons:
            btn = QPushButton(btn_text)
            btn.setFixedSize(25, 25)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            btn.clicked.connect(callback)
            nav_layout.addWidget(btn)

        center_container = QWidget()
        center_layout = QHBoxLayout(center_container)
        center_layout.setContentsMargins(0,0,0,0)
        
        warn_msg = QLabel("Do not enter your bank account or something important in this browser. If you enter, this will be in your responsibility!")
        warn_msg.setStyleSheet("""
            QLabel{
                background-color: red;
                border: 1px solid #ccc;
                border-radius: 4px;
                color: white; 
                padding: 5px;
            }
        """)
        center_layout.addWidget(warn_msg)

        self.url_bar = QLineEdit()
        self.url_bar.setFixedWidth(600)
        self.url_bar.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 4px;
                background: white;
            }
        """)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        center_layout.addWidget(self.url_bar)
        
        nav_layout.addWidget(center_container, alignment=Qt.AlignCenter)
        
        settings_btn = QPushButton("⚙")
        settings_btn.setFixedSize(25, 25)
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        settings_btn.clicked.connect(self.show_settings)
        nav_layout.addWidget(settings_btn)

        parent_layout.addWidget(nav_panel)

    def setup_web_container(self, parent_layout):
        self.web_container = QWidget()
        self.web_layout = QVBoxLayout(self.web_container)
        self.web_layout.setContentsMargins(0,0,0,0)
        self.web_layout.setSpacing(0)
        parent_layout.addWidget(self.web_container, stretch=1)

    def show_settings(self):
        settings_widget = SettingsWidget()
        
        if hasattr(self, 'new_tab_btn'):
            self.tab_layout.removeWidget(self.new_tab_btn)
            self.new_tab_btn.setParent(None)
        
        current_index = len(self.tabs)
        tab_button = TabButton("Settings", None, lambda: self.close_tab(current_index))
        tab_button.clicked.connect(lambda: self.switch_to_tab(current_index))
        self.tab_layout.addWidget(tab_button)
        
        settings_widget.hide()
        self.web_layout.addWidget(settings_widget)
        self.tabs.append((tab_button, settings_widget))
        
        if not hasattr(self, 'new_tab_btn'):
            self.new_tab_btn = QPushButton("+")
            self.new_tab_btn.setFixedSize(25, 25)
            self.new_tab_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    font-size: 16px;
                    margin-left: 2px;
                }
                QPushButton:hover {
                    background-color: #ddd;
                }
            """)
            self.new_tab_btn.clicked.connect(self.add_new_tab)
        
        self.tab_layout.addWidget(self.new_tab_btn)
        self.update_tab_layout()
        self.switch_to_tab(current_index)

    def add_new_tab(self):
        if hasattr(self, 'new_tab_btn'):
            self.tab_layout.removeWidget(self.new_tab_btn)
            self.new_tab_btn.setParent(None)
        
        current_index = len(self.tabs)
        tab_button = TabButton("Yeni Sekme", None, lambda: self.close_tab(current_index))
        tab_button.clicked.connect(lambda: self.switch_to_tab(current_index))
        self.tab_layout.addWidget(tab_button)
        
       
        web_view = QWebEngineView()
        web_view.setUrl(QUrl("https://www.google.com"))
        web_view.hide()

        web_view.page().titleChanged.connect(lambda title: self.update_tab_title_and_icon(tab_button, title, web_view))
        web_view.page().iconChanged.connect(lambda icon: self.update_tab_title_and_icon(tab_button, web_view.page().title(), web_view))
        web_view.urlChanged.connect(lambda url: self.update_url_bar(url))
        
        self.web_layout.addWidget(web_view)
        self.tabs.append((tab_button, web_view))
        
        if not hasattr(self, 'new_tab_btn'):
            self.new_tab_btn = QPushButton("+")
            self.new_tab_btn.setFixedSize(25, 25)
            self.new_tab_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    font-size: 16px;
                    margin-left: 2px;
                }
                QPushButton:hover {
                    background-color: #ddd;
                }
            """)
            self.new_tab_btn.clicked.connect(self.add_new_tab)
        
        self.tab_layout.addWidget(self.new_tab_btn)
        self.update_tab_layout()
        self.switch_to_tab(current_index)

    def update_tab_title_and_icon(self, tab, title, web_view):
        short_title = title[:15] + "..." if len(title) > 15 else title
        tab.title_label.setText(short_title)
        favicon = web_view.page().icon()
        if not favicon.isNull():
            tab.favicon.setPixmap(favicon.pixmap(16, 16))
        self.update_tab_layout()

    def close_tab(self, index):
        if not self.tabs or index >= len(self.tabs):
            return
            
        if len(self.tabs) > 1:
            self.tabs[index][1].hide()
            
            to_remove = self.tabs.pop(index)
            to_remove[1].deleteLater()
            to_remove[0].deleteLater()
            
            if index <= self.current_tab:
                self.current_tab = max(0, self.current_tab - 1)
            
            for i, (tab, _) in enumerate(self.tabs):
                tab.close_btn.clicked.disconnect()
                tab.close_btn.clicked.connect(lambda idx=i: self.close_tab(idx))
            
            self.update_tab_layout()
            self.switch_to_tab(self.current_tab)
        else:
            self.close()

    def switch_to_tab(self, index):
        if not self.tabs or index >= len(self.tabs):
            return
            
        if self.current_tab is not None and self.current_tab < len(self.tabs):
            current_widget = self.tabs[self.current_tab][1]
            current_tab_button = self.tabs[self.current_tab][0]
            current_widget.hide()
            current_tab_button.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    padding: 2px 5px;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)
        
        self.current_tab = index
        new_widget = self.tabs[index][1]
        new_tab_button = self.tabs[index][0]
        new_widget.show()
        new_tab_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 2px 5px;
                text-align: left;
            }
        """)
        
        if isinstance(new_widget, QWebEngineView):
            self.url_bar.setText(new_widget.url().toString())

    def get_tab_index(self, tab_button):
        for i, (btn, _) in enumerate(self.tabs):
            if btn == tab_button:
                return i
        return -1

    def move_tab(self, from_idx, to_idx):
        if from_idx == to_idx:
            return
            
        tab = self.tabs.pop(from_idx)
        self.tabs.insert(to_idx, tab)
        
        for i, (tab, _) in enumerate(self.tabs):
            tab.close_btn.clicked.disconnect()
            tab.close_btn.clicked.connect(lambda idx=i: self.close_tab(idx))
        
        self.update_tab_layout()
        
        if self.current_tab == from_idx:
            self.current_tab = to_idx
        elif from_idx < self.current_tab <= to_idx:
            self.current_tab -= 1
        elif to_idx <= self.current_tab < from_idx:
            self.current_tab += 1


    def update_tab_layout(self):
            for i in reversed(range(self.tab_layout.count())):
                widget = self.tab_layout.itemAt(i).widget()
                if widget != self.new_tab_btn:
                    widget.setParent(None)
            
            available_width = (self.tab_container.width() - 30) // max(len(self.tabs), 1)
            
            for tab, _ in self.tabs:
                tab.updateWidth(available_width)
                self.tab_layout.addWidget(tab)
            
            self.tab_layout.addWidget(self.new_tab_btn)

    def update_url_bar(self, url):
            if self.current_tab is not None:
                current_widget = self.tabs[self.current_tab][1]
                if isinstance(current_widget, QWebEngineView) and current_widget.hasFocus():
                    self.url_bar.setText(url.toString())

    def toggle_maximize(self):
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

    def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton and event.y() < 30:
                self.drag_pos = event.globalPos() - self.pos()
                event.accept()

    def mouseMoveEvent(self, event):
            if self.drag_pos and event.y() < 30:
                self.move(event.globalPos() - self.drag_pos)
                event.accept()

    def mouseReleaseEvent(self, event):
            self.drag_pos = None

    def resizeEvent(self, event):
            super().resizeEvent(event)
            self.update_tab_layout()

    def go_back(self):
            if self.current_tab is not None:
                current_widget = self.tabs[self.current_tab][1]
                if isinstance(current_widget, QWebEngineView) and current_widget.history().canGoBack():
                    current_widget.back()

    def go_forward(self):
            if self.current_tab is not None:
                current_widget = self.tabs[self.current_tab][1]
                if isinstance(current_widget, QWebEngineView) and current_widget.history().canGoForward():
                    current_widget.forward()

    def reload_page(self):
            if self.current_tab is not None:
                current_widget = self.tabs[self.current_tab][1]
                if isinstance(current_widget, QWebEngineView):
                    current_widget.reload()

    def navigate_to_url(self):
            if self.current_tab is not None:
                current_widget = self.tabs[self.current_tab][1]
                if isinstance(current_widget, QWebEngineView):
                    url = self.url_bar.text()
                    if not url.startswith("http://") and not url.startswith("https://"):
                        url = "https://www.google.com/search?q=" + url
                    current_widget.setUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())