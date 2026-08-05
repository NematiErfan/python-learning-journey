# FPGA Lab Manager

A Python-based Object-Oriented Programming project for managing FPGA devices in a virtual hardware laboratory.

This project simulates a simple FPGA laboratory management system where users can add, search, remove, and monitor FPGA devices through a command-line interface.

---

## Project Overview

The goal of this project is to practice and apply Object-Oriented Programming concepts in Python by designing a small hardware management system.

The project contains two main classes:

- `FPGA` → Represents an FPGA device with its specifications and behaviors.
- `FPGALab` → Manages multiple FPGA objects inside a laboratory environment.

---

## Features

### FPGA Management

- Create FPGA objects with:
  - Name
  - Vendor
  - Frequency
  - Power consumption
  - LUT resources

- Configure FPGA status
- Reset FPGA status
- Increase operating frequency
- Enable low power mode
- Display FPGA information

---

### Laboratory Management

The FPGA Lab Manager allows users to:

- Add new FPGA devices
- Show all available FPGAs
- Search for an FPGA by name
- Remove an FPGA
- Generate total power consumption reports
- Calculate total LUT resources

---

## Object-Oriented Programming Concepts Used

### Classes and Objects

Creating FPGA objects:

```python
fpga = FPGA("ARTIX7", "AMD", 100, 6, 5000)
```

---

### Attributes

Each FPGA object stores its own data:

```python
self.name
self.vendor
self.frequency
self.power
self.luts
self.configured
```

---

### Methods

Objects contain behaviors:

```python
configure()
reset()
increase_frequency()
low_power_mode()
```

---

### Special Methods

Python built-in behaviors:

### `__str__()`

Allows readable object printing:

```python
print(fpga)
```

### `__len__()`

Allows LUT calculation:

```python
len(fpga)
```

---

### Object Composition

The `FPGALab` class manages multiple FPGA objects:

```python
self.fpgas = []
```

Each laboratory contains a collection of FPGA devices.

---

## Project Structure

```
FPGA-Lab-Manager/
│
├── main.py          # User interface and program control
│
├── fpga.py          # FPGA class definition
│
├── lab.py           # FPGALab management class
│
└── README.md        # Project documentation
```

---

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd FPGA-Lab-Manager
```

Run the program:

```bash
python main.py
```

---

## Example Usage

```
================
FPGA Lab Manager
================

1. Add FPGA
2. Show FPGA
3. Find FPGA
4. Remove FPGA
5. Power Report
6. Exit

Select an Option: 1

Enter FPGA Name: ARTIX7
Enter FPGA Vendor: AMD
Enter FPGA Frequency: 100
Enter FPGA Power: 6
Enter FPGA LUTs Number: 5000

New FPGA Added!
```

---

## Example FPGA Output

```
FPGA ARTIX7 produced by AMD
Frequency: 100 MHz
Power: 6 W
LUTs: 5000
FPGA Not Configured
```

After configuration:

```
FPGA ARTIX7 produced by AMD
Frequency: 125 MHz
Power: 3 W
LUTs: 5000
FPGA Configured
```

---

## Future Improvements

Possible future extensions:

- Save FPGA data using JSON files
- Load previous laboratory configurations
- Add FPGA editing functionality
- Create a graphical user interface (GUI)
- Add database support
- Implement automated testing

---

## Author

Erfan Nemati

Python Learning Journey - OOP Project