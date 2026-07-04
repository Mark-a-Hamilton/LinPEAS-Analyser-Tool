# **Installation Guide — LinPEAS‑Analyser‑Tool (LPA)**

## **Overview**
The LinPEAS‑Analyser‑Tool (LPA) is designed to be portable, self‑contained, and easy to install.  
This guide provides:

- a recommended installation method for users without an existing tool layout  
- guidance for users with their own preferred directory structure  
- important notes about module and profile placement  
- instructions for adding LPA to your system PATH  

---

# **1. Recommended Installation (Standard Users)**

If you do not already use a structured tool layout, the simplest and most professional installation method is to place LPA under:

```
/usr/local/bin/python/
```

This location is ideal because:

- `/usr/local/bin` is reserved for **locally installed system tools**  
- placing LPA under a dedicated `python/` directory keeps the tool self‑contained  
- adding this directory to `PATH` makes LPA globally accessible  
- modules and profiles remain neatly grouped with the engine  

### **Directory Structure**
Your installation should look like this:

```
/usr/local/bin/python/
│
├── lpa
│
├── modules/
│   ├── system_overview.py
│   ├── sudo_rules.py
│   ├── kernel_version.py
│   └── ... (all other modules)
│
└── profiles/
    ├── lpa-default.json
    ├── lpa-kb.json
    └── ... (future profiles)
```

### **Installation Steps**

#### **1. Create the installation directory**
```bash
sudo mkdir -p /usr/local/bin/python
```

#### **2. Copy the LPA engine**
```bash
sudo cp lpa /usr/local/bin/python/
```

#### **3. Copy modules**
```bash
sudo cp -r modules /usr/local/bin/python/
```

#### **4. Copy profiles**
```bash
sudo cp -r profiles /usr/local/bin/python/
```

#### **5. Make the engine executable**
```bash
sudo chmod +x /usr/local/bin/python/lpa
```

#### **6. Add the directory to PATH**
Append the following line to `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="/usr/local/bin/python:$PATH"
```

Reload your shell:

```bash
source ~/.bashrc
```

---

# **2. Custom Installation (Advanced Users)**

If you already use a structured tool layout (e.g., `/opt/tools/`, `$HOME/.local/bin/`, or a custom security toolkit directory), you may install LPA anywhere you prefer.

### **However, the following rules must be followed:**

### **✔ lpa, modules/, and profiles/ MUST be in the same directory**
LPA uses **relative paths** to load:

- analysis modules  
- profile definitions  
- the knowledge base  

If these directories are separated, LPA will not function correctly.

### **✔ The directory containing lpa MUST be in your PATH**
Example:

```bash
export PATH="$HOME/tools/lpa:$PATH"
```

### **✔ The directory must remain writable if you plan to add custom modules or profiles**
This allows:

- custom analysis modules  
- custom KB entries  
- custom report structures  

---

# **3. Verifying the Installation**

Run:

```bash
lpa -h
```

You should see the LPA help menu, confirming that the tool is globally accessible.

---

# **4. Developer Mode**

If you prefer to run LPA directly from the repository (without installing):

```bash
python3 lpa -i linpeas-output.txt
```

Modules and profiles will be loaded from the local directory automatically.

---

# **5. Summary**

This installation strategy provides:

- a clean, professional directory structure  
- global accessibility  
- predictable module and profile resolution  
- compatibility with user‑defined layouts  
- support for both standard and advanced users  

LPA is now ready for use as a system‑level privilege‑escalation analysis tool.

---

