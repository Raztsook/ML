### README.md

# Patent Claims Clustering Project

## By
Raz Tsook

## Project Brief

This project focuses on extracting text from patent websites, comparing various clustering methods, and implementing the chosen model in a web application. Here is a step-by-step overview of the process:

1. **Extracting Patent Claims**:
   - I started by extracting the text of patent claims from Google Patents websites using web scraping techniques. This involved parsing the HTML content of the patent pages to retrieve the claims.

2. **Comparing Clustering Methods**:
   - I compared three different clustering methods:
     1. **KNN (K-Nearest Neighbors)**
     2. **LDA (Latent Dirichlet Allocation)**
     3. **BERT Embeddings with K-Means Clustering**
   - I analyzed the results of these methods to determine which provided the best clustering performance for my text data.

3. **Selecting the Best Model**:
   - Based on my analysis, I selected the **BERT Embeddings with K-Means Clustering** model as it provided the best results in terms of clustering performance.

4. **Preparing Files for the Application**:
   - After choosing the best model, I prepared the necessary files that would be used by the web application. This involved generating BERT embeddings for the patent claims and saving these embeddings and the claims to files.

5. **Implementing the Web Application**:
   - I uploaded the prepared files to Aplitzkia and created a web application using Flask. The application allows users to specify the number of clusters they want and provides meaningful titles for each cluster using LDA topic modeling.

This workflow ensures that I have a robust method for clustering patent claims and a user-friendly interface for interacting with the clustered data.

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
    cd ML - Task
    ```
2. Run the application:
    ```bash
    python app.py
    ```
3. Open your web browser and go to `http://127.0.0.1:5000` to interact with the application.

### Example Usage
To see the groups with a specific number of claims, you can use the input field on the main page of the web application. Enter the desired number of groups and click "Submit."

## Project Structure
```
ML - Task/
│
├── myenv/ # Virtual environment directory
├── .gitignore # Git ignore file
├── notebook.ipynb # Jupyter notebook for training the model and preparing data
├── app.py # Main application file
├── templates/ # Directory for HTML templates
│ └── index.html # HTML template for the web app
├── embeddings.npy # Numpy file with BERT embeddings for the claims
├── claims.txt # Text file with the extracted patent claims
├── README.md # Project instructions and setup guide
└── requirements.txt # List of dependencies

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

