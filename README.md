# 🧪 Chemical Management System (CMS)

A lightweight, object-oriented command-line inventory tracker built in Python. Designed to keep track of laboratory chemicals—handling quantities, categories, and expiry dates with local data persistence and a built-in analytics dashboard.

---

## ✨ Features

* **Object-Oriented Design:** Clean separation of concerns using a `Chemical` model and an `Inventory` management class.
* **Full CRUD Operations:** Add, view, search (by ID or name), update (quantity or category), and remove chemicals seamlessly.
* **Persistent Storage:** Automatically saves and loads your inventory data using a local `chemicals.json` file so nothing gets lost when you close the app.
**Data Visualization:** Powered by `matplotlib` to generate a 2x2 analytics dashboard showing category breakdowns, unit distributions, expiry overviews, and total inventory metrics.
* **Interactive CLI Menu:** A clean, user-friendly command-line interface.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** 
  * `json` (Built-in for file I/O)
  * `matplotlib` (For generating analytics charts)

---

## 🚀 How to Run It

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/chemical-management-system.git](https://github.com/YOUR-USERNAME/chemical-management-system.git)
   cd chemical-management-system
