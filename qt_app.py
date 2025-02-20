from util import *
import contextlib, time, sys
import gpt4all
from PySide6 import QtWidgets, QtGui, QtCore
from ui.main_ui import Ui_MainWindow as UiMainWindow
from ui.selection_ui import Ui_Dialog as UiSelection

class StreamThread(QtCore.QThread): # CONSOLE THREAD
    append = QtCore.Signal(str)
    move_scrollbar = QtCore.Signal()
    def __init__(self, other:UiMainWindow, entry:str, item:QtWidgets.QListWidgetItem) -> None:
        super(StreamThread, self).__init__()
        self.thread_lock : QtCore.QMutex = QtCore.QMutex()
        self.arg_other : MainWindow = other
        self.entry : str = entry
        self.item : QtWidgets.QListWidgetItem = item

    def run(self) -> None:
        answer : str = self.arg_other.choosed_character['name'] + ' : '
        for token_index, token in enumerate(self.arg_other.llm.generate(self.entry, 200, 0.35, 40, 0.40, 1.25, 100, 12, streaming=True)):
            if token_index == 0:
                token = token.lstrip('\n')
            answer = answer + token
            self.item.setText(answer)
        self.arg_other.line_edit.setEnabled(True)
        self.arg_other.button_send.setEnabled(True)
        self.arg_other.running_response = False
        self.arg_other = None

    def lock(self) -> None:
        self.thread_lock.lock()

    def unlock(self) -> None:
        self.thread_lock.unlock()

class MainWindow(QtWidgets.QMainWindow, UiMainWindow): # MAIN WINDOW
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent=parent)
        
        QtGui.QFontDatabase.addApplicationFont(os.path.join(asset_directory, 'noto_sans_condensed_light.ttf'))
        self.character_data : Tuple[List[CharacterCard], List[ModelCard]] = get_character_data()

        self.running_response : bool = False
        self.llm : Optional[gpt4all.GPT4All] = None
        self.choosed_character : Optional[CharacterCard] = None
        self.choosed_model : Optional[ModelCard] = None
        self.chat_session : Optional[contextlib._GeneratorContextManager[gpt4all.GPT4All]] = None
        self.process_stream : Optional[StreamThread] = None

        self.setupUi(self)

        image : QtGui.QPixmap = QtGui.QPixmap(QtGui.QPixmap(os.path.join(asset_directory, 'dark_tiles.png')))
        self.label_image.setPixmap(image.scaled(256, 256))
        self.label_character.setText('-')

        self.button_send.clicked.connect(self.send_chat)
        self.line_edit.returnPressed.connect(self.send_chat)

        self.action_selection.triggered.connect(self.show_selection)
        self.action_clear.triggered.connect(self.exit_chat)
        self.action_exit.triggered.connect(self.close)

    def show_selection(self) -> None:
        window : QtWidgets.QDialog = QtWidgets.QDialog()
        dialog : UiSelection = UiSelection()
        dialog.setupUi(window)
        self.character_data = get_character_data()
        for i, char in enumerate(self.character_data[0]):
            dialog.combo_character.addItem(char['name'], i)
        for i, model in enumerate(self.character_data[1]):
            dialog.combo_model.addItem(model['name'], i)
        dialog.combo_character.currentTextChanged.connect(lambda _: self.character_selected(dialog))
        dialog.button_box.accepted.connect(lambda: self.enter_chat(dialog, window))
        window.exec()

    def character_selected(self, dialog:UiSelection) -> None:
        ui_selected_character : str = dialog.combo_character.currentText()
        if not ui_selected_character:
            return
        selected_char : CharacterCard = self.character_data[0][dialog.combo_character.itemData(dialog.combo_character.currentIndex())]
        description : str = 'Gender: %s\nLanguage: %s\nOrigin: %s\nAuthor: %s\n\n%s' % (
            selected_char['gender'],
            selected_char['language'],
            selected_char['origin'],
            selected_char['author'],
            selected_char['description']
        )
        dialog.text_description.setText(description)
        image : QtGui.QPixmap = QtGui.QPixmap(os.path.join(selected_char['path'], selected_char['image']))
        dialog.label_image.setPixmap(image.scaled(64, 64))

    def enter_chat(self, dialog:UiSelection, window:QtWidgets.QDialog) -> None:
        ui_selected_character : str = dialog.combo_character.currentText()
        ui_selected_model : str = dialog.combo_model.currentText()
        if not ui_selected_character:
            return
        if not ui_selected_model:
            return
        self.label_character.setText('Loading..')
        self.line_edit.clear()
        self.list_chat.clear()
        if self.process_stream:
            self.process_stream.terminate()
        self.process_stream = None
        window.close()
        self.choosed_model = self.character_data[1][dialog.combo_model.itemData(dialog.combo_model.currentIndex())]
        self.choosed_character = self.character_data[0][dialog.combo_character.itemData(dialog.combo_character.currentIndex())]
        self.llm = gpt4all.GPT4All(self.choosed_model['file'], model_directory, None, False, device='gpu')
        self.chat_session = self.llm.chat_session(self.choosed_character['system_template'], self.choosed_character['prompt_template'])
        self.chat_session.__enter__()
        image : QtGui.QPixmap = QtGui.QPixmap(os.path.join(self.choosed_character['path'], self.choosed_character['image']))
        self.label_image.setPixmap(image.scaled(256, 256))
        self.label_character.setText(self.choosed_character['name'])

    def send_chat(self) -> None:
        if not self.llm:
            return
        if self.running_response:
            return
        if not self.line_edit.text().strip():
            return
        self.running_response = True
        entry : str = self.line_edit.text().strip()
        self.line_edit.setText('')
        self.line_edit.setEnabled(False)
        self.button_send.setEnabled(False)
        self.list_chat.addItem(QtWidgets.QListWidgetItem(QtGui.QIcon(os.path.join(asset_directory, 'light_tiles.png')), 'You : ' + entry))
        response_item : QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem(QtGui.QIcon(os.path.join(self.choosed_character['path'], self.choosed_character['image'])), self.choosed_character['name'] + ' : ...')
        self.list_chat.addItem(response_item)
        self.process_stream = StreamThread(self, entry, response_item)
        self.process_stream.start()

    def exit_chat(self) -> None:
        self.line_edit.setEnabled(True)
        self.line_edit.clear()
        self.list_chat.clear()
        if self.process_stream:
            self.process_stream.terminate()
        self.process_stream = None
        self.button_send.setEnabled(True)
        self.chat_session.__exit__(None, None, None)
        self.chat_session = None
        self.llm = None
        self.choosed_character = None
        self.choosed_model = None
        image : QtGui.QPixmap = QtGui.QPixmap(QtGui.QPixmap(os.path.join(asset_directory, 'dark_tiles.png')))
        self.label_image.setPixmap(image.scaled(256, 256))
        self.label_character.setText('-')

if __name__ == '__main__':
    print(app_name, app_version)
    print('Copyright 2024 Vladimir Alexandre Pakhomov. All rights reserved.')
    font_size : int = 16
    font_file : str = os.path.join(current_directory, 'font_size.txt')
    if os.path.isfile(font_file):
        font_size = int(open(font_file, 'r').read().strip())
    app : QtWidgets.QApplication = QtWidgets.QApplication([])
    app.setWindowIcon(QtGui.QIcon(os.path.join(asset_directory, 'icon.svg')))
    app.setStyleSheet('* { font-family: \'Noto Sans\'; font-size: %spx; }' % font_size)
    main_window : MainWindow = MainWindow()
    main_window.show()
    sys.exit(app.exec())
