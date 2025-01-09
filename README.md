# Solar Browser

Solar Browser is a Python-based web browser for desktop. It uses **QtWebEngine** as its core. In the future, I plan to develop a custom web engine using Python. If successful, this custom engine will replace the current one, likely in version **1.0** or later. Additionally, I aim to release a **C++ version** of Solar Browser, which will utilize **Firefox's Gecko web engine** instead of the Chromium-based engine. 

Thank you for your support!

---

## Features (Planned and Current)
- **Current:**
  - Python-based application using QtWebEngine.
  - Easy-to-run setup for developers.

- **Future:**
  - Custom Python-based web engine.
  - C++ version with Gecko web engine for enhanced performance and compatibility.

---

## How to Run?
This section is for those who want to run Solar Browser when no releases are available in the [Releases](#) tab or on the official website. It is also intended for developers contributing to the project.

### Prerequisites
1. **Install Python**:
   - Download Python from: [https://www.python.org/](https://www.python.org/downloads/).
   - During installation on Windows, ensure to tick the **Install pip** option in the setup configuration. Pip is required to install dependencies.

2. **Install Required Packages**:
   - Open a terminal and run the following commands:

     ```bash
     pip install PyQt5
     pip install PyQtWebEngine
     ```

### Running Solar Browser
1. Once the dependencies are installed, navigate to the project folder in the terminal.
2. Run the application using the following command:

   ```bash
   python desktop.py
   ```

3. Alternatively, you can build the project if required.

---

## For Developers
For more detailed developer instructions, refer to the [Developer Guide](For%20Developers.md).

---

## Roadmap
- **Version 0.x**:
  - Continued improvements and feature enhancements for the Python-based browser.
- **Version 1.0+**:
  - Transition to a custom Python-based web engine.
  - Release of the C++ version with Gecko web engine.

---

### Thank You!
Your support means everything! If you encounter issues or have suggestions, feel free to contribute or report them via the [GitHub Issues](#) page.
