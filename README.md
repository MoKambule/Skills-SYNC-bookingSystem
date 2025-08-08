# 👩‍🏫 Mentor Finder (Python + Firebase)

This is a personal project built to practice working with **Firebase Firestore** in Python.  
It queries a Firestore database to fetch available mentors based on their role and availability.

---

## 📌 Project Overview

- Retrieves all users with the role of `"mentor"` from the Firestore `users` collection  
- Collects relevant information such as mentor `name`, `expertise`, and `availability`  
- Returns a list of mentors in a structured format  

This project was created for **learning and practice purposes**.

---

## 🔧 Requirements

- Python 3.7 or higher  
- Firebase Admin SDK  
- A Firebase Firestore project  
- A `serviceAccountKey.json` file for Firebase Admin initialization  

---

## 📦 Install Dependencies

Install the required package using pip:

```bash
pip install firebase-admin
