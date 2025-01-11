from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from utils.helpers import format_file_size

class DownloadWidget(QWidget):
    def __init__(self, download_item, parent=None):
        super().__init__(parent)
        self.download_item = download_item
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # File info
        info_container = QWidget()
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 0, 0, 0)
        
        # Filename
        self.filename_label = QLabel(download_item.path().split('/')[-1])
        self.filename_label.setStyleSheet("color: white; font-weight: bold;")
        info_layout.addWidget(self.filename_label)
        
        # Progress bar and status
        progress_container = QWidget()
        progress_layout = QHBoxLayout(progress_container)
        progress_layout.setContentsMargins(0, 0, 0, 0)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #3F3F44;
                border-radius: 2px;
                background: #2B2A33;
                height: 20px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #0060DF;
                border-radius: 2px;
            }
        """)
        progress_layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("Starting...")
        self.status_label.setStyleSheet("color: #999;")
        progress_layout.addWidget(self.status_label)
        
        info_layout.addWidget(progress_container)
        layout.addWidget(info_container)
        
        # Control buttons
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(5)
        
        # Open folder button
        self.open_folder_btn = QPushButton()
        self.open_folder_btn.setIcon(QIcon("res/folder.png"))
        self.open_folder_btn.setToolTip("Open containing folder")
        self.open_folder_btn.clicked.connect(self.open_containing_folder)
        self.open_folder_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #52525E;
            }
        """)
        button_layout.addWidget(self.open_folder_btn)
        
        # Cancel/Remove button
        self.cancel_btn = QPushButton()
        self.cancel_btn.setIcon(QIcon("res/close.png"))
        self.cancel_btn.setToolTip("Cancel download")
        self.cancel_btn.clicked.connect(self.cancel_download)
        self.cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #52525E;
            }
        """)
        button_layout.addWidget(self.cancel_btn)
        
        layout.addWidget(button_container)
        
        # Connect download signals
        download_item.downloadProgress.connect(self.update_progress)
        download_item.stateChanged.connect(self.update_state)
        
        self.setStyleSheet("""
            QWidget {
                background-color: #1C1B22;
                border-radius: 4px;
            }
        """)
    
    def update_progress(self, bytes_received, bytes_total):
        """Update the progress bar and status label."""
        progress = (bytes_received * 100) / bytes_total
        self.progress_bar.setValue(int(progress))
        
        # Update status with file size
        received_size = format_file_size(bytes_received)
        total_size = format_file_size(bytes_total)
        self.status_label.setText(f"{received_size} of {total_size}")
    
    def update_state(self, state):
        """Update the widget state based on download state."""
        from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem
        
        if state == QWebEngineDownloadItem.DownloadCompleted:
            self.status_label.setText("Completed")
            self.status_label.setStyleSheet("color: #00C853;")
            self.cancel_btn.setIcon(QIcon("res/delete.png"))
            self.cancel_btn.setToolTip("Remove from list")
        elif state == QWebEngineDownloadItem.DownloadCancelled:
            self.status_label.setText("Cancelled")
            self.status_label.setStyleSheet("color: #FF5252;")
        elif state == QWebEngineDownloadItem.DownloadInterrupted:
            self.status_label.setText("Failed")
            self.status_label.setStyleSheet("color: #FF5252;")
    
    def open_containing_folder(self):
        """Open the folder containing the downloaded file."""
        path = self.download_item.path()
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.dirname(path)))
    
    def cancel_download(self):
        """Cancel the download or remove it from the list if completed."""
        from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem
        
        if self.download_item.state() == QWebEngineDownloadItem.DownloadInProgress:
            self.download_item.cancel()
        else:
            # Remove from list if completed
            self.parent().remove_download(self) 