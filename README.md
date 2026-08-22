# Two Connected Tanks — OpenModelica Desktop App

A PyQt6 desktop application for running an OpenModelica-generated
simulation of the `NonInteractingTanks.TwoConnectedTanks` model.

This project was developed as part of the FOSSEE/OpenModelica Desktop App
Screening Task.

---

## 📌 Overview

The project consists of two main parts:

1. Compiling the supplied `TwoConnectedTanks` Modelica model using
   OpenModelica to generate a simulation executable and its dependent files.
2. Building a Python/PyQt6 desktop application that allows the user to
   select the generated executable, provide simulation start and stop times,
   and launch the simulation.

The application validates the simulation parameters before execution and
reports whether the simulation completed successfully.

---

## 🔄 Workflow

```mermaid
flowchart TD
    A["Modelica Model<br/>TwoConnectedTanks"]
    B["OpenModelica / OMEdit<br/>Compile"]
    C["Executable + Dependencies"]
    D["PyQt6 Desktop App"]
    E["Select + Enter Parameters"]
    F{"Validate<br/>0 ≤ start < stop < 5"}
    G["Run Simulation"]
    H["Simulation Result"]
    I["Error"]

    A --> B --> C --> D --> E --> F
    F -->|Valid| G --> H
    F -->|Invalid| I
    G -->|Failed| I

## ✨ Features

- PyQt6-based desktop GUI
- Executable file selection using a file dialog
- Start time input
- Stop time input
- Input validation
- Enforces:

  `0 <= start time < stop time < 5`

- Passes simulation parameters to the OpenModelica executable
- Displays simulation status
- Displays execution errors when the simulation fails
- Uses an object-oriented Python application structure
- Keeps the OpenModelica model and generated executable files organized
  separately from the GUI code

---

## 🛠️ Technologies Used

- **Python 3.6+**
- **PyQt6**
- **OpenModelica**
- **Windows 10/11**

The current implementation was developed and tested on Windows.

---

## 📁 Project Structure

```text
FOSSEE_TwoConnectedTanks/
│
├── app.py
├── requirements.txt
├── README.md
│
├── executable/
│   ├── TwoConnectedTanks.bat
│   ├── TwoConnectedTanks.exe
│   ├── TwoConnectedTanks_init.xml
│   ├── TwoConnectedTanks_info.json
│   ├── TwoConnectedTanks_external_functions.json
│   ├── TwoConnectedTanks_res.mat
│   ├── TwoConnectedTanks.log
│   └── other OpenModelica-generated files
│
├── model/
│   └── NonInteractingTanks/
│       ├── package.mo
│       ├── package.order
│       ├── FlowConnect.mo
│       ├── Tank.mo
│       ├── Tank2.mo
│       └── TwoConnectedTanks.mo
│
└── screenshots/
    ├── condition.png
    ├── generated_files.png
    ├── pyqt_app.png
    └── simulation_success.png
