# Two Connected Tanks — OpenModelica Desktop App

A PyQt6 desktop application for running an OpenModelica-generated simulation of the `NonInteractingTanks.TwoConnectedTanks` model.

This project was developed as part of the **FOSSEE/OpenModelica Desktop App Screening Task**.

---

## 📌 Overview

The project consists of two main parts:

1. **OpenModelica Simulation**
   - Load and compile the supplied `TwoConnectedTanks` Modelica model using OpenModelica/OMEdit.
   - Generate the simulation executable and its dependent files.

2. **Python Desktop Application**
   - Build a desktop GUI using Python and PyQt6.
   - Allow the user to select the generated OpenModelica executable.
   - Accept simulation start and stop times.
   - Validate the input parameters.
   - Execute the simulation with the supplied parameters.
   - Display the simulation status and execution errors.

The application is designed to provide a simple interface for running the compiled OpenModelica simulation without manually entering simulation commands in a terminal.

---

## 🔄 Application Workflow

```mermaid
flowchart TD
    A["TwoConnectedTanks Modelica Model"]
    B["OpenModelica / OMEdit"]
    C["Compile Model"]
    D["Generated Executable and Dependencies"]
    E["PyQt6 Desktop Application"]
    F["Select Executable"]
    G["Enter Start and Stop Time"]
    H{"Validate Input"}
    I["Run Simulation"]
    J["Simulation Completed"]
    K["Display Error"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H -->|Valid| I
    H -->|Invalid| K
    I -->|Success| J
    I -->|Failure| K
