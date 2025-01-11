from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from PyQt5.QtCore import QSettings
from config.translations import translations
from .download_widget import DownloadWidget

class DownloadsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QSettings('Solar', 'Browser')
        self.current_language = self.settings.value('language', 'en')
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(20)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        title = QLabel(translations[self.current_language]['downloads'])
        title.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        header_layout.addWidget(title)
        
        self.clear_all_btn = QPushButton("Clear All")
        self.clear_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:disabled {
                background-color: #666;
                color: #999;
            }
        """)
        self.clear_all_btn.clicked.connect(self.clear_all_downloads)
        self.clear_all_btn.setEnabled(False)  # Initially disabled
        header_layout.addWidget(self.clear_all_btn, alignment=Qt.AlignRight)
        
        layout.addWidget(header)
        
        # Downloads list
        self.downloads_container = QWidget()
        self.downloads_layout = QVBoxLayout(self.downloads_container)
        self.downloads_layout.setContentsMargins(0, 0, 0, 0)
        self.downloads_layout.setSpacing(10)
        
        # Empty state message
        self.empty_label = QLabel("No downloads yet")
        self.empty_label.setStyleSheet("""
            QLabel {
                color: #999;
                font-size: 14px;
                padding: 20px;
            }
        """)
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.downloads_layout.addWidget(self.empty_label)
        
        self.downloads_layout.addStretch()
        
        # Scroll area for downloads
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.downloads_container)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background: #2B2A33;
                width: 14px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #3F3F44;
                min-height: 20px;
                border-radius: 7px;
                margin: 2px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        layout.addWidget(self.scroll)
        
        # Keep track of downloads
        self.download_widgets = []
    
    def add_download(self, download_item):
        """Add a new download to the list."""
        # Remove empty state if this is the first download
        if not self.download_widgets:
            self.empty_label.hide()
            self.clear_all_btn.setEnabled(True)
        
        # Remove stretch
        if self.downloads_layout.count() > 0:
            self.downloads_layout.takeAt(self.downloads_layout.count() - 1)
        
        # Add new download widget
        download_widget = DownloadWidget(download_item, self)
        self.downloads_layout.addWidget(download_widget)
        self.download_widgets.append(download_widget)
        
        # Add stretch back
        self.downloads_layout.addStretch()
    
    def remove_download(self, download_widget):
        """Remove a download from the list."""
        if download_widget in self.download_widgets:
            self.downloads_layout.removeWidget(download_widget)
            self.download_widgets.remove(download_widget)
            download_widget.deleteLater()
            
            # Show empty state if no downloads left
            if not self.download_widgets:
                self.empty_label.show()
                self.clear_all_btn.setEnabled(False)
    
    def clear_all_downloads(self):
        """Clear all downloads from the list."""
        # Clear all downloads except the empty label and stretch
        for widget in self.download_widgets[:]:  # Create a copy of the list to iterate
            self.remove_download(widget)
        
        # Reset the list
        self.download_widgets = []
        
        # Show empty state
        self.empty_label.show()
        self.clear_all_btn.setEnabled(False) 