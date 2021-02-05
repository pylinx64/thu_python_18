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
		
		# создает браузер
		self.browser = QWebEngineView()
		# переходит на сайт по умолчанию
		self.browser.setUrl(QUrl("http://duckduckgo.come"))
		#коннект
		self.browser.urlChanged.connect(self.update_urlbar)
		self.browser.loadFinished.connect(self.update_title)
		self.setCentralWidget(self.browser)
		
		#статус
		self.status = QStatusBar()
		self.setStatusBar(self.status)
		
		#тулбар
		navtb = QTool("Navigation")
		navtb.setIconSize(Qsize(16,16))
		self.addToolBar(navtb)
		
		#кнопка назад
		back_btn = QAction(QIcon(os.path.join('images', '313-arrow-left.png')), "Back", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(self.browser.back)
		navtb.addAction(back_btn)

		#кнопка вперёд
		forward_btn = QAction(QIcon(os.path.join('images', '309-arrow-right.png')), "forward", self)
		forward_btn.setStatusTip("forward to previous page")
		forward_btn.triggered.connect(self.browser.forward)
		navtb.addAction(forward_btn)
		
		#кнопка перезагрузить
		reload_btn = QAction(QIcon(os.path.join('images', '133-spinner11.png7')), "reload", self)
		reload_btn.setStatusTip("reload")
		reload_btn.triggered.connect(self.browser.reload)
		navtb.addAction(reload_btn)
		
		#кнопка DOmoi
		home_btn = QAction(QIcon(os.path.join('images', '002-home2.png')), "home", self)
		home_btn.setStatusTip("go to home page")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)
		
		#Сепаратор
		navtb.addSeparator()
		
		#SSL ключ
		self.httpsicon = QLabel()
		self.httpsicon.setPixmap(QPixmap(os.path.join(images.join('images', '181-shield.png'))))
		navtb.addWidget(self.httpsicon)
		
		def add_new_tab(self, qurl=None, label="Blank"):
			'''Добавляет новую вкладку'''
			
			# проверяет пустую ссылку
			if qurl is None:
				qurl = QUrl('')
	
			# запускает браузер
			browser = QWebEngineView()
			# подставляет ссылку
			browser.setUrl(qurl)
			# добавляем новую вкладку
			i = self.tabs.addTab(browser, label)
	
			self.tabs.setCurrentIndex(i)
			
			# обновляет страничку браузера
			browser.urlChanged.connect(lambda qurl, browser=browser:
									   self.update_urlbar(qurl, browser))
			# заголовок окна вкладки при загрузке
			browser.loadFinished.connect(lambda _, i=i, browser=browser:
										 self.tabs.setTabText(i, browser.page().title()))
		
		def tab_open_doubleclick(self, i):
			if i == -1:  # добавляем вкладку в конец списка
				self.add_new_tab()
				
		def current_tab_changed(self, i):
			qurl = self.tabs.currentWidget().url()
			self.update_urlbar(qurl, self.tabs.currentWidget())
			self.update_title(self.tabs.currentWidget())
			
		
			
			

		
 		
app = QApplication(sys.argv)	
app.setApplicationName("Dino Browser")
 		
window = MainWindow()
app.exec_()
		
		
