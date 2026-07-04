# **LinPEAS‑Analyser‑Tool (LPA)**

The **LinPEAS‑Analyser‑Tool (LPA)** is a structured analysis engine that processes raw LinPEAS output and converts it into a clear, modular, vulnerability‑focused privilege‑escalation report.

LPA does **not** replace LinPEAS — it **extends** it.  
LinPEAS is one of the most widely used Linux privilege‑escalation enumeration tools, and without LinPEAS this analyser would not exist.

👉 [**LinPEAS Repository**](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS) 

---

## **What LPA Does**
LPA takes the raw, unstructured LinPEAS output and:

- extracts relevant sections using profile markers  
- processes each subsection through modular analysis engines  
- matches findings against a structured vulnerability knowledge base  
- produces a clean Markdown report  
- aligns findings with Privilege‑Escalation‑Principles  
- provides remediation guidance where applicable  

This makes LinPEAS output easier to understand, easier to navigate, and easier to act upon.

---

## **📘 Documentation Overview**

### **📘 [lpa.md](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/blob/main/lpa/docs/lpa.md) — How LPA Works**
A practical guide explaining:
- how to run LPA  
- what input/output looks like  
- how the internal workflow operates  
- how modules and profiles interact  
- how to interpret the final report  

---

### **📘 [profiles.md](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/blob/main/lpa/docs/profilles.md) — Profiles & Structure**
A technical breakdown of:
- how `lpa-default.json` defines sections, markers, and subsections  
- how `lpa-kb.json` defines vulnerabilities  
- naming conventions  
- alphabetical ordering rules  

---

### **📘 [modules.md](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/blob/main/lpa/docs/modules.md) — Analysis Modules**
A developer‑focused overview describing:
- each analysis module  
- what subsection it processes  
- what data it extracts  
- how it interacts with the KB  
- how modules contribute to the final report  

---

### **📘 [Privilege‑Escalation‑Principles.md](https://github.com/Mark-a-Hamilton/LinPEAS-Analyser-Tool/blob/main/lpa/docs/Privilege-Escalation-Principles.md)**
A methodology guide explaining:
- how to evaluate findings  
- how to identify exploit paths  
- how to prioritise remediation  
- how to apply privilege‑escalation logic consistently  

---

## **Why LPA Exists**
LinPEAS produces a huge amount of valuable information — but it is raw, dense, and unstructured.

LPA exists to:

- reduce analysis time  
- highlight actionable findings  
- provide structured vulnerability intelligence  
- make privilege‑escalation enumeration easier to understand  
- support both learning and professional use  

---

## **Acknowledgements**
Special thanks to the creators of **LinPEAS** and **PEASS‑NG**.  
Their work is foundational to Linux privilege‑escalation research and tooling.

---
