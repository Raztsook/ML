import os
from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sentence_transformers import SentenceTransformer

# Set the environment variable to disable the tokenizers parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Initialize the Flask application
app = Flask(__name__)

# Load pre-trained SentenceTransformer model for generating embeddings
vectorizer = SentenceTransformer('all-MiniLM-L6-v2')

# Load previously saved embeddings and claims
embeddings = np.load('embeddings.npy')
with open('claims.txt', 'r') as f:
    claims = f.readlines()

# Function to generate cluster titles using LDA topic modeling
def get_cluster_titles_lda(claims, labels, n_clusters):
    cluster_titles = []
    for i in range(n_clusters):
        # Extract claims belonging to the current cluster
        cluster_claims = [claims[j] for j in range(len(claims)) if labels[j] == i]
        if len(cluster_claims) < 2:
            # Assign a default title if the cluster has too few documents
            cluster_titles.append(f"Cluster {i+1}")
            continue
        # Vectorize the claims in the current cluster
        count_vectorizer = CountVectorizer(max_df=0.85, min_df=1, stop_words='english')
        term_matrix = count_vectorizer.fit_transform(cluster_claims)
        # Apply LDA to find the most representative terms
        lda = LatentDirichletAllocation(n_components=1, random_state=42)
        lda.fit(term_matrix)
        terms = count_vectorizer.get_feature_names_out()
        topic_words = lda.components_[0]
        top_words_idx = topic_words.argsort()[-10:]
        top_words = [terms[idx] for idx in top_words_idx]
        # Create a title from the top words
        cluster_titles.append(" ".join(top_words))
    return cluster_titles

@app.route('/')
def home():
    # Render the home page with the input form
    return render_template('index.html')

@app.route('/group', methods=['POST'])
def group_claims():
    # Get the number of clusters requested by the user
    n_groups = int(request.form.get('groups'))
    
    # Fit KMeans with the requested number of clusters
    kmeans = KMeans(n_clusters=n_groups, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    
    # Count the number of claims in each cluster
    group_counts = np.bincount(labels)
    
    # Generate titles for each cluster using LDA
    cluster_titles = get_cluster_titles_lda(claims, labels, n_groups)
    
    # Create a response with cluster titles and claim counts
    response = {'groups': []}
    for i in range(n_groups):
        group_info = {
            'title': cluster_titles[i],
            'number_of_claims': int(group_counts[i])
        }
        response['groups'].append(group_info)
    
    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
