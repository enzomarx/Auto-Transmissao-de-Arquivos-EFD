import subprocess
import sys
import pyautogui
import pyperclip
import time
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QLineEdit, QFileDialog,
    QTextEdit, QMessageBox, QSlider, QProgressBar
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QCoreApplication, QProcess
from PyQt5.QtGui import QIcon, QFont

# Def var
arquivos_pulados = []

def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

required_packages = ['pyautogui', 'pyperclip', 'PyQt5']
for package in required_packages:
    check_and_install(package)

# init aplicativo EFD
def inicio(multiplier):
    pyautogui.press('win')
    time.sleep(1 * multiplier)
    pyautogui.press('e')
    time.sleep(0.20 * multiplier)
    pyautogui.press('f')
    time.sleep(0.20 * multiplier)
    pyautogui.press('d')
    time.sleep(0.20 * multiplier)
    pyautogui.press('space')
    time.sleep(0.20 * multiplier)
    pyautogui.press('c')
    time.sleep(0.20 * multiplier)
    pyautogui.press('o')
    time.sleep(0.20 * multiplier)
    pyautogui.press('n')
    time.sleep(0.20 * multiplier)
    pyautogui.press('t')
    time.sleep(0.20 * multiplier)
    pyautogui.press('r')
    time.sleep(0.20 * multiplier)
    pyautogui.press('i')
    time.sleep(0.20 * multiplier)
    pyautogui.press('b')
    time.sleep(0.20 * multiplier)
    pyautogui.press('u')
    time.sleep(0.20 * multiplier)
    pyautogui.press('i')
    time.sleep(0.20 * multiplier)
    pyautogui.press('enter')
    time.sleep(50 * multiplier)
    pyautogui.click(x=688, y=74)  # Clique na janela
    time.sleep(0.25 * multiplier)
    pyautogui.hotkey('win', 'up')
    time.sleep(1.25 * multiplier)

# Função para definir o diretório
def diretorio(multiplier):
    pyautogui.click(x=43, y=60)
    time.sleep(2.5 * multiplier)
    pyautogui.click(x=496, y=216)
    time.sleep(2.5 * multiplier)
    pyautogui.click(x=936, y=517)
    time.sleep(2 * multiplier)
    pyautogui.click(x=971, y=158)
    time.sleep(1 * multiplier)

# Função para capturar o índice do arquivo selecionado
def get_selected_index():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    selected_text = pyperclip.paste()
    return selected_text

class AutomationThread(QThread):
    log_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    pause_signal = pyqtSignal(bool)

    def __init__(self, num_loops, multiplier, log_file_path):
        super().__init__()
        self.num_loops = num_loops
        self.multiplier = multiplier
        self.log_file_path = log_file_path
        self.log = []
        self.is_paused = False

    def run(self):
        global arquivos_pulados

        down_press_count = 0

        for linha in range(self.num_loops):
            self.progress_signal.emit(linha + 1)
            if self.is_paused:
                while self.is_paused:
                    time.sleep(0.1)

            start_time = time.time()
            pyautogui.click(x=45, y=62)
            time.sleep(2 * self.multiplier)
            pyautogui.click(591, 216)
            time.sleep(2 * self.multiplier)

            index_before = get_selected_index()

            for _ in range(down_press_count):
                pyautogui.press('down')
                time.sleep(1 * self.multiplier)

            index_after = get_selected_index()

            if index_before == index_after:
                arquivos_pulados.append(linha + 1)
                log_entry = f"Arquivo {linha + 1} pulado."
            else:
                log_entry = f"Arquivo {linha + 1} processado: {index_after}"

            self.log.append(log_entry)
            self.log_signal.emit(log_entry)

            down_press_count += 1
            time.sleep(3 * self.multiplier)
            pyautogui.click(x=935, y=519)
            time.sleep(3 * self.multiplier)
            #pyautogui.click(x=689, y=394)
            #time.sleep(3 * self.multiplier)
            pyautogui.click(x=627, y=399)
            time.sleep(3 * self.multiplier)
            pyautogui.click(x=627, y=399)
            time.sleep(3.4 * self.multiplier)
            pyautogui.click(x=681, y=387)
            time.sleep(3.4 * self.multiplier)
            pyautogui.click(x=681, y=387)
            time.sleep(2.8 * self.multiplier)
            pyautogui.click(x=228, y=59)
            time.sleep(2.8 * self.multiplier)

            end_time = time.time()
            loop_time = end_time - start_time
            loop_log = f"Loop {linha + 1}: Tempo gasto = {loop_time} seconds"
            self.log.append(loop_log)
            self.log_signal.emit(loop_log)

        with open(self.log_file_path, 'w') as file:
            for entry in self.log:
                file.write(entry + '\n')

        print("Arquivos pulados:", arquivos_pulados)

        self.sign_documents()
        self.import_documents()
        self.show_success_message()

    def sign_documents(self):
        pyautogui.click(252, 66)  # Clique no ícone de assinatura
        time.sleep(3)
        pyautogui.click(570, 336)  # Clique no primeiro item da lista
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'a')  # Seleciona todos os documentos
        time.sleep(0.5)
        pyautogui.click(688, 528)  # OK!
        time.sleep(3)
        pyautogui.click(647, 322)  # Seleciona segundo certificado
        time.sleep(3)
        pyautogui.click(x=873, y=476)  # OK do certificado
        time.sleep(300)
        pyautogui.click(x=683, y=392)  # OK final
        time.sleep(3)

    def import_documents(self):
        pyautogui.click(318, 61)  # Ícone de importação
        time.sleep(3)
        pyautogui.click(541, 337)  # Clique no primeiro documento
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'a')  # Selecionar todos os documentos
        time.sleep(0.5)
        pyautogui.click(693, 527)  # OK!
        time.sleep(300)
        pyautogui.click(x=733, y=467)  # Fechar
        time.sleep(3)

    def show_success_message(self):
        pyautogui.alert("OS ARQUIVOS FORAM TRANSMITIDOS COM SUCESSO")

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Painel de Controle")
        self.setGeometry(1200, 100, 300, 400)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setStyleSheet("""
            background-color: rgba(245, 245, 245, 200);
            border: 1px solid #000;
            border-radius: 10px;
            font-family: Arial, sans-serif;
        """)

        self.total_loops = 0
        self.current_loop = 0
        self.is_running = False

        layout = QVBoxLayout()

        self.label_status = QLabel("Status: Parado")
        self.label_status.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(self.label_status)

        self.label_current_loop = QLabel("Loop Atual: 0")
        self.label_current_loop.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.label_current_loop)

        self.label_total_loops = QLabel("Total de Loops: 0")
        self.label_total_loops.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.label_total_loops)

        self.label_skipped_files = QLabel("Arquivos Pulados: 0")
        self.label_skipped_files.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.label_skipped_files)

        self.slider_speed = QSlider(Qt.Horizontal)
        self.slider_speed.setMinimum(1)
        self.slider_speed.setMaximum(20)
        self.slider_speed.setValue(10)
        self.slider_speed.valueChanged.connect(self.update_speed)
        layout.addWidget(QLabel("Velocidade:"))
        layout.addWidget(self.slider_speed)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.button_pause = QPushButton("Pausar")
        self.button_pause.setStyleSheet("""
            background-color: #FFA500;
            color: white;
            border: 1px solid #000;
        """)
        self.button_pause.clicked.connect(self.pause)
        layout.addWidget(self.button_pause)

        self.button_continue = QPushButton("Continuar")
        self.button_continue.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            border: 1px solid #000;
        """)
        self.button_continue.clicked.connect(self.continue_)
        layout.addWidget(self.button_continue)

        self.button_stop = QPushButton("Parar")
        self.button_stop.setStyleSheet("""
            background-color: #f44336;
            color: white;
            border: 1px solid #000;
        """)
        self.button_stop.clicked.connect(self.stop)
        layout.addWidget(self.button_stop)

        self.setLayout(layout)

    def update_display(self):
        self.label_status.setText("Status: Em Execução" if self.is_running else "Status: Parado")
        self.label_current_loop.setText(f"Loop Atual: {self.current_loop}")
        self.label_total_loops.setText(f"Total de Loops: {self.total_loops}")
        self.label_skipped_files.setText(f"Arquivos Pulados: {len(arquivos_pulados)}")

    def update_speed(self):
        multiplier = self.slider_speed.value() / 10.0
        self.parent().multiplier = multiplier

    def pause(self):
        self.is_running = False
        self.update_display()
        self.parent().thread.is_paused = True

    def continue_(self):
        self.is_running = True
        self.update_display()
        self.parent().thread.is_paused = False

    def stop(self):
        self.is_running = False
        self.current_loop = 0
        self.update_display()
        self.parent().thread.terminate()

class APPEFD(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Transmissão de Arquivos EFD")
        self.setGeometry(100, 100, 800, 600)
        #self.setWindowIcon(QIcon("C:/Users/Enzo/Desktop/ByteVault/PROJETOS/Auto Transmissão de Arquivos EFD/icon 3.png"))
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f8ff;
            }
            QLabel {
                font-size: 14px;
                font-family: Arial, sans-serif;
                color: #333;
            }
            QComboBox, QLineEdit {
                font-size: 14px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-family: Arial, sans-serif;
            }
            QPushButton {
                font-size: 14px;
                padding: 10px;
                border: 1px solid #000;
                border-radius: 4px;
                font-family: Arial, sans-serif;
            }
            QPushButton#start_button {
                background-color: #4CAF50;
                color: white;
            }
            QPushButton#start_button:hover {
                background-color: #45a049;
            }
            QPushButton#save_path_button {
                background-color: #FFA500;
                color: white;
            }
            QPushButton#save_path_button:hover {
                background-color: #FF8C00;
            }
            QPushButton#clear_actions_button {
                background-color: #f44336;
                color: white;
            }
            QPushButton#clear_actions_button:hover {
                background-color: #e53935;
            }
            QPushButton:hover {
                border: 1px solid #000;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
            }
            QSlider {
                background: #ccc;
                border: 1px solid #999;
                height: 10px;
                margin: 5px 0;
            }
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
                font-family: Arial, sans-serif;
                color: #333;
            }
        """)

        main_layout = QVBoxLayout()

        self.label_multiplier = QLabel("Escolha o multiplicador do tempo de suspensão:")
        main_layout.addWidget(self.label_multiplier)

        self.combo_box_multiplier = QComboBox()
        self.combo_box_multiplier.addItems(["1.0", "1.10", "1.20", "1.30", "1.40", "1.50", "1.60", "1.70", "1.80", "1.90", "2.0"])
        main_layout.addWidget(self.combo_box_multiplier)

        self.label_num_loops = QLabel("Digite o número de loops desejado:")
        main_layout.addWidget(self.label_num_loops)

        self.input_num_loops = QLineEdit()
        main_layout.addWidget(self.input_num_loops)

        self.save_path_button = QPushButton("Escolha onde salvar o arquivo de log", self)
        self.save_path_button.setObjectName("save_path_button")
        self.save_path_button.clicked.connect(self.select_save_path)
        main_layout.addWidget(self.save_path_button)

        self.start_button = QPushButton("Start", self)
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.start_process)
        main_layout.addWidget(self.start_button)

        self.clear_actions_button = QPushButton("Limpar Ações", self)
        self.clear_actions_button.setObjectName("clear_actions_button")
        self.clear_actions_button.clicked.connect(self.clear_actions)
        main_layout.addWidget(self.clear_actions_button)

        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        main_layout.addWidget(self.log_display)

        self.setLayout(main_layout)

        self.log_file_path = ""

        self.control_panel = ControlPanel(self)
        self.control_panel.show()
        self.multiplier = 1.0

    def select_save_path(self):
        self.log_file_path = QFileDialog.getSaveFileName(self, "Salvar Arquivo de Log", "", "Text Files (*.txt)")[0]

    def start_process(self):
        multiplier = float(self.combo_box_multiplier.currentText())
        try:
            num_loops = int(self.input_num_loops.text())
        except ValueError:
            QMessageBox.critical(self, "Erro", "Por favor, insira um número válido de loops.")
            return

        if not self.log_file_path:
            QMessageBox.warning(self, "Aviso", "Por favor, escolha um local para salvar o arquivo de log.")
            return

        inicio(multiplier)
        diretorio(multiplier)

        self.control_panel.is_running = True
        self.control_panel.total_loops = num_loops
        self.control_panel.progress_bar.setMaximum(num_loops)
        self.control_panel.update_display()
        self.showMinimized()

        self.thread = AutomationThread(num_loops, multiplier, self.log_file_path)
        self.thread.log_signal.connect(self.update_log_display)
        self.thread.progress_signal.connect(self.update_progress)
        self.thread.pause_signal.connect(self.update_pause_status)
        self.thread.finished.connect(self.execution_finished)
        self.thread.start()

    def update_log_display(self, log_entry):
        self.log_display.append(log_entry)
        self.control_panel.update_display()

    def update_progress(self, value):
        self.control_panel.current_loop = value
        self.control_panel.progress_bar.setValue(value)
        self.control_panel.update_display()

    def update_pause_status(self, is_paused):
        self.control_panel.is_running = not is_paused
        self.control_panel.update_display()

    def execution_finished(self):
        QMessageBox.information(self, "Informação", "A execução foi concluída.")
        self.control_panel.close()

    def clear_actions(self):
        global arquivos_pulados
        arquivos_pulados = []
        self.log_display.clear()
        self.control_panel.label_skipped_files.setText("Arquivos Pulados: 0")
        QCoreApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)

if __name__ == "__main__":
    app = QApplication([])
    window = APPEFD()
    window.show()
    app.exec_()
