# 🔍 TP4 – Regular Expressions Toolkit

**Course:** Advanced Programming – Python  
**Year:** 3rd Year Computer Security Engineering (2025/2026)

---

## 📖 Overview

This TP focuses on text mining with Python's `re` module.  
The script `regex.py` reads Niccolò Machiavelli's *The Prince* (`the-prince.txt`) and extracts:
- four-digit years
- capitalized words
- capitalized full names
- quoted dialogues

Screenshots (`function.png`, `pattern.png`) and `RegEx.pdf` summarize the lecture content used to build these exercises.

---

## 🎯 Features

- ✅ Safe file loading with graceful fallback when the source is missing
- ✅ Reusable helper functions returning typed `List[str]` results
- ✅ Clearly documented regex patterns you can tweak quickly
- ✅ Standalone execution for quick debugging (`python regex.py`)
- ✅ Console previews of the extracted data to verify matches

---

## 📂 Project Structure

```
tp4/
├── regex.py         # Core script with helper extraction functions
├── the-prince.txt   # Sample corpus (Project Gutenberg)
├── RegEx.pdf        # Reference slides
├── function.png     # Class diagram of helpers
├── pattern.png      # Overview of regex syntax used
└── README.md        # This file
```

---

## 🧠 Regex Cheatsheet (used in `regex.py`)

| Helper | Pattern | Purpose |
|--------|---------|---------|
| `extractYears` | `\d{4}` | Grab every four-digit sequence (possible year) |
| `extractCapitilized` | `\b[A-Z][a-z]+\b` | Match words that start with a capital letter |
| `extractFullNames` | `\b[A-Z][a-z]+\b\s+\b[A-Z][a-z]+\b` | Detect simple `First Last` combinations |
| `extractDilogs` | `["'\`].+?["'\`]` | Capture text enclosed in single, double, or backtick quotes |

> Tip: Adjust the patterns (for example, allow hyphenated names) to refine the extraction accuracy for your own dataset.

---

## 🚀 How to Run

```bash
cd /Users/macbook/Desktop/advanced_python/tp4
python regex.py
```

The script will print the book content once (useful for debugging) followed by each extracted list.

---

## 💡 Example Output

```
['1513', '1811', '1908', '2012']
['Gutenberg', 'Literary', 'Archive', 'Foundation', 'Machiavelli']
['Niccolo Machiavelli', 'Project Gutenberg']
['"Of Mixed Principalities"', '"If France could be united"', '"As Pertinax said"']
```

---

## ✨ Key Concepts Practiced

- Reading text files safely with Python
- Designing focused helper functions
- Crafting and testing regex patterns
- Lazy vs greedy quantifiers
- Token boundaries (`\b`), character classes, and quantifiers (`+`, `{n}`)
- Quick validation of extraction logic via printouts

---

Need tighter matching? Start by refining the regex patterns above, rerun `python regex.py`, and compare the new lists. This loop mirrors the iterative workflow used in class. Enjoy experimenting! 🎉

