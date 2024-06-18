### README.md

# Grouping Patent Texts for Mobile Communication Analysis

## By
Raz Tsook


## Objective
Our goal is to better understand competition in the mobile communications sector by studying patent claims. We have created a method to group patent claims into clear topics and use this method in a simple interactive tool. This tool lets users pick how many groups they want and shows the names and number of claims in each group.

## Tasks

### Task 1: Extracting Text from Patents
- **Goal:** Extract claims from three patents related to mobile communications.
- **Instructions:**
  - Choose three patents relevant to mobile communications.
  - Focus on extracting just the claims text.
  - **Bonus:** Automate this process using a tool like BeautifulSoup.

### Task 2: Grouping Claims by Topic
- **Goal:** Use different models to group claims by similar topics.
- **Instructions:**
  - Experiment with three different methods or models for grouping paragraphs in a Jupyter notebook (e.g., clustering algorithms, text generation).
  - Show the results of the grouping with a number of groups you define.
  - Compare these methods and select the best one for the next task. Explain why this method was chosen, focusing on its effectiveness and suitability for the task.

### Task 3: Creating an Interactive Application
- **Goal:** Build a basic web application that uses your chosen grouping method.
- **Instructions:**
  - Use a web framework (like Flask, Django, or FastAPI) to build the application.
  - Add your paragraph grouping method to the app.
  - Let users choose how many groups they want.
  - Show the names of the groups and how many claims each has.

## Setup Instructions

### Prerequisites
- Python 3.8 or later
- Git

### Clone the Repository
```bash
git clone https://github.com/Raztsook/ML.git
cd ML


### Create a Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

### Install the Requirements
```bash
pip install -r requirements.txt
```

### Running the Jupyter Notebook
1. Open Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Open `analysis.ipynb` and run the cells to see the experiments with different models for grouping paragraphs.

### Running the Web Application
1. Navigate to the application directory:
    ```bash
    cd app
    ```
2. Run the application:
    ```bash
    python app.py
    ```
3. Open your web browser and go to `http://127.0.0.1:5000` to interact with the application.

### Example Usage
To see the groups with a specific number of claims, you can use an endpoint like this:
```
http://127.0.0.1:5000/groups?number_of_groups=3
```

## Project Structure
```
ML - Task/
│
├── myenv/                   # Virtual environment directory
├── analysis.ipynb           # Jupyter notebook with research and analysis
├── app/
│   ├── app.py               # Main application file
│   ├── templates/
│   │   └── index.html       # HTML template for the web app
├── requirements.txt         # List of dependencies
├── README.md                # Project instructions and setup guide
└── .gitignore               # Git ignore file
```

## Python Version
This project was developed using Python 3.8.

## Evaluation Criteria

### Functionality
The application performs the following tasks as intended:
- Extracts text from patent claims.
- Groups patent claims into topics using various models.
- Provides an interactive tool for users to select the number of groups and view the results.

### Innovation
The methods used for grouping patent claims involve experimenting with different models, including clustering algorithms and text generation techniques. The selection of the best method is based on a thorough comparison, focusing on effectiveness and suitability for the task. The implementation of an interactive web application further demonstrates innovation by providing users with a flexible and user-friendly tool.

### Documentation
The project is well-documented with:
- A detailed README file that includes setup and running instructions.
- A Jupyter notebook (`analysis.ipynb`) that outlines the research and analysis conducted.
- Clear and concise comments within the code to explain the functionality.

### Note
The application's user interface is simple and text-based, as the focus is on functionality rather than UI design.

