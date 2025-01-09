import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QDialog,
    QTabWidget, QCheckBox, QGroupBox, QRadioButton, QComboBox, QMessageBox, QStackedWidget,
    QShortcut, QScrollArea, QProgressBar, QFileDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl, Qt, QMimeData, QSettings, QTimer, QSize, QStandardPaths
from PyQt5.QtGui import QIcon, QPixmap, QDrag, QKeySequence
from PyQt5.QtGui import QDesktopServices

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
        'language_restart_note': 'Not: Dil değişikliğinin tamamen uygulanması için tarayıcıyı yeniden başlatmanız gerekebilir.',
        'keyboard_shortcuts': 'Klavye Kısayolları',
        'search_suggestions': 'Arama Önerileri',
        'show_search_suggestions': 'Arama önerilerini göster',
        'custom_search_engine': 'Özel Arama Motoru',
        'search_engine_name': 'Arama Motoru Adı',
        'search_engine_url': 'Arama URL (sorgu için %s kullanın)',
        'security': 'Güvenlik',
        'downloads': 'İndirilenler',
        'tabs': 'Sekmeler',
        'restore_session': 'Önceki oturumu geri yükle',
        'warn_quit': 'Çıkışta uyar',
        'default_browser': 'Varsayılan tarayıcı yap',
        'custom_startup': 'Belirli bir sayfayı aç',
        'enter_url': 'URL girin (örn: https://www.google.com)',
        'navigation': 'Gezinme',
        'back': 'Geri',
        'forward': 'İleri',
        'reload': 'Yenile',
        'home': 'Ana Sayfa',
        'close_tab': 'Sekmeyi Kapat',
        'new_tab': 'Yeni Sekme',
        'quit': 'Çıkış',
        'accept_cookies': 'Çerezleri Kabul Et',
        'do_not_track': 'İzleme Yapma',
        'block_popups': 'Pop-up Pencereleri Engelle',
        'location_access': 'Konum Erişimi',
        'password_autofill': 'Otomatik Şifre Doldurma',
        'payment_autofill': 'Otomatik Ödeme Doldurma',
        'address_autofill': 'Otomatik Adres Doldurma',
        'safe_browsing': 'Güvenli Tarama',
        'always_use_https': 'Her zaman HTTPS kullan',
        'send_error_reports': 'Hata raporları gönder',
        'third_party_cookies': 'Üçüncü taraf çerezleri engelle',
        'fingerprinting': 'Parmak izi almayı engelle',
        'secure_dns': 'Güvenli DNS kullan',
        'insecure_content': 'Tehlikeli içeriği engelle',
        'certificate_warnings': 'Sertifika uyarılarını göster',
        'find_in_settings': 'Ayarlarda Ara',
        'accept': 'Kabul Et',
        'cancel': 'İptal',
        'custom': 'Özel',
        'about': 'Hakkında',
        'version': 'Sürüm',
        'developers': 'Geliştiriciler',
        'license': 'Lisans',
        'website': 'Web Sitesi',
        'description_restore_session': 'Önceki pencere ve sekmeleri aç',
        'description_warn_quit': 'Birden fazla sekmeyi kapatırken uyarı göster',
        'description_default_browser': 'Solar\'ı varsayılan tarayıcınız olarak ayarlayın',
        'description_custom_startup': 'Tarayıcı başladığında belirli bir sayfa aç',
        'description_accept_cookies': 'Web sitelerinin çerez saklamasına izin ver',
        'description_do_not_track': 'Web sitelerine \'İzleme Yapma\' sinyali gönder',
        'description_block_popups': 'Açılır pencereleri engelle',
        'description_location_access': 'Web sitelerinin konumunuzu istemesine izin ver',
        'description_password_autofill': 'Kaydedilen şifreleri otomatik doldur',
        'description_payment_autofill': 'Ödeme yöntemlerini kaydet ve doldur',
        'description_address_autofill': 'Adresleri kaydet ve doldur',
        'description_safe_browsing': 'Tehlikeli sitelere karşı koruma',
        'description_always_use_https': 'Mümkün olduğunda HTTPS bağlantılarını kullan',
        'description_send_error_reports': 'Tarayıcıyı geliştirmek için hata raporları gönder',
        'description_third_party_cookies': 'Sitelerin takip çerezlerini kullanmasını engelle',
        'description_fingerprinting': 'Sitelerin sistem özelliklerinizle sizi tanımlamasını engelle',
        'description_secure_dns': 'Gelişmiş güvenlik için DNS-over-HTTPS kullan',
        'description_insecure_content': 'Tehlikeli siteler hakkında uyarı al',
        'description_certificate_warnings': 'Geçersiz SSL sertifikaları hakkında uyarı göster',
        'downloads_settings': 'İndirme Ayarları',
        'download_location': 'İndirme Konumu',
        'ask_download_location': 'Her indirmede konum sor',
        'auto_open_downloads': 'İndirilen dosyaları otomatik aç',
        'show_downloads_when_start': 'İndirme başladığında indirilenler sayfasını göster',
        'clear_downloads_on_exit': 'Çıkışta indirme geçmişini temizle',
        'change_location': 'Değiştir',
        'current_location': 'Mevcut konum:',
        'clear_downloads': 'İndirme Geçmişini Temizle',
        'clear_downloads_description': 'Tüm indirme geçmişini temizle'
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
        'language_restart_note': 'Note: Browser restart may be required for language changes to take full effect.',
        'keyboard_shortcuts': 'Keyboard Shortcuts',
        'search_suggestions': 'Search Suggestions',
        'show_search_suggestions': 'Show search suggestions',
        'custom_search_engine': 'Custom Search Engine',
        'search_engine_name': 'Search Engine Name',
        'search_engine_url': 'Search URL (use %s for query)',
        'security': 'Security',
        'downloads': 'Downloads',
        'tabs': 'Tabs',
        'restore_session': 'Restore previous session',
        'warn_quit': 'Warn when quitting',
        'default_browser': 'Make default browser',
        'custom_startup': 'Open specific page',
        'enter_url': 'Enter URL (e.g., https://www.google.com)',
        'navigation': 'Navigation',
        'back': 'Back',
        'forward': 'Forward',
        'reload': 'Reload',
        'home': 'Home',
        'close_tab': 'Close Tab',
        'new_tab': 'New Tab',
        'quit': 'Quit',
        'accept_cookies': 'Accept Cookies',
        'do_not_track': 'Do Not Track',
        'block_popups': 'Block Pop-ups',
        'location_access': 'Location Access',
        'password_autofill': 'Password AutoFill',
        'payment_autofill': 'Payment AutoFill',
        'address_autofill': 'Address AutoFill',
        'safe_browsing': 'Safe Browsing',
        'always_use_https': 'Always use HTTPS',
        'send_error_reports': 'Send error reports',
        'third_party_cookies': 'Block third-party cookies',
        'fingerprinting': 'Block fingerprinting',
        'secure_dns': 'Use secure DNS',
        'insecure_content': 'Block dangerous content',
        'certificate_warnings': 'Show certificate warnings',
        'find_in_settings': 'Find in Settings',
        'accept': 'Accept',
        'cancel': 'Cancel',
        'custom': 'Custom',
        'about': 'About',
        'version': 'Version',
        'developers': 'Developers',
        'license': 'License',
        'website': 'Website',
        'description_restore_session': 'Open previous windows and tabs',
        'description_warn_quit': 'Show a warning when attempting to close multiple tabs',
        'description_default_browser': 'Set Solar as your default browser',
        'description_custom_startup': 'Open a specific page when browser starts',
        'description_accept_cookies': 'Allow websites to store cookies',
        'description_do_not_track': 'Send websites a \'Do Not Track\' signal',
        'description_block_popups': 'Block pop-up windows',
        'description_location_access': 'Allow websites to request your location',
        'description_password_autofill': 'Automatically fill in saved passwords',
        'description_payment_autofill': 'Save and fill payment methods',
        'description_address_autofill': 'Save and fill addresses',
        'description_safe_browsing': 'Protect against dangerous sites',
        'description_always_use_https': 'Upgrade connections to HTTPS when available',
        'description_send_error_reports': 'Help improve browser by sending reports',
        'description_third_party_cookies': 'Prevent sites from using tracking cookies',
        'description_fingerprinting': 'Prevent sites from identifying you via system characteristics',
        'description_secure_dns': 'Use DNS-over-HTTPS for enhanced security',
        'description_insecure_content': 'Get warnings about dangerous sites',
        'description_certificate_warnings': 'Warn about invalid SSL certificates',
        'downloads_settings': 'Download Settings',
        'download_location': 'Download Location',
        'ask_download_location': 'Ask where to save each file before downloading',
        'auto_open_downloads': 'Open certain file types after downloading',
        'show_downloads_when_start': 'Show downloads page when a download starts',
        'clear_downloads_on_exit': 'Clear download history when browser closes',
        'change_location': 'Change',
        'current_location': 'Current location:',
        'clear_downloads': 'Clear Downloads',
        'clear_downloads_description': 'Clear all download history'
    },
    'ru': {
        'settings': 'Настройки',
        'general': 'Общие',
        'general_settings': 'Общие настройки',
        'startup': 'Запуск',
        'startup_settings': 'Настройки запуска',
        'search': 'Поиск',
        'search_settings': 'Настройки поиска',
        'privacy': 'Конфиденциальность',
        'privacy_security': 'Конфиденциальность и безопасность',
        'language': 'Язык',
        'language_settings': 'Языковые настройки',
        'save_settings': 'Сохранить настройки',
        'settings_saved': 'Настройки сохранены!',
        'show_on_startup': 'Показывать при запуске',
        'default_search': 'Поисковая система по умолчанию',
        'clear_data': 'Очистить данные браузера',
        'preferred_language': 'Предпочитаемый язык:',
        'language_restart_note': 'Примечание: Для полного применения изменений языка может потребоваться перезапуск браузера.',
        'keyboard_shortcuts': 'Сочетания клавиш',
        'search_suggestions': 'Поисковые подсказки',
        'show_search_suggestions': 'Показывать поисковые подсказки',
        'custom_search_engine': 'Пользовательская поисковая система',
        'search_engine_name': 'Название поисковой системы',
        'search_engine_url': 'URL поиска (используйте %s для запроса)',
        'security': 'Безопасность',
        'downloads': 'Загрузки',
        'tabs': 'Вкладки',
        'restore_session': 'Восстановить предыдущую сессию',
        'warn_quit': 'Предупреждать при выходе',
        'default_browser': 'Сделать браузером по умолчанию',
        'custom_startup': 'Открыть определенную страницу',
        'enter_url': 'Введите URL (например, https://www.google.com)',
        'navigation': 'Навигация',
        'back': 'Назад',
        'forward': 'Вперед',
        'reload': 'Обновить',
        'home': 'Домой',
        'close_tab': 'Закрыть вкладку',
        'new_tab': 'Новая вкладка',
        'quit': 'Выход',
        'accept_cookies': 'Принимать куки',
        'do_not_track': 'Не отслеживать',
        'block_popups': 'Блокировать всплывающие окна',
        'location_access': 'Доступ к местоположению',
        'password_autofill': 'Автозаполнение паролей',
        'payment_autofill': 'Автозаполнение платежей',
        'address_autofill': 'Автозаполнение адресов',
        'safe_browsing': 'Безопасный просмотр',
        'always_use_https': 'Всегда использовать HTTPS',
        'send_error_reports': 'Отправлять отчеты об ошибках',
        'third_party_cookies': 'Блокировать сторонние куки',
        'fingerprinting': 'Блокировать сбор цифровых отпечатков',
        'secure_dns': 'Использовать безопасный DNS',
        'insecure_content': 'Блокировать опасный контент',
        'certificate_warnings': 'Показывать предупреждения о сертификатах',
        'find_in_settings': 'Найти в настройках',
        'accept': 'Принять',
        'cancel': 'Отмена',
        'custom': 'Пользовательский',
        'about': 'О программе',
        'version': 'Версия',
        'developers': 'Разработчики',
        'license': 'Лицензия',
        'website': 'Веб-сайт',
        'description_restore_session': 'Открыть предыдущие окна и вкладки',
        'description_warn_quit': 'Показывать предупреждение при закрытии нескольких вкладок',
        'description_default_browser': 'Сделать Solar браузером по умолчанию',
        'description_custom_startup': 'Открывать определенную страницу при запуске браузера',
        'description_accept_cookies': 'Разрешить сайтам сохранять куки',
        'description_do_not_track': 'Отправлять сайтам сигнал \'Не отслеживать\'',
        'description_block_popups': 'Блокировать всплывающие окна',
        'description_location_access': 'Разрешить сайтам запрашивать ваше местоположение',
        'description_password_autofill': 'Автоматически заполнять сохраненные пароли',
        'description_payment_autofill': 'Сохранять и заполнять способы оплаты',
        'description_address_autofill': 'Сохранять и заполнять адреса',
        'description_safe_browsing': 'Защита от опасных сайтов',
        'description_always_use_https': 'Использовать HTTPS, когда доступно',
        'description_send_error_reports': 'Помогать улучшать браузер, отправляя отчеты',
        'description_third_party_cookies': 'Запретить сайтам использовать куки отслеживания',
        'description_fingerprinting': 'Запретить сайтам идентифицировать вас по характеристикам системы',
        'description_secure_dns': 'Использовать DNS-over-HTTPS для повышенной безопасности',
        'description_insecure_content': 'Получать предупреждения об опасных сайтах',
        'description_certificate_warnings': 'Предупреждать о недействительных SSL-сертификатах',
        'downloads_settings': 'Настройки загрузки',
        'download_location': 'Папка загрузки',
        'ask_download_location': 'Спрашивать, где сохранить каждый файл перед загрузкой',
        'auto_open_downloads': 'Открывать определенные типы файлов после загрузки',
        'show_downloads_when_start': 'Показывать страницу загрузок при начале загрузки',
        'clear_downloads_on_exit': 'Очищать историю загрузок при закрытии браузера',
        'change_location': 'Изменить',
        'current_location': 'Текущая папка:',
        'clear_downloads': 'Очистить загрузки',
        'clear_downloads_description': 'Очистить всю историю загрузок'
    }
}

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QSettings('Solar', 'Browser')
        self.current_language = self.settings.value('language', 'en')
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # Notification panel
        self.notification_container = QWidget()
        self.notification_container.setFixedHeight(0)  # Initially hidden
        self.notification_container.setStyleSheet("""
            QWidget {
                background-color: #1C1B22;
                border-bottom: 1px solid #3F3F44;
            }
        """)
        notification_layout = QHBoxLayout(self.notification_container)
        notification_layout.setContentsMargins(20, 10, 20, 10)
        
        self.notification_label = QLabel("")
        self.notification_label.setStyleSheet("color: white; font-size: 13px;")
        notification_layout.addWidget(self.notification_label)
        
        self.notification_buttons = QWidget()
        notification_buttons_layout = QHBoxLayout(self.notification_buttons)
        notification_buttons_layout.setContentsMargins(0, 0, 0, 0)
        notification_buttons_layout.setSpacing(10)
        
        self.accept_btn = QPushButton("Accept")
        self.accept_btn.setStyleSheet("""
            QPushButton {
                background-color: #0060DF;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0250BB;
            }
        """)
        self.accept_btn.clicked.connect(self.accept_changes)
        
        self.reject_btn = QPushButton("Cancel")
        self.reject_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: 1px solid #3F3F44;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #52525E;
            }
        """)
        self.reject_btn.clicked.connect(self.reject_changes)
        
        notification_buttons_layout.addWidget(self.accept_btn)
        notification_buttons_layout.addWidget(self.reject_btn)
        notification_layout.addWidget(self.notification_buttons)
        
        self.notification_container.hide()
        self.layout.addWidget(self.notification_container)
        
        # Search bar at top
        search_container = QWidget()
        search_container.setStyleSheet("background-color: #2B2A33;")
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(20, 10, 20, 10)
        
        # Save settings button
        save_button = QPushButton(translations[self.current_language]['save_settings'])
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #0060DF;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 13px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #0250BB;
            }
        """)
        save_button.clicked.connect(self.accept_changes)
        search_layout.addWidget(save_button)
        
        search_box = QLineEdit()
        search_box.setPlaceholderText("Find in Settings")
        search_box.setStyleSheet("""
            QLineEdit {
                background-color: #1C1B22;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 8px;
                color: white;
                font-size: 13px;
            }
        """)
        search_layout.addWidget(search_box)
        self.layout.addWidget(search_container)
        
        # Content area
        content = QWidget()
        content.setStyleSheet("""
            QWidget {
                background-color: #1C1B22;
                color: white;
            }
            QLabel {
                color: white;
                font-size: 13px;
            }
            QCheckBox {
                color: white;
                padding: 8px 5px;
                font-size: 13px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 1px solid #3F3F44;
                border-radius: 2px;
                background: #2B2A33;
            }
            QCheckBox::indicator:checked {
                background: #0060DF;
                border-color: #0060DF;
            }
            QRadioButton {
                color: white;
                padding: 8px 5px;
                font-size: 13px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 1px solid #3F3F44;
                border-radius: 9px;
                background: #2B2A33;
            }
            QRadioButton::indicator:checked {
                background: #0060DF;
                border-color: #0060DF;
            }
            QGroupBox {
                border: 1px solid #3F3F44;
                border-radius: 4px;
                margin-top: 1.5em;
                padding: 25px;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 7px;
                padding: 0 10px;
            }
            QComboBox {
                background-color: #2B2A33;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 8px;
                color: white;
                font-size: 13px;
                min-width: 200px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url(res/dropdown.png);
                width: 12px;
                height: 12px;
            }
            QLineEdit {
                background-color: #2B2A33;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 8px;
                color: white;
                font-size: 13px;
                min-width: 200px;
            }
            QPushButton {
                font-size: 13px;
            }
        """)
        
        # Sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #2B2A33;
                border-right: 1px solid #3F3F44;
            }
            QPushButton {
                text-align: left;
                padding: 12px 20px;
                border: none;
                border-radius: 0;
                color: white;
                background: transparent;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #52525E;
            }
            QPushButton[selected="true"] {
                background-color: #52525E;
                border-left: 4px solid #0df;
            }
        """)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Create sidebar buttons
        self.stack_widget = QStackedWidget()
        
        # General button and page
        general_btn = self.add_sidebar_button(translations[self.current_language]['general'], "res/settings_dark.svg")
        general_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(0))
        sidebar_layout.addWidget(general_btn)
        
        # Search button and page
        search_btn = self.add_sidebar_button(translations[self.current_language]['search'], "res/search_dark.svg")
        search_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(1))
        sidebar_layout.addWidget(search_btn)
        
        # Privacy button and page
        privacy_btn = self.add_sidebar_button(translations[self.current_language]['privacy_security'], "res/privacy_dark.png")
        privacy_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(2))
        sidebar_layout.addWidget(privacy_btn)
        
        # Language button and page
        language_btn = self.add_sidebar_button(translations[self.current_language]['language'], "res/language_dark.png")
        language_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(3))
        sidebar_layout.addWidget(language_btn)

        # Shortcuts button and page
        shortcuts_btn = self.add_sidebar_button(translations[self.current_language]['keyboard_shortcuts'], "res/keyboard_dark.png")
        shortcuts_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(4))
        sidebar_layout.addWidget(shortcuts_btn)
        
        # About button and page
        about_btn = self.add_sidebar_button(translations[self.current_language]['about'], "res/about_dark.png")
        about_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(5))
        sidebar_layout.addWidget(about_btn)
        
        sidebar_layout.addStretch()
        
        # Setup pages
        self.setup_general_page()
        self.setup_search_page()
        self.setup_privacy_page()
        self.setup_language_page()
        self.setup_shortcuts_page()
        self.setup_about_page()
        
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        content_layout.addWidget(sidebar)
        content_layout.addWidget(self.stack_widget, 1)
        
        self.layout.addWidget(content)

    def add_sidebar_button(self, text, icon_path):
        btn = QPushButton(text)
        if icon_path:
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(16, 16))
        return btn

    def setup_general_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(30)
        
        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
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
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(30)
        
        # Startup section
        startup_group = QGroupBox(translations[self.current_language]['startup'])
        startup_layout = QVBoxLayout()
        startup_layout.setSpacing(15)
        startup_layout.setContentsMargins(15, 15, 15, 15)
        
        self.general_checkboxes = {}
        startup_options = [
            ("restore_session", translations[self.current_language]['restore_session'], 
             translations[self.current_language]['description_restore_session']),
            ("warn_quit", translations[self.current_language]['warn_quit'], 
             translations[self.current_language]['description_warn_quit']),
            ("default_browser", translations[self.current_language]['default_browser'], 
             translations[self.current_language]['description_default_browser']),
            ("custom_startup", translations[self.current_language]['custom_startup'], 
             translations[self.current_language]['description_custom_startup'])
        ]
        
        for key, title, desc in startup_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 15)
            
            option = QCheckBox(title)
            option.setStyleSheet("""
                QCheckBox {
                    color: white;
                    font-size: 13px;
                    font-weight: normal;
                }
            """)
            option.setChecked(self.settings.value(key, False, type=bool))
            
            desc_label = QLabel(desc)
            desc_label.setStyleSheet("color: #999; font-size: 12px; padding-left: 25px;")
            desc_label.setWordWrap(True)
            
            self.general_checkboxes[key] = option
            option_layout.addWidget(option)
            option_layout.addWidget(desc_label)
            
            # Add startup page input
            if key == "custom_startup":
                self.startup_url = QLineEdit()
                self.startup_url.setPlaceholderText(translations[self.current_language]['enter_url'])
                self.startup_url.setText(self.settings.value("startup_url", "https://www.google.com"))
                self.startup_url.setStyleSheet("""
                    QLineEdit {
                        background-color: #2B2A33;
                        border: 1px solid #3F3F44;
                        border-radius: 4px;
                        padding: 8px;
                        color: white;
                        font-size: 13px;
                        margin-left: 25px;
                        margin-top: 5px;
                    }
                """)
                option_layout.addWidget(self.startup_url)
                
                # Enable/disable URL input based on checkbox
                option.stateChanged.connect(lambda state, input=self.startup_url: 
                    input.setEnabled(state == Qt.Checked))
                self.startup_url.setEnabled(option.isChecked())
            
            startup_layout.addWidget(option_container)
        
        startup_group.setLayout(startup_layout)
        scroll_layout.addWidget(startup_group)
        
        # Downloads section
        downloads_group = QGroupBox(translations[self.current_language]['downloads_settings'])
        downloads_layout = QVBoxLayout()
        downloads_layout.setSpacing(15)
        downloads_layout.setContentsMargins(15, 15, 15, 15)
        
        # Download location
        location_container = QWidget()
        location_layout = QVBoxLayout(location_container)
        location_layout.setContentsMargins(0, 0, 0, 15)
        
        location_label = QLabel(translations[self.current_language]['download_location'])
        location_label.setStyleSheet("color: white; font-size: 13px; font-weight: bold;")
        location_layout.addWidget(location_label)
        
        current_location = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        current_location_label = QLabel(f"{translations[self.current_language]['current_location']} {current_location}")
        current_location_label.setObjectName('current_location_label')
        current_location_label.setStyleSheet("color: #999; font-size: 12px; padding-left: 5px;")
        current_location_label.setWordWrap(True)
        location_layout.addWidget(current_location_label)
        
        change_location_btn = QPushButton(translations[self.current_language]['change_location'])
        change_location_btn.clicked.connect(self.change_download_location)
        change_location_btn.setStyleSheet("""
            QPushButton {
                background-color: #2B2A33;
                color: white;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 8px 16px;
                font-size: 13px;
                max-width: 100px;
                margin-left: 5px;
            }
            QPushButton:hover {
                background-color: #52525E;
            }
        """)
        location_layout.addWidget(change_location_btn)
        
        downloads_layout.addWidget(location_container)
        
        # Download options
        download_options = [
            ("ask_download_location", translations[self.current_language]['ask_download_location']),
            ("auto_open_downloads", translations[self.current_language]['auto_open_downloads']),
            ("show_downloads_when_start", translations[self.current_language]['show_downloads_when_start']),
            ("clear_downloads_on_exit", translations[self.current_language]['clear_downloads_on_exit'])
        ]
        
        for key, title in download_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 10)
            
            option = QCheckBox(title)
            option.setStyleSheet("""
                QCheckBox {
                    color: white;
                    font-size: 13px;
                    font-weight: normal;
                }
            """)
            option.setChecked(self.settings.value(key, False, type=bool))
            self.general_checkboxes[key] = option
            option_layout.addWidget(option)
            
            downloads_layout.addWidget(option_container)
        
        # Clear downloads button
        clear_downloads_container = QWidget()
        clear_downloads_layout = QVBoxLayout(clear_downloads_container)
        clear_downloads_layout.setContentsMargins(0, 15, 0, 0)
        
        clear_downloads_btn = QPushButton(translations[self.current_language]['clear_downloads'])
        clear_downloads_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        clear_downloads_btn.clicked.connect(self.clear_downloads_history)
        clear_downloads_layout.addWidget(clear_downloads_btn)
        
        desc_label = QLabel(translations[self.current_language]['clear_downloads_description'])
        desc_label.setStyleSheet("color: #999; font-size: 12px; padding-left: 5px;")
        desc_label.setWordWrap(True)
        clear_downloads_layout.addWidget(desc_label)
        
        downloads_layout.addWidget(clear_downloads_container)
        
        downloads_group.setLayout(downloads_layout)
        scroll_layout.addWidget(downloads_group)
        
        # Tabs section
        tabs_group = QGroupBox(translations[self.current_language]['tabs'])
        tabs_layout = QVBoxLayout()
        tabs_layout.setSpacing(12)
        tabs_layout.setContentsMargins(15, 15, 15, 15)
        
        tab_options = [
            ("ctrl_tab_recent", "Ctrl+Tab cycles through tabs in recently used order"),
            ("warn_multiple_tabs", translations[self.current_language]['warn_quit']),
            ("switch_to_new_tabs", "When you open a link in a new tab, switch to it immediately"),
            ("show_tab_previews", "Show tab previews on hover"),
            ("tab_audio_muting", "Allow tab audio muting"),
            ("tab_groups", "Enable tab groups")
        ]
        
        for key, title in tab_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 10)
            
            option = QCheckBox(title)
            option.setStyleSheet("""
                QCheckBox {
                    color: white;
                    font-size: 13px;
                    font-weight: normal;
                }
            """)
            option.setChecked(self.settings.value(key, False, type=bool))
            self.general_checkboxes[key] = option
            option_layout.addWidget(option)
            
            tabs_layout.addWidget(option_container)
        
        tabs_group.setLayout(tabs_layout)
        scroll_layout.addWidget(tabs_group)
        
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)
        
        self.stack_widget.addWidget(page)

    def setup_shortcuts_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(30)
        
        # Navigation shortcuts
        nav_group = QGroupBox(translations[self.current_language]['navigation'])
        nav_layout = QVBoxLayout()
        nav_layout.setSpacing(15)
        
        self.shortcut_inputs = {}
        shortcuts = [
            ("back", translations[self.current_language]['back'], "Alt+Left"),
            ("forward", translations[self.current_language]['forward'], "Alt+Right"),
            ("reload", translations[self.current_language]['reload'], "Ctrl+R"),
            ("home", translations[self.current_language]['home'], "Alt+Home"),
            ("close_tab", translations[self.current_language]['close_tab'], "Ctrl+W"),
            ("new_tab", translations[self.current_language]['new_tab'], "Ctrl+T"),
            ("quit", translations[self.current_language]['quit'], "Ctrl+Q")
        ]
        
        for key, title, default in shortcuts:
            row = QWidget()
            row_layout = QHBoxLayout(row)
            row_layout.setContentsMargins(0, 0, 0, 0)
            
            label = QLabel(title)
            label.setMinimumWidth(150)
            shortcut_input = QLineEdit()
            shortcut_input.setText(self.settings.value(f"shortcuts/{key}", default))
            shortcut_input.setPlaceholderText("Type shortcut")
            self.shortcut_inputs[key] = shortcut_input
            
            row_layout.addWidget(label)
            row_layout.addWidget(shortcut_input)
            row_layout.addStretch()
            nav_layout.addWidget(row)
        
        nav_group.setLayout(nav_layout)
        layout.addWidget(nav_group)
        
        layout.addStretch()
        self.stack_widget.addWidget(page)

    def setup_privacy_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(35)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
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
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(35)
        
        # Privacy settings
        privacy_group = QGroupBox(translations[self.current_language]['privacy_security'])
        privacy_layout = QVBoxLayout()
        privacy_layout.setSpacing(15)
        privacy_layout.setContentsMargins(15, 15, 15, 15)
        
        self.privacy_checkboxes = {}
        privacy_options = [
            ("accept_cookies", translations[self.current_language]['accept_cookies'], 
             translations[self.current_language]['description_accept_cookies']),
            ("do_not_track", translations[self.current_language]['do_not_track'], 
             translations[self.current_language]['description_do_not_track']),
            ("block_popups", translations[self.current_language]['block_popups'], 
             translations[self.current_language]['description_block_popups']),
            ("location_access", translations[self.current_language]['location_access'], 
             translations[self.current_language]['description_location_access']),
            ("password_autofill", translations[self.current_language]['password_autofill'], 
             translations[self.current_language]['description_password_autofill']),
            ("payment_autofill", translations[self.current_language]['payment_autofill'], 
             translations[self.current_language]['description_payment_autofill']),
            ("address_autofill", translations[self.current_language]['address_autofill'], 
             translations[self.current_language]['description_address_autofill']),
            ("safe_browsing", translations[self.current_language]['safe_browsing'], 
             translations[self.current_language]['description_safe_browsing']),
            ("always_use_https", translations[self.current_language]['always_use_https'], 
             translations[self.current_language]['description_always_use_https']),
            ("send_error_reports", translations[self.current_language]['send_error_reports'], 
             translations[self.current_language]['description_send_error_reports']),
            ("third_party_cookies", translations[self.current_language]['third_party_cookies'], 
             translations[self.current_language]['description_third_party_cookies']),
            ("fingerprinting", translations[self.current_language]['fingerprinting'], 
             translations[self.current_language]['description_fingerprinting'])
        ]
        
        for key, title, desc in privacy_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 10)
            
            option = QCheckBox(title)
            option.setStyleSheet("""
                QCheckBox {
                    color: white;
                    font-size: 13px;
                    font-weight: normal;
                }
            """)
            option.setChecked(self.settings.value(key, False, type=bool))
            
            desc_label = QLabel(desc)
            desc_label.setStyleSheet("color: #999; font-size: 12px; padding-left: 25px;")
            desc_label.setWordWrap(True)
            
            self.privacy_checkboxes[key] = option
            option_layout.addWidget(option)
            option_layout.addWidget(desc_label)
            
            privacy_layout.addWidget(option_container)
        
        privacy_group.setLayout(privacy_layout)
        scroll_layout.addWidget(privacy_group)
        
        # Security section
        security_group = QGroupBox(translations[self.current_language]['security'])
        security_layout = QVBoxLayout()
        security_layout.setSpacing(15)
        security_layout.setContentsMargins(15, 15, 15, 15)
        
        security_options = [
            ("secure_dns", translations[self.current_language]['secure_dns'], 
             translations[self.current_language]['description_secure_dns']),
            ("insecure_content", translations[self.current_language]['insecure_content'], 
             translations[self.current_language]['description_insecure_content']),
            ("certificate_warnings", translations[self.current_language]['certificate_warnings'], 
             translations[self.current_language]['description_certificate_warnings'])
        ]
        
        for key, title, desc in security_options:
            option_container = QWidget()
            option_layout = QVBoxLayout(option_container)
            option_layout.setContentsMargins(0, 0, 0, 10)
            
            option = QCheckBox(title)
            option.setStyleSheet("""
                QCheckBox {
                    color: white;
                    font-size: 13px;
                    font-weight: normal;
                }
            """)
            option.setChecked(self.settings.value(key, True, type=bool))
            
            desc_label = QLabel(desc)
            desc_label.setStyleSheet("color: #999; font-size: 12px; padding-left: 25px;")
            desc_label.setWordWrap(True)
            
            self.privacy_checkboxes[key] = option
            option_layout.addWidget(option)
            option_layout.addWidget(desc_label)
            
            security_layout.addWidget(option_container)
        
        security_group.setLayout(security_layout)
        scroll_layout.addWidget(security_group)
        
        # Clear browsing data button
        clear_data_btn = QPushButton(translations[self.current_language]['clear_data'])
        clear_data_btn.clicked.connect(self.clear_browsing_data)
        clear_data_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        scroll_layout.addWidget(clear_data_btn)
        
        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)
        
        self.stack_widget.addWidget(page)

    def show_notification(self, message, show_buttons=True):
        self.notification_container.setFixedHeight(50)
        self.notification_container.show()
        self.notification_label.setText(message)
        self.notification_buttons.setVisible(show_buttons)
        
        if not show_buttons:
            QTimer.singleShot(5000, self.hide_notification)
    
    def hide_notification(self):
        self.notification_container.setFixedHeight(0)
        self.notification_container.hide()
    
    def accept_changes(self):
        self.save_settings()
        self.show_notification("Settings saved successfully!", False)
    
    def reject_changes(self):
        self.hide_notification()
        # Reload settings
        self.load_settings()
    
    def save_settings(self):
        # Save general settings
        for key, checkbox in self.general_checkboxes.items():
            self.settings.setValue(key, checkbox.isChecked())
            
            # Save custom startup URL if enabled
            if key == "custom_startup" and checkbox.isChecked():
                self.settings.setValue("startup_url", self.startup_url.text())
        
        # Save shortcuts
        for key, input_field in self.shortcut_inputs.items():
            self.settings.setValue(f"shortcuts/{key}", input_field.text())
        
        # Save search settings
        custom_selected = self.custom_engine_radio.isChecked()
        
        if custom_selected:
            # Save custom search engine
            self.settings.setValue('default_search_engine', self.custom_engine_name.text())
            self.settings.setValue('default_search_engine_url', self.custom_engine_url.text())
        else:
            # Save default search engine
            for name, url, radio in self.search_engine_buttons:
                if radio.isChecked() and name != "custom":
                    self.settings.setValue('default_search_engine', name)
                    self.settings.setValue('default_search_engine_url', '')
                    break
        
        self.settings.setValue('show_search_suggestions', self.show_suggestions.isChecked())
        
        # Save privacy settings
        for key, checkbox in self.privacy_checkboxes.items():
            self.settings.setValue(key, checkbox.isChecked())
        
        # Save language settings
        new_language = {
            'English': 'en',
            'Türkçe': 'tr',
            'Русский': 'ru'
        }[self.language_combo.currentText()]
        
        if new_language != self.current_language:
            self.settings.setValue('language', new_language)
            self.show_notification("Language changed. Browser restart required for changes to take effect.", False)
        
        self.settings.sync()
        
        # Apply shortcuts
        if hasattr(self.window(), 'setup_shortcuts'):
            self.window().setup_shortcuts()

    def show_restart_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(translations[self.current_language]['language_restart_note'])
        msg.setWindowTitle(translations[self.current_language]['settings'])
        msg.exec_()

    def clear_browsing_data(self):
        reply = QMessageBox.question(
            self,
            translations[self.current_language]['clear_data'],
            "Are you sure you want to clear all browsing data? This cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Clear QWebEngineProfile data
            if hasattr(self.window(), 'tabs'):
                for tab_button, web_view in self.window().tabs:
                    if isinstance(web_view, QWebEngineView):
                        web_view.page().profile().clearAllVisitedLinks()
                        web_view.page().profile().clearHttpCache()
                        web_view.page().profile().cookieStore().deleteAllCookies()
            
            QMessageBox.information(self, "Success", "Browsing data cleared successfully!")

    def setup_search_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(30)
        
        # Search engine section
        search_group = QGroupBox(translations[self.current_language]['default_search'])
        search_layout = QVBoxLayout()
        search_layout.setSpacing(15)
        search_layout.setContentsMargins(15, 15, 15, 15)
        
        self.search_engine_buttons = []
        
        # Default engines
        default_engines = [
            ("Google", "https://www.google.com/search?q="),
            ("DuckDuckGo", "https://duckduckgo.com/?q="),
            ("Bing", "https://www.bing.com/search?q="),
            ("Yandex", "https://yandex.com/search/?text=")
        ]
        
        # Custom engine section
        custom_engine = QWidget()
        custom_layout = QVBoxLayout(custom_engine)
        custom_layout.setContentsMargins(0, 0, 0, 0)
        custom_layout.setSpacing(10)
        
        self.custom_engine_radio = QRadioButton(translations[self.current_language]['custom'])
        self.custom_engine_radio.setStyleSheet("""
            QRadioButton {
                color: white;
                font-size: 13px;
                font-weight: normal;
            }
        """)
        
        custom_layout.addWidget(self.custom_engine_radio)
        
        custom_input = QWidget()
        custom_input_layout = QVBoxLayout(custom_input)
        custom_input_layout.setContentsMargins(25, 0, 0, 0)
        custom_input_layout.setSpacing(10)
        
        self.custom_engine_name = QLineEdit()
        self.custom_engine_name.setPlaceholderText(translations[self.current_language]['search_engine_name'])
        self.custom_engine_url = QLineEdit()
        self.custom_engine_url.setPlaceholderText(translations[self.current_language]['search_engine_url'])
        
        for input_field in [self.custom_engine_name, self.custom_engine_url]:
            input_field.setStyleSheet("""
                QLineEdit {
                    background-color: #2B2A33;
                    border: 1px solid #3F3F44;
                    border-radius: 4px;
                    padding: 8px;
                    color: white;
                    font-size: 13px;
                }
            """)
            custom_input_layout.addWidget(input_field)
        
        custom_layout.addWidget(custom_input)
        
        # Load current settings
        current_engine = self.settings.value('default_search_engine', 'Google')
        current_engine_url = self.settings.value('default_search_engine_url', '')
        is_custom = True
        
        # Add default engines
        for name, url in default_engines:
            radio = QRadioButton(name)
            radio.setStyleSheet("""
                QRadioButton {
                    color: white;
                    font-size: 13px;
                    font-weight: normal;
                }
            """)
            if name == current_engine and not current_engine_url:
                radio.setChecked(True)
                is_custom = False
            self.search_engine_buttons.append((name, url, radio))
            search_layout.addWidget(radio)
        
        # Add custom engine section
        search_layout.addWidget(custom_engine)
        self.search_engine_buttons.append(("custom", "", self.custom_engine_radio))
        
        # If using custom engine, set the values
        if is_custom:
            self.custom_engine_radio.setChecked(True)
            self.custom_engine_name.setText(current_engine)
            self.custom_engine_url.setText(current_engine_url)
        
        # Enable/disable custom inputs based on radio selection
        def update_custom_inputs():
            enabled = self.custom_engine_radio.isChecked()
            self.custom_engine_name.setEnabled(enabled)
            self.custom_engine_url.setEnabled(enabled)
        
        self.custom_engine_radio.toggled.connect(update_custom_inputs)
        update_custom_inputs()
        
        search_group.setLayout(search_layout)
        layout.addWidget(search_group)
        
        # Search suggestions
        suggestions_group = QGroupBox(translations[self.current_language]['search_suggestions'])
        suggestions_layout = QVBoxLayout()
        suggestions_layout.setContentsMargins(15, 15, 15, 15)
        
        self.show_suggestions = QCheckBox(translations[self.current_language]['show_search_suggestions'])
        self.show_suggestions.setStyleSheet("""
            QCheckBox {
                color: white;
                font-size: 13px;
                font-weight: normal;
            }
        """)
        self.show_suggestions.setChecked(self.settings.value('show_search_suggestions', True, type=bool))
        
        suggestions_layout.addWidget(self.show_suggestions)
        suggestions_group.setLayout(suggestions_layout)
        layout.addWidget(suggestions_group)
        
        layout.addStretch()
        self.stack_widget.addWidget(page)

    def setup_language_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(20)
        
        # Language settings
        language_group = QGroupBox(translations[self.current_language]['language_settings'])
        language_layout = QVBoxLayout()
        
        self.language_combo = QComboBox()
        self.language_combo.addItems(['English', 'Türkçe', 'Русский'])
        self.language_combo.setCurrentText({
            'en': 'English',
            'tr': 'Türkçe',
            'ru': 'Русский'
        }[self.current_language])
        
        language_layout.addWidget(QLabel(translations[self.current_language]['preferred_language']))
        language_layout.addWidget(self.language_combo)
        
        note_label = QLabel(translations[self.current_language]['language_restart_note'])
        note_label.setStyleSheet("color: #999; font-style: italic; margin-top: 20px;")
        note_label.setWordWrap(True)
        language_layout.addWidget(note_label)
        
        language_group.setLayout(language_layout)
        layout.addWidget(language_group)
        
        layout.addStretch()
        self.stack_widget.addWidget(page)

    def load_settings(self):
        # Load general settings
        for key in self.general_checkboxes:
            self.general_checkboxes[key].setChecked(
                self.settings.value(key, False, type=bool)
            )
        
        # Load shortcuts
        for key in self.shortcut_inputs:
            default = {
                'back': 'Alt+Left',
                'forward': 'Alt+Right',
                'reload': 'Ctrl+R',
                'home': 'Alt+Home',
                'close_tab': 'Ctrl+W',
                'new_tab': 'Ctrl+T',
                'quit': 'Ctrl+Q'
            }.get(key, '')
            self.shortcut_inputs[key].setText(
                self.settings.value(f"shortcuts/{key}", default)
            )
        
        # Load search settings
        default_engine = self.settings.value('default_search_engine', 'Google')
        for engine, radio in self.search_engine_buttons:
            radio.setChecked(engine == default_engine)
        
        if hasattr(self, 'show_suggestions'):
            self.show_suggestions.setChecked(
                self.settings.value('show_search_suggestions', True, type=bool)
            )
        
        # Load privacy settings
        for key in self.privacy_checkboxes:
            self.privacy_checkboxes[key].setChecked(
                self.settings.value(key, False, type=bool)
            )
        
        # Load language settings
        if hasattr(self, 'language_combo'):
            current_lang = {
                'en': 'English',
                'tr': 'Türkçe',
                'ru': 'Русский'
            }[self.settings.value('language', 'en')]
            self.language_combo.setCurrentText(current_lang)

    def setup_about_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(30)
        
        # About section
        about_group = QGroupBox(translations[self.current_language]['about'])
        about_layout = QVBoxLayout()
        about_layout.setSpacing(15)
        about_layout.setContentsMargins(15, 15, 15, 15)
        
        # Logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("res/logo.png")
        if not logo_pixmap.isNull():
            logo_label.setPixmap(logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)
        about_layout.addWidget(logo_label)
        
        # Version
        version_label = QLabel(f"{translations[self.current_language]['version']}: Solar Browser Python Edition, version code: sdpyqt0.0.0.2-bt")
        version_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        version_label.setAlignment(Qt.AlignCenter)
        about_layout.addWidget(version_label)
        
        # Developers
        dev_label = QLabel(f"{translations[self.current_language]['developers']}:")
        dev_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
                font-weight: bold;
                padding-top: 20px;
            }
        """)
        about_layout.addWidget(dev_label)
        
        developers = [
            "Developed by Ata TÜRKÇÜ",
            "Special thanks to Mustafa ÇAKI"
        ]
        
        for dev in developers:
            dev_name = QLabel(dev)
            dev_name.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 13px;
                    padding-left: 20px;
                }
            """)
            about_layout.addWidget(dev_name)
        
        # License
        license_label = QLabel(f"{translations[self.current_language]['license']}: GPL-3.0")
        license_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
                padding-top: 20px;
            }
        """)
        about_layout.addWidget(license_label)
        
        # Website with GitHub button
        website_container = QWidget()
        website_layout = QHBoxLayout(website_container)
        website_layout.setContentsMargins(0, 20, 0, 0)
        website_layout.setSpacing(10)
        
        website_label = QLabel(f"{translations[self.current_language]['website']}:")
        website_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
            }
        """)
        website_layout.addWidget(website_label)
        
        github_btn = QPushButton()
        github_btn.setIcon(QIcon("res/github.png"))
        github_btn.setText("GitHub")
        github_btn.setCursor(Qt.PointingHandCursor)
        github_btn.setStyleSheet("""
            QPushButton {
                background-color: #2B2A33;
                color: white;
                border: 1px solid #3F3F44;
                border-radius: 4px;
                padding: 8px 16px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #52525E;
            }
        """)
        github_btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl('https://github.com/Solar-Browser/desktop')))
        website_layout.addWidget(github_btn)
        
        website_layout.addStretch()
        about_layout.addWidget(website_container)
        
        about_group.setLayout(about_layout)
        layout.addWidget(about_group)
        
        layout.addStretch()
        self.stack_widget.addWidget(page)

    def clear_downloads_history(self):
        reply = QMessageBox.question(
            self,
            translations[self.current_language]['clear_downloads'],
            translations[self.current_language]['clear_downloads_description'],
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Clear downloads history
            if hasattr(self.window(), 'downloads_page'):
                self.window().downloads_page.clear_all_downloads()
            QMessageBox.information(self, "Success", "Downloads history cleared successfully!")
    
    def change_download_location(self):
        new_location = QFileDialog.getExistingDirectory(
            self,
            translations[self.current_language]['download_location'],
            QStandardPaths.writableLocation(QStandardPaths.DownloadLocation),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        
        if new_location:
            self.settings.setValue('download_location', new_location)
            current_location_label = self.findChild(QLabel, 'current_location_label')
            if current_location_label:
                current_location_label.setText(f"{translations[self.current_language]['current_location']} {new_location}")

class TabButton(QPushButton):
    def __init__(self, title, favicon, close_callback, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.minimum_width = 40 
        self.preferred_width = 200  
        self.setFixedHeight(30)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid white;
                border-radius: 8px;
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
        self.favicon.setStyleSheet("""
            QLabel{
                background-color: white;
                border: none;
            }
        """)
        self.main_layout.addWidget(self.favicon)

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("""
            QLabel{
                font-size: 11px;
                background-color: white;
                border: none;
        }
        """)
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
                border-radius: 8px;
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
        self.settings = QSettings('Solar', 'Browser')
        self.current_language = self.settings.value('language', 'en')
        self.tabs = []
        self.current_tab = None
        self.downloads_page = None

        self.show_warning()
        self.setup_shortcuts()
        
        # Setup download handling
        profile = QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.handle_download)
    
    def handle_download(self, download_item):
        # Show downloads page if enabled
        if self.settings.value('show_downloads_when_start', False, type=bool):
            self.show_downloads()
        
        # Set download path
        if self.settings.value('ask_download_location', False, type=bool):
            suggested_path = os.path.join(
                self.settings.value('download_location', 
                QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)),
                download_item.suggestedFileName()
            )
            path, _ = QFileDialog.getSaveFileName(
                self,
                translations[self.current_language]['download_location'],
                suggested_path
            )
            if path:
                download_item.setPath(path)
            else:
                download_item.cancel()
                return
        else:
            download_dir = self.settings.value('download_location', 
                QStandardPaths.writableLocation(QStandardPaths.DownloadLocation))
            download_item.setPath(os.path.join(download_dir, download_item.suggestedFileName()))
        
        # Add to downloads page
        if not self.downloads_page:
            self.show_downloads()
        self.downloads_page.add_download(download_item)
        
        # Handle auto-open setting
        if self.settings.value('auto_open_downloads', False, type=bool):
            download_item.finished.connect(lambda: self.auto_open_download(download_item))
        
        download_item.accept()
    
    def auto_open_download(self, download_item):
        if download_item.state() == QWebEngineDownloadItem.DownloadCompleted:
            QDesktopServices.openUrl(QUrl.fromLocalFile(download_item.path()))
    
    def show_downloads(self):
        if not self.downloads_page:
            self.downloads_page = DownloadsPage()
            
            if hasattr(self, 'new_tab_btn'):
                self.tab_layout.removeWidget(self.new_tab_btn)
                self.new_tab_btn.setParent(None)
            
            current_index = len(self.tabs)
            tab_button = TabButton(translations[self.current_language]['downloads'], None, lambda: self.close_tab(current_index))
            tab_button.clicked.connect(lambda: self.switch_to_tab(current_index))
            self.tab_layout.addWidget(tab_button)
            
            self.downloads_page.hide()
            self.web_layout.addWidget(self.downloads_page)
            self.tabs.append((tab_button, self.downloads_page))
            
            if not hasattr(self, 'new_tab_btn'):
                self.new_tab_btn = QPushButton("+")
                self.new_tab_btn.setFixedSize(25, 25)
                self.new_tab_btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: 1px solid #ccc;
                        border-radius: 8px;
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

    def setup_shortcuts(self):
        # Create shortcuts
        shortcuts = {
            'back': (self.go_back, "Alt+Left"),
            'forward': (self.go_forward, "Alt+Right"),
            'reload': (self.reload_page, "Ctrl+R"),
            'home': (lambda: self.navigate_to_url("https://www.google.com"), "Alt+Home"),
            'close_tab': (lambda: self.close_tab(self.current_tab) if self.current_tab is not None else None, "Ctrl+W"),
            'new_tab': (self.add_new_tab, "Ctrl+T"),
            'quit': (self.close, "Ctrl+Q")
        }
        
        # Clear existing shortcuts
        if hasattr(self, '_shortcuts'):
            for shortcut in self._shortcuts:
                shortcut.setEnabled(False)
                shortcut.deleteLater()
        
        self._shortcuts = []
        
        # Create new shortcuts
        for key, (callback, default) in shortcuts.items():
            shortcut = QShortcut(QKeySequence(self.settings.value(f"shortcuts/{key}", default)), self)
            shortcut.activated.connect(callback)
            self._shortcuts.append(shortcut)

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
        self.top_bar = QWidget()
        self.top_bar.setFixedHeight(40)
        self.top_bar.setStyleSheet("background-color: #f0f0f0;")
        top_layout = QHBoxLayout(self.top_bar)
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
        window_layout.setSpacing(2)

        min_btn = QPushButton("−")
        max_btn = QPushButton("▢")
        close_btn = QPushButton("×")
        
        for btn in [min_btn, max_btn, close_btn]:
            btn.setFixedSize(25, 25)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    font-size: 11px;
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
        parent_layout.addWidget(self.top_bar)

    def setup_navigation_bar(self, parent_layout):
        self.nav_panel = QWidget()
        self.nav_panel.setFixedHeight(35)
        nav_layout = QHBoxLayout(self.nav_panel)
        nav_layout.setContentsMargins(5,0,5,0)
        self.nav_panel.setStyleSheet("background-color: white")

        nav_buttons = [
            ("res/back_white.png", self.go_back),
            ("res/forward_white.png", self.go_forward),
            ("res/reload_white.png", self.reload_page)
        ]

        for icon_path, callback in nav_buttons:
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(16, 16))
            btn.setFixedSize(25, 25)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border: 1px solid #ccc;
                    border-radius: 8px;
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
        
        # Warning icon and tooltip
        warn_container = QWidget()
        warn_container.setFixedSize(30, 30)
        warn_btn = QPushButton(warn_container)
        warn_btn.setIcon(QIcon("res/warn.png"))
        warn_btn.setIconSize(QSize(16, 16))
        warn_btn.setFixedSize(25, 25)
        warn_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        
        # Warning tooltip
        self.warning_tooltip = QWidget(self)
        self.warning_tooltip.setStyleSheet("""
            QWidget {
                background-color: #2B2A33;
                border: 1px solid #3F3F44;
                border-radius: 8px;
            }
            QLabel {
                color: white;
                padding: 10px;
            }
        """)
        tooltip_layout = QVBoxLayout(self.warning_tooltip)
        tooltip_layout.setContentsMargins(0, 0, 0, 0)
        
        warning_text = QLabel("Do not enter your bank account or something important in this browser. If you enter, this will be in your responsibility!")
        warning_text.setWordWrap(True)
        warning_text.setFixedWidth(300)
        tooltip_layout.addWidget(warning_text)
        
        self.warning_tooltip.hide()
        
        warn_btn.enterEvent = lambda e: self.show_warning_tooltip()
        warn_btn.leaveEvent = lambda e: self.hide_warning_tooltip()
        
        center_layout.addWidget(warn_container)

        self.url_bar = QLineEdit()
        self.url_bar.setFixedWidth(600)
        self.url_bar.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 4px;
                background: white;
            }
        """)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        center_layout.addWidget(self.url_bar)
        
        nav_layout.addWidget(center_container, alignment=Qt.AlignCenter)
        
        settings_btn = QPushButton()
        settings_btn.setIcon(QIcon("res/settings_white.png"))
        settings_btn.setIconSize(QSize(16, 16))
        settings_btn.setFixedSize(25, 25)
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        settings_btn.clicked.connect(self.show_settings)
        nav_layout.addWidget(settings_btn)

        parent_layout.addWidget(self.nav_panel)

    def show_warning_tooltip(self):
        if hasattr(self, 'warning_tooltip'):
            pos = self.nav_panel.mapToGlobal(QPoint(0, self.nav_panel.height()))
            self.warning_tooltip.move(pos.x() + 10, pos.y() + 5)
            self.warning_tooltip.show()

    def hide_warning_tooltip(self):
        if hasattr(self, 'warning_tooltip'):
            self.warning_tooltip.hide()

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
                    border-radius: 8px;
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
        tab_button = TabButton(translations[self.current_language]['settings'] if current_index == 0 else "New Tab", None, lambda: self.close_tab(current_index))
        tab_button.clicked.connect(lambda: self.switch_to_tab(current_index))
        self.tab_layout.addWidget(tab_button)
        
        web_view = QWebEngineView()
        web_view.settings().setAttribute(web_view.settings().FullScreenSupportEnabled, True)
        web_view.settings().setAttribute(web_view.settings().PlaybackRequiresUserGesture, False)
        web_view.page().fullScreenRequested.connect(self.handle_fullscreen_request)
        
        # Use custom startup page if configured
        if self.settings.value('custom_startup', False, type=bool):
            startup_url = self.settings.value('startup_url', 'https://www.google.com')
        else:
            startup_url = 'https://www.google.com'
            
        web_view.setUrl(QUrl(startup_url))
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
                    border-radius: 8px;
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
        short_title = title[:20] + "..." if len(title) > 20 else title
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
                    background-color: white;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 2px 5px;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: white;
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
                border-radius: 8px;
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
        
        # Update close button callbacks
        for i, (tab_btn, _) in enumerate(self.tabs):
            tab_btn.close_btn.clicked.disconnect()
            tab_btn.close_btn.clicked.connect(lambda idx=i: self.close_tab(idx))
            # Update click handlers
            tab_btn.clicked.disconnect()
            tab_btn.clicked.connect(lambda checked, idx=i: self.switch_to_tab(idx))
        
        if self.current_tab == from_idx:
            self.current_tab = to_idx
        elif from_idx < self.current_tab <= to_idx:
            self.current_tab -= 1
        elif to_idx <= self.current_tab < from_idx:
            self.current_tab += 1
            
        self.update_tab_layout()
        self.switch_to_tab(self.current_tab)

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
                    # Get the current search engine settings
                    engine = self.settings.value('default_search_engine', 'Google')
                    engine_url = self.settings.value('default_search_engine_url', '')
                    
                    # Use custom search engine if configured
                    if engine_url:
                        search_url = engine_url.replace('%s', QUrl.toPercentEncoding(url).data().decode())
                    else:
                        # Use default search engines
                        search_urls = {
                            'Google': 'https://www.google.com/search?q=',
                            'DuckDuckGo': 'https://duckduckgo.com/?q=',
                            'Bing': 'https://www.bing.com/search?q=',
                            'Yandex': 'https://yandex.com/search/?text='
                        }
                        search_url = search_urls.get(engine, search_urls['Google']) + QUrl.toPercentEncoding(url).data().decode()
                    
                    url = search_url
                
                current_widget.setUrl(QUrl(url))

    def handle_fullscreen_request(self, request):
        request.accept()
        if request.toggleOn():
            self.showFullScreen()
            # Hide UI elements
            if hasattr(self, 'top_bar'):
                self.top_bar.hide()
            if hasattr(self, 'nav_panel'):
                self.nav_panel.hide()
        else:
            self.showNormal()
            # Show UI elements
            if hasattr(self, 'top_bar'):
                self.top_bar.show()
            if hasattr(self, 'nav_panel'):
                self.nav_panel.show()

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
        progress = (bytes_received * 100) / bytes_total
        self.progress_bar.setValue(int(progress))
        
        # Update status with file size
        received_size = self.format_size(bytes_received)
        total_size = self.format_size(bytes_total)
        self.status_label.setText(f"{received_size} of {total_size}")
    
    def update_state(self, state):
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
    
    def format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
    
    def open_containing_folder(self):
        path = self.download_item.path()
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.dirname(path)))
    
    def cancel_download(self):
        if self.download_item.state() == QWebEngineDownloadItem.DownloadInProgress:
            self.download_item.cancel()
        else:
            # Remove from list if completed
            self.parent().remove_download(self)

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
        
        clear_all_btn = QPushButton("Clear All")
        clear_all_btn.setStyleSheet("""
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
        """)
        clear_all_btn.clicked.connect(self.clear_all_downloads)
        header_layout.addWidget(clear_all_btn, alignment=Qt.AlignRight)
        
        layout.addWidget(header)
        
        # Downloads list
        self.downloads_container = QWidget()
        self.downloads_layout = QVBoxLayout(self.downloads_container)
        self.downloads_layout.setContentsMargins(0, 0, 0, 0)
        self.downloads_layout.setSpacing(10)
        self.downloads_layout.addStretch()
        
        # Scroll area for downloads
        scroll = QScrollArea()
        scroll.setWidget(self.downloads_container)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
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
        layout.addWidget(scroll)
    
    def add_download(self, download_item):
        # Remove stretch
        self.downloads_layout.takeAt(self.downloads_layout.count() - 1)
        
        # Add new download widget
        download_widget = DownloadWidget(download_item, self)
        self.downloads_layout.addWidget(download_widget)
        
        # Add stretch back
        self.downloads_layout.addStretch()
    
    def remove_download(self, download_widget):
        self.downloads_layout.removeWidget(download_widget)
        download_widget.deleteLater()
    
    def clear_all_downloads(self):
        while self.downloads_layout.count() > 1:  # Keep the stretch
            item = self.downloads_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
    