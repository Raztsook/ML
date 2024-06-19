### README.md

# Patent Claims Clustering Project

## By
Raz Tsook

## Description
This project extracts text from patent websites, compares clustering methods, and provides an application to group patent claims.

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

## Installation Steps

1. **Clone the repository**

    ```sh
    git clone https://github.com/Raztsook/ML.git
    cd ML
    ```

2. **Create and activate a virtual environment**

    ```sh
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**

    ```sh
    python app.py
    ```

## Running the Application

After completing the above steps, you can run the application by navigating to the project directory and executing the following command:

```sh
python app.py


### Example Usage
To see the groups with a specific number of claims, you can use the input field on the main page of the web application. Enter the desired number of groups and click "Submit."


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
- A Jupyter notebook (`notebook.ipynb`) that outlines the research and analysis conducted.
- Clear and concise comments within the code to explain the functionality.

### Note
The application's user interface is simple and text-based, as the focus is on functionality rather than UI design.

