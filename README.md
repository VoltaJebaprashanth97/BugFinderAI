# 🚀 Bug Finder AI

**Bug Finder AI** is a powerful AI-driven bug tracking system that helps software teams quickly find similar bug reports based on contextual meaning rather than exact keywords. 

It leverages **Natural Language Processing (NLP)** to enhance bug retrieval and reduce redundant issue reporting.

Created by **Volta Jebaprashanth** for use at Bileeta. Feel free to reach out at **voltajeba@gmail.com** or **+94774637185**.

The front end implementation is here: [BugFinder AI Frontend](https://github.com/VoltaJebaprashanth97/BugFinder-UI).

![Alt text](https://raw.githubusercontent.com/VoltaJebaprashanth97/BugFinder-UI/refs/heads/main/assets/Screenshot1.png)

---

## 📝 Features

✅ **AI-Powered Similarity Search** – Uses `SentenceTransformer` to Finds relevant bug reports beyond simple keyword matching.  

✅ **FastAPI Backend** – High-performance web API for seamless integration.  

✅ **Integration with Azure TFS** – Supports work item retrieval from Azure TFS and other project management tools.

✅ **Filtering Options** – Search bugs by status, project, assigned user, and more.

✅ **High Accuracy** – Leverages advanced NLP models to improve retrieval precision.  

✅ **Easy Integration** – RESTful API endpoints for external applications.  

✅ **Open Source** – Built for the community, contributions welcome!  

---

## 📂 Project Structure

```
📂 BugFinderAI/
│── 📂 AI/                        # AI-based similarity search models
│── 📂 Filter/                    # filteration logic
│── 📂 Initiator/                 # core initialization logic
│── 📂 PreProcessing/             # preprocess the dataset
│── 📂 Runner/                    # initialization runner
│── 📂 SendFilters/               # filteration with requests
│── 📂 SystemFiles/               # the CSV with bulk dataset should be kept here
│── 📂 Utils/                     # utilities
│── 📜 Config.py                  # confgurations
│── 📜 main.py                    # FastAPI entry point
│── 📜 requirements.txt           # Python dependencies
│── 📜 README.md                  # Project documentation
│── 📜 .gitignore                 # Ignore unnecessary files
│── 📜 LICENSE                    # Open-source license
```

---

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/VoltaJebaprashanth97/BugFinderAI.git
cd BugFinderAI
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣Preprocess Your Data**  

1. **Export Work Items**  
   - Download a CSV file containing bulk work items from your project management tool (e.g., **Azure TFS Server** or any other platform).  

2. **Move the CSV File**  
   - Copy and paste the CSV file into the **`📂 SystemFiles/`** directory.  

3. **Run the Data Cleaning Script**  
   - Execute the following command to clean and preprocess your data:  
     ```sh
     python PreProcessing/DataCleaner.py
     ```  
   - Modify the script as needed to fit your specific data requirements.  

4. **Generate Embeddings**  
   - After cleaning the data, run the embedding script:  
     ```sh
     python PreProcessing/Embedding.py
     ```  

---
### **4️⃣ Run the API Server**
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```


The API should now be available at `http://localhost:8000` 🚀

---

## 📡 API Endpoints

### **🟢 Health Check**
```http
GET /
```
Response:
```json
"BUG FINDER AI IS RUNNING"
```

### **🔍 Find Similar Bugs without filters**
```http
GET /{given_text}
```
Example:
```http
GET /standard user cant do dispose
```
Response:
```json
[
{
  "ID": 100001,
  "Work Item Type": "Bug",
  "Project Code": "LK",
  "Title": "Unable to do commodity dispose using standard user",
  "Repro Steps": ".....",
  "Symptom": "....",
  "Issue Root Cause": ".....",
  "Proposed Fix": "....",
  "QA Remark": "...",
  "Unit Test Steps": "...",
  "System Info": "...",
  "Responsible Team": "Backend Team",
  "Issue Classification": "Permission Issue",
  "State": "Open",
  "Test By": "QA Team",
  "Tags": ["Permission", "User Role", "Commodity"],
  "Release No": "2.1.5",
  "Created By": "Alice Johnson",
  "Assigned To": "Bob Smith",
  "AC Tested Date": "2025-03-10",
  "Created Date": "2025-03-11 09:15:30",
  "Source Category": "User Report",
  "Cosine_Similarity": 0.7891234567
}  

]
```

### **📊 Get Available Filters**
```http
GET /get_filters
```

### **⚙️ Advanced Bug Search (POST)**
```http
POST /process_data
```
Example Payload:
```json
{
    "mode": "Title",
    "numberOfResults": 1000,
    "givenText": "Cannot do data entry",
    "searchFilters": {
        "workItemTypeFilter": ["Issue"],
        "statusFilter": ["Closed"],
        "projectCodeFilter": [],
        "testByFilter": ["Volta Jebaprashanth"],
        "assignedToFilter": ["Elon Musk"],
        "sourceCategoryFilter": [],
        "createdDateGreaterThanFilter": "2023-01-12",
        "createdDateLesserThanFilter": "2023-12-23"
    }
},
}
```

---


## 🤝 Contributing
We welcome contributions from the community! 🎉 To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## 🎯 Future Improvements
- 📊 **Implement a Dashboard** to visualize bug trends.
- 🚀 **Deploy as a Cloud API** for global access.
- 🤖 **Improve AI Model** for better accuracy.


---

## ⭐ Show Your Support!
If you like this project, don't forget to **⭐ Star** the repository! 😊

