an article from the MIT Sloan School of Management, “a majority of data (80% to 90%, according to multiple analyst estimates) is unstructured information like text, video, audio, web server logs, social media, and more. That’s a huge untapped resource with the potential to create competitive advantage for companies that figure out how to use it. Unlike structured data — which is organized in a searchable format, like a database — unstructured data doesn’t adhere to conventional data models.”

# 🌟 Topic Modeling for Market Trends

### **Create a New Project Folder**

- Create a new folder on your desktop.
- Open Visual Studio Code and drag and drop the folder into the IDE.

### **Open the Terminal**

- Ensure the terminal is opened in the project folder. If not, use:
  ```bash
  cd /path/to/your/project/folder
  ```

### **Create a Virtual Environment**

- Run the following command to create a virtual environment:
  ```bash
  python3 -m venv .venv
  ```

### **Activate Virtual Environment**

- Activate the virtual environment by running:
  ```bash
  source .venv/bin/activate
  ```

### **Install Dependencies**

- Install the required Python libraries:
  ```bash
  pip install notebook ipykernel pandas numpy gensim nltk pyLDAvis matplotlib
  ```

### **Register the Virtual Environment as a Jupyter Kernel**

- Register the virtual environment:
  ```bash
  python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
  ```

### **Install VS Code Extensions**

- Install the following extensions from the VS Code marketplace:
  - **🐍 Python**
  - **📓 Jupyter**

### **Create a New Notebook File**

- Create a new file and save it with the `.ipynb` extension.

### **Select the Python Kernel**

- In the top-right corner of the notebook interface, click on the kernel dropdown.
- Select `Python (.venv)` as the kernel. If it doesn’t appear, restart VS Code.

### **Test the Setup**

- 🧪 Insert the following code into a notebook cell and run it to verify:

  ```python
  import sys
  print(sys.version)

  import pandas as pd
  print(pd.__version__)
  ```

---
