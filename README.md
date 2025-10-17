# 🚀 Streamlit RISC-V Simulator

A web-based interactive simulator for the **RISC-V** instruction set architecture, built using **Streamlit**. This tool allows users to input assembly code, execute it cycle-by-cycle, and visualize the changes in the register file, memory, and execution pipeline.

---

## ✨ Features

* **Interactive Code Editor:** A dedicated area for writing and editing RISC-V assembly code.
* **Real-time Register View:** Displays all 32 RISC-V registers ($\text{x0}$ to $\text{x31}$) with their standard ABI names ($\text{zero}$, $\text{ra}$, $\text{sp}$, etc.) and current values.
* **Execution Controls:** Step-by-step execution and full run functionality.
* **Detailed Log:** Provides an execution log showing the sequence of instructions and any simulation errors.

---

## ⚙️ Project Structure

The application is organized into a modular structure for easy development and maintenance:

| Directory/File | Purpose |
| :--- | :--- |
| `app.py` | The main Streamlit application entry point. |
| `components/` | Contains reusable Streamlit UI components (e.g., `code_editor.py`, `register_file.py`). |
| `utils/` | Contains core logic and non-UI functions (e.g., `simulator.py` for execution). |
| `styles/` | Contains the custom CSS to style the application (e.g., `style.css`). |
| `assets/` | Reserved for images, icons, or other static assets. |

---

## 💻 Installation and Setup

### Prerequisites

You need **Python 3.8+** installed on your system.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/vishalsinha1602/VISHARO-RISC-V-WEB-VISUALIZER.git
    cd VISHARO-RISC-V-WEB-VISUALIZER
    ```

2.  **Create a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    You will need a `requirements.txt` file listing all required packages (at minimum, `streamlit`).
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run the Simulator

1.  Ensure your virtual environment is active.
2.  Run the main application file using Streamlit:

    ```bash
    streamlit run app.py
    ```

3.  Your default web browser will automatically open the application at `http://localhost:8501`.

---

## 📝 Usage

1.  Paste your RISC-V assembly code into the **Code Editor** area.
2.  Use the **Control Buttons** to start the simulation:
    * **Run:** Executes the entire program until completion.
    * **Step:** Executes one instruction at a time, allowing you to trace changes.
3.  Monitor the **Register File** and **Simulation Result** panels to track the program's state.

---

## 👥 Team

This project was developed by the following team members:

* **ROSELINE**
* **HARSHITA**
* **SHEWTA**
* **VISHAL**

---

## 🤝 Contributing

Contributions are welcome! If you find a bug or have an idea for an enhancement, please open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
