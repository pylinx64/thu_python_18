# библиотеки для GUI-приложения
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

# библиотека для работы с системой
import os
import sys

# создаем "главное окно"

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		
		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)
		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
		self.tabs.currentChanged.connect(self.current_tab_changed)
		self.tabs.setTabsClosable(True)
	
		
		self.qp = QPalette()
		self.qp.setColor(QPalette.Window, Qt.white)
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		self.setCentralWidget(self.tabs)
		
		
		#статус
		self.status = QStatusBar()
		self.setStatusBar(self.status)

		#тулбар
		navtb = QToolBar("Navigation")
		navtb.setIconSize(QSize(16, 16))
		self.addToolBar(navtb)

		#кнопка назад
		back_btn = QAction(QIcon(os.path.join('images', '313-arrow-left.png')), "Back", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		navtb.addAction(back_btn)

		#кнопка вперёд
		forward_btn = QAction(QIcon(os.path.join('images', '309-arrow-right.png')), "forward", self)
		forward_btn.setStatusTip("forward to previous page")
		forward_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		navtb.addAction(forward_btn)

		#кнопка перезагрузить
		reload_btn = QAction(QIcon(os.path.join('images', '133-spinner11.png7')), "reload", self)
		reload_btn.setStatusTip("reload")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		navtb.addAction(reload_btn)

		#кнопка Domoi
		home_btn = QAction(QIcon(os.path.join('images', '002-home2.png')), "home", self)
		home_btn.setStatusTip("go to home page")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		#Сепаратор
		navtb.addSeparator()

		#SSL ключ
		self.httpsicon = QLabel()
		self.httpsicon.setPixmap(QPixmap(os.path.join('images', '181-shield.png')))
		navtb.addWidget(self.httpsicon)
		#проверяю пустую ссылку
	def add_new_tab(self, qurl=None, label="Blank"):
		if qurl is None:
			qurl = QUrl('')
		#запускает браузер
		browser = QWebEnigeView()
		#подставляет ссылку
		browser.setUrl(qurl)
		#добавляет новую вкладку
		i = self.tabs.addTab(browser, label)
		
		self.tabs.setCurrentIndex(i)
		#обновляет страничку браузера
		browser.urlChanged.connect(lambda qurl, browser=browser:
															self.update_urlbar(qurl, browser))
		#заголовок окна вкладки при загрузке
		browser.loadFinished.connect(lambda _, i=i, browser=browser:
																self.tabs.setTabText(i, browser.page().title()))

	def tab_open_doubleclick(self, i):
		if i == -1: #добавляем вкладку в конец списка
			self.add_new_tab()
	
	def current_tab_changed(self, i):
		qurl = self.tabs.currentWidget().url()
		self.update_urlbar(qurl, self.tabs.currentWidget())
		self.update_title(self.tabs.currentWidget())
		#закрытие вкладки
	def close_current_tab(self, i):
		if self.tabs.count() < 2:
			retrun
		
		self .tabs.removeTab(i)
	
	def update_title(self, browser):
		if browser != self.tabs.currentWidget():
			return
			
		title = self.tabs.currentWidget().page().title()
		self.seWindowTitle("%s - DinoBrowser" % title)
		
	def navigate_home(self):
		self.tabs.currentWidget().setUrl(QUrl ("http://www.google.com"))
	
	def navigate_to_url(self):
		q = QUrl(self.urlbar.text())
		if q.scheme() == "":
			q.setScheme("http")
			
		self.tabs.currentWidget().setUrl(q)
		
	def update_urlbar(self, q, browser=None):
		if browser != self.tabs.currentWidget():
			return
		if q.scheme() == 'https':
			self.https.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))
		else:
			self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-noss1.png')))
		
		self.urlbar.setText(q.toString())
		self.urlbar.setCursorPosition(0)
	
	

app = QApplication(sys.argv)
app.setApplicationName("dino browser")
window = MainWindow()
app.setPalette(window.qp)

app.exec_()
