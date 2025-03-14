# 🌟 Topic Modeling for Market Trends

## **🚀 Getting Started**

Follow these steps to set up the project environment and get started:

### **1️⃣ Create a New Project Folder**
- 🖥️ Create a new folder on your desktop.
- 🎯 Open Visual Studio Code and drag and drop the folder into the IDE.

### **2️⃣ Open the Terminal**
- 💻 Ensure the terminal is opened in the project folder. If not, use:
  ```bash
  cd /path/to/your/project/folder
  ```

### **3️⃣ Create a Virtual Environment**
- 🛠️ Run the following command to create a virtual environment:
  ```bash
  python3 -m venv .venv
  ```

### **4️⃣ Activate Virtual Environment**
- ✅ Activate the virtual environment by running:
  ```bash
  source .venv/bin/activate
  ```

### **5️⃣ Install Dependencies**
- 📦 Install the required Python libraries:
  ```bash
  pip install notebook ipykernel pandas numpy gensim nltk pyLDAvis matplotlib
  ```

### **6️⃣ Register the Virtual Environment as a Jupyter Kernel**
- 🔗 Register the virtual environment:
  ```bash
  python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
  ```

### **7️⃣ Install VS Code Extensions**
- 🛍️ Install the following extensions from the VS Code marketplace:
  - **🐍 Python**
  - **📓 Jupyter**

### **8️⃣ Create a New Notebook File**
- 📄 Create a new file and save it with the `.ipynb` extension.

### **9️⃣ Select the Python Kernel**
- 🎛️ In the top-right corner of the notebook interface, click on the kernel dropdown.
- 🔄 Select `Python (.venv)` as the kernel. If it doesn’t appear, restart VS Code.

### **🔟 Test the Setup**
- 🧪 Insert the following code into a notebook cell and run it to verify:
  ```python
  import sys
  print(sys.version)
  
  import pandas as pd
  print(pd.__version__)
  ```

---
