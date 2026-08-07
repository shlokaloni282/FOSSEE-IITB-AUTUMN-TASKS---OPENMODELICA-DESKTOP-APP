import os
import sys
import subprocess

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QFileDialog,
    QLineEdit,
    QMessageBox,
)


class SimulationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.exe_path = ""

        self.setWindowTitle("Two Connected Tanks Simulator")
        self.setGeometry(300, 200, 600, 350)

        layout = QVBoxLayout()

        # Executable
        layout.addWidget(QLabel("OpenModelica Executable"))

        self.pathLabel = QLabel("No executable selected")
        self.pathLabel.setWordWrap(True)
        layout.addWidget(self.pathLabel)

        self.browseButton = QPushButton("Browse Executable")
        self.browseButton.clicked.connect(self.browse_executable)
        layout.addWidget(self.browseButton)

        # Start time
        layout.addWidget(QLabel("Start Time"))

        self.startInput = QLineEdit()
        self.startInput.setPlaceholderText("Example: 0")
        layout.addWidget(self.startInput)

        # Stop time
        layout.addWidget(QLabel("Stop Time"))

        self.stopInput = QLineEdit()
        self.stopInput.setPlaceholderText("Example: 4")
        layout.addWidget(self.stopInput)

        # Run button
        self.runButton = QPushButton("Run Simulation")
        self.runButton.clicked.connect(self.run_simulation)
        layout.addWidget(self.runButton)

        # Status
        self.statusLabel = QLabel("Status: Waiting")
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

    def browse_executable(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select TwoConnectedTanks.exe",
            "",
            "Executable (*.exe)"
        )

        if file_name:
            self.exe_path = file_name
            self.pathLabel.setText(file_name)

    def run_simulation(self):
        # Check executable
        if not self.exe_path:
            QMessageBox.warning(
                self,
                "Error",
                "Please select the OpenModelica executable."
            )
            return

        # Read input
        try:
            start = int(self.startInput.text())
            stop = int(self.stopInput.text())
        except ValueError:
            QMessageBox.warning(
                self,
                "Error",
                "Start time and stop time must be integers."
            )
            return

        # Required condition from task
        if not (0 <= start < stop < 5):
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Condition must satisfy:\n"
                "0 <= Start Time < Stop Time < 5"
            )
            return

        self.statusLabel.setText("Status: Running...")
        self.runButton.setEnabled(False)

        # ---------------------------------------------------------
        # OpenModelica runtime directory
        # ---------------------------------------------------------
        om_bin = r"C:\Program Files\OpenModelica1.27.0-64bit\bin"

        if not os.path.exists(om_bin):
            QMessageBox.critical(
                self,
                "OpenModelica Error",
                "OpenModelica bin directory was not found:\n\n"
                + om_bin
            )
            self.runButton.setEnabled(True)
            self.statusLabel.setText("Status: Failed")
            return

        # Copy current environment
        env = os.environ.copy()

        # Add OpenModelica runtime DLL directory to PATH
        env["PATH"] = om_bin + os.pathsep + env.get("PATH", "")

        # Working directory = directory containing executable
        working_dir = os.path.dirname(self.exe_path)

        # Command
        command = [
            self.exe_path,
            f"-startTime={start}",
            f"-stopTime={stop}",
        ]

        print("\nWorking Directory:")
        print(working_dir)

        print("\nOpenModelica bin:")
        print(om_bin)

        print("\nCommand:")
        print(command)

        try:
            result = subprocess.run(
                command,
                cwd=working_dir,
                env=env,
                capture_output=True,
                text=True,
            )

            print("\nSTDOUT:")
            print(result.stdout)

            print("\nSTDERR:")
            print(result.stderr)

            print("\nReturn Code:")
            print(result.returncode)

            if result.returncode == 0:
                self.statusLabel.setText(
                    "Status: Simulation Completed"
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Simulation completed successfully!\n\n"
                    + result.stdout
                )

            else:
                self.statusLabel.setText(
                    "Status: Simulation Failed"
                )

                QMessageBox.critical(
                    self,
                    "Simulation Error",
                    f"Return Code: {result.returncode}\n\n"
                    f"STDOUT:\n{result.stdout}\n\n"
                    f"STDERR:\n{result.stderr}"
                )

        except Exception as error:
            self.statusLabel.setText("Status: Simulation Failed")

            QMessageBox.critical(
                self,
                "Execution Error",
                str(error)
            )

        finally:
            self.runButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SimulationApp()
    window.show()

    sys.exit(app.exec())