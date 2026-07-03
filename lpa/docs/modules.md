# 📘 **LPA Module Architecture & Development Guide**

## Overview  
The LPA module suite forms the analytical backbone of the LinPEAS‑Analyser Tool. Each module is a self‑contained Python processor responsible for interpreting a specific Privilege Escalation Principle or analysis domain. The engine dynamically loads these modules, executes their logic against LinPEAS output, and aggregates the results into a structured, principle‑aligned report.

The modules were created through a **human–AI co‑development workflow**:  
- You defined the conceptual model, PrivEsc principles, and structural rules.  
- AI assistance generated consistent module templates and rule‑based processors.  
- You refined, validated, and contextualised each module to ensure correctness and alignment with the Privilege‑Escalation-Principles.md document.

This hybrid workflow ensures the modules are both **technically robust** and **pedagogically clear**, suitable for learning, analysis, and professional reporting.

---

## Module Naming Convention  
All modules follow a strict three‑element naming pattern:

### **1. `lpa_` prefix**  
Every module begins with `lpa_` to identify it as part of the LinPEAS‑Analyser Tool ecosystem.

Examples from your repo:  
- `lpa_binary_capability_analysis.py`  
- `lpa_environmental_issues.py`  
- `lpa_final_summary.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### **2. Principle or Analysis Type Name**  
The second element identifies the PrivEsc principle or analysis domain implemented by the module.

Examples:  
- `lpa_sudo_misconfigurations.py` → Sudo misconfiguration principle  
- `lpa_kernel_exposures.py` → Kernel exposure principle  
- `lpa_filesystem_permissions.py` → Permissions principle  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### **3. `.py` extension**  
All modules are standard Python files, enabling dynamic loading and introspection.

### **Full Naming Pattern**  
```
lpa_<principle-or-analysis-type>.py
```

This naming convention is intentionally simple, predictable, and scalable.

---

## Real Module Examples (from LPA repository)  
Below is a curated list of your actual modules, grouped by conceptual purpose.

### 🔧 **Privilege Escalation Vector Modules**  
These modules directly map to PrivEsc principles:

- `lpa_sudo_misconfigurations.py`  
- `lpa_filesystem_permissions.py`  
- `lpa_kernel_exposures.py`  
- `lpa_network_exposures.py`  
- `lpa_service_misconfigurations.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### 🧩 **Capability & Token Modules**  
These modules analyse privilege‑related capabilities and tokens:

- `lpa_binary_capability_analysis.py`  
- `lpa_capabilities.py`  
- `lpa_token_inventory.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### 🧱 **Environment & Configuration Modules**  
These modules detect misconfigurations and environmental weaknesses:

- `lpa_environmental_analysis.py`  
- `lpa_environmental_issues.py`  
- `lpa_misconfig_analysis.py`  
- `lpa_container_analysis.py`  
- `lpa_container_risks.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### 🔐 **Credential & Secret Modules**  
These modules detect credential exposures and authentication weaknesses:

- `lpa_credential_analysis.py`  
- `lpa_credential_exposures.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### 🧠 **CVE & Vulnerability Modules**  
These modules contextualise kernel and software vulnerabilities:

- `lpa_cve_collapse.py`  
- `lpa_cve_contextualisation.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### 📊 **Structural & Summary Modules**  
These modules provide high‑level system views and final reporting:

- `lpa_system_overview.py`  
- `lpa_execution_flow.py`  
- `lpa_hardening_recommendations.py`  
- `lpa_final_summary.py`  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

---

## How Modules Are Structured  
Each module contains:

- A `process(section_id, subsection_id, context)` function  
- Rule‑based logic to interpret LinPEAS output  
- Structured findings returned as dictionaries:
  - `issue`  
  - `item`  
  - `details`  
  - optional `evidence`  
- Optional enrichment using the knowledge base (`lpa-kb.json`)

Modules are designed to be **deterministic**, **stateless**, and **fully isolated**, ensuring predictable behaviour and safe dynamic loading.

---

## Relationship to Privilege-Escalation-Principles.md  
The modules are contextualised directly through the **Privilege-Escalation-Principles.md** document.

### **1. Principle Definition**  
The principles document defines *what* each PrivEsc vector represents.

### **2. Module Implementation**  
Each module implements the *logic* required to detect evidence of that principle.

Examples:  
- `lpa_sudo_misconfigurations.py` → Sudo privilege boundary weaknesses  
- `lpa_kernel_exposures.py` → Kernel CVE exposure mapping  
- `lpa_filesystem_permissions.py` → Weak permission exploitation paths  
  [github.com](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/tree/main/lpa/modules)

### **3. Profile Mapping**  
The profile (`lpa-default.json`) maps LinPEAS sections to modules using `analysis_type`.

This creates a complete chain:

**Principle → Module → Profile → LinPEAS Section → LPA Report**

---

## How Modules Were Developed (Human + AI Collaboration)  
The module suite was created using a structured workflow:

1. **You defined the PrivEsc principles**  
2. **AI generated module templates**  
3. **You refined and validated each module**  
4. **AI assisted with KB integration**

This workflow produced modules that are both technically correct and pedagogically aligned with your teaching model.

---

## Adding New Modules in the Future  
The module system is intentionally designed to be **extensible**.

### **Step 1 — Define the New Principle**  
Add the conceptual definition to *Privilege-Escalation-Principles.md*.

### **Step 2 — Create a New Module File**  
Follow the naming convention:

```
lpa_<newprinciple>.py
```

### **Step 3 — Add KB Entries**  
Extend `lpa-kb.json`.

### **Step 4 — Update the Profile**  
Map the new LinPEAS section to your module.

### **Step 5 — Validate Output**  
Run LPA against known LinPEAS samples.

---

## Summary  
The LPA module system is:

- **Structured**  
- **Predictable**  
- **Extensible**  
- **Aligned with PrivEsc principles**  
- **Built through human–AI collaboration**  

Your repo now contains a professional‑grade module architecture ready for teaching, analysis, and future expansion.

---

