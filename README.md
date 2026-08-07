# Two Connected Tanks — OpenModelica Desktop App

A PyQt6 desktop application for running the OpenModelica-generated simulation of the `NonInteractingTanks.TwoConnectedTanks` model.

## Overview

This project was completed for the FOSSEE/OpenModelica desktop-app task. The task requires the supplied model package to be compiled in OpenModelica, producing an executable and its required dependent files, then used from a Python desktop application.

The application lets a user select the generated launcher, enter a simulation start time and stop time, validate those values, and run the simulation. The result is produced by the OpenModelica-generated program.

> **Implementation note**
> The task refers to selecting and executing the OpenModelica-generated executable. In this Windows implementation, the GUI selects `TwoConnectedTanks.bat`, the launcher generated beside `TwoConnectedTanks.exe`. The batch launcher sets the OpenModelica runtime path and then runs the executable. The compiled `.exe` remains the simulation program.

## Task Requirements Addressed

- Use Python 3.6+ and PyQt6.
- Use OpenModelica on a supported Windows or Linux operating system.
- Compile the `TwoConnectedTanks` model and retain the generated executable, dependent files, and required runtime dependencies.
- Provide a desktop GUI that accepts a start time and stop time and invokes the generated simulation program with those command-line options.
- Enforce the required time condition: `0 <= start time < stop time < 5`.

## Requirements

- Windows 10/11 (the current launcher workflow was tested on Windows).
- Python 3.6 or later.
- PyQt6.
- OpenModelica installed locally.

The generated Windows launcher expects the OpenModelica runtime to be available. On the development machine, it uses the OpenModelica `bin` directory through the generated batch file.

## Project Structure

```text
FOSSEE_TwoConnectedTanks/
│
├── app.py
├── requirements.txt
├── README.md
│
├── executable/
│   ├── TwoConnectedTanks.bat       # selected by the GUI (Windows launcher)
│   ├── TwoConnectedTanks.exe       # OpenModelica-generated executable
│   ├── TwoConnectedTanks_init.xml
│   ├── TwoConnectedTanks_info.json
│   ├── TwoConnectedTanks_external_functions.json
│   ├── TwoConnectedTanks_res.mat
│   ├── TwoConnectedTanks.log
│   └── other files generated with the executable
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
    ├── omedit_loaded.png
    ├── generated_files.png
    ├── pyqt_app.png
    └── simulation_success.png
```

File names in `executable/` may vary slightly by OpenModelica version. Keep the complete generated file set together; do not copy only the `.exe`.

## Model and Simulation Workflow

1. Open the `NonInteractingTanks` package in OMEdit.
2. Build or simulate `NonInteractingTanks.TwoConnectedTanks` to create the executable and companion files.
3. Copy the complete generated output into `executable/`.
4. Start the PyQt6 application.
5. Select `TwoConnectedTanks.bat` from `executable/`.
6. Enter valid start and stop times and run the simulation.
7. The batch launcher prepares the OpenModelica runtime environment and starts `TwoConnectedTanks.exe` with `-startTime` and `-stopTime` options.
8. OpenModelica writes the simulation result, including the `.mat` result file, in the executable directory.

> **Implementation note**
> During development, two model compatibility changes were made to run the supplied package in the installed OpenModelica version: `FlowConnect.mo` uses `flow Real F;`, and `Tank2.mo` protects the `V/Q1` calculation at zero flow. These are implementation details of this project, not additional task requirements.

## Install Dependencies

From the project root, create and activate a virtual environment if desired, then install the Python dependency:

```powershell
python -m pip install -r requirements.txt
```

`requirements.txt` should contain:

```text
PyQt6
```

## Run the Application

From the project root:

```powershell
python app.py
```

Ensure OpenModelica is installed before running a simulation. The generated `TwoConnectedTanks.bat` file contains the runtime setup used by this Windows implementation.

## Using the GUI

1. Click **Browse Executable**.
2. Select `executable/TwoConnectedTanks.bat`.
3. Enter a numeric **Start Time**.
4. Enter a numeric **Stop Time**.
5. Click **Run Simulation**.
6. Review the status label and success or error dialog.

For example, use:

```text
Start Time: 0
Stop Time: 4
```

On a successful run, OpenModelica reports a zero return code and a successful simulation message.

## Input Validation

The application checks that:

- A launcher file has been selected.
- Start Time and Stop Time are numeric.
- The values satisfy `0 <= Start Time < Stop Time < 5`.

For example, `Start Time = 0` and `Stop Time = 5` is rejected because the stop time must be strictly less than `5`.

## Generated Simulation Files

OpenModelica produces several files alongside the executable. Important examples include:

- `TwoConnectedTanks.exe` — compiled simulation program.
- `TwoConnectedTanks.bat` — Windows launcher that provides the runtime environment used by this implementation.
- `TwoConnectedTanks_init.xml` — initialization data that must match the executable.
- `TwoConnectedTanks_res.mat` — simulation results in MATLAB MAT format.
- `TwoConnectedTanks_info.json` and log/profile files — generated metadata and diagnostic output.

Do not mix files generated by different builds. In particular, an executable and its `_init.xml` file must come from the same OpenModelica build.

## Screenshots

Include the following screenshots in `screenshots/` before submission:

1. OMEdit with the `NonInteractingTanks` package loaded.
2. OMEdit output confirming the simulation finished successfully.
3. The generated executable folder, showing the executable and companion files.
4. The PyQt6 application with valid inputs and a successful simulation result.

Suggested image references once the files are added:

```markdown
![PyQt6 application](screenshots/pyqt_app.png)
![Successful simulation](screenshots/simulation_success.png)
```

## Troubleshooting

### The executable reports a missing OpenModelica DLL

Run the generated `TwoConnectedTanks.bat` instead of launching the `.exe` directly. The batch file sets the OpenModelica runtime path before starting the executable. Confirm that OpenModelica is still installed at the path referenced by the batch file.

### `TwoConnectedTanks_init.xml` does not match the executable

Regenerate the model in OpenModelica and copy the entire generated file set again. Do not combine a new `.exe` with an older `_init.xml` file.

### The application rejects the time values

Use numeric values satisfying `0 <= start < stop < 5`, for example `0` and `4`.

### The simulation fails but the app starts normally

Check the error dialog, terminal output, and `TwoConnectedTanks.log`. Also verify that the selected `.bat` file is in the same folder as its matching `.exe` and generated companion files.

## Verification Performed

The implementation was tested with a valid run using Start Time `0` and Stop Time `4`. The GUI completed the simulation successfully, receiving return code `0` and OpenModelica `LOG_SUCCESS` output.
