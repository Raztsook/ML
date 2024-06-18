from flask import Flask, request, jsonify, send_from_directory
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd 

app = Flask(__name__, static_folder='.', static_url_path='')

# Load pre-trained model
bert_model = SentenceTransformer('all-MiniLM-L6-v2')
kmeans_model = joblib.load('kmeans_bert_model.pkl')  # Ensure this is saved from your previous training

def get_patent_claims(patent_numbers):
    claims = []
    for patent_number in patent_numbers:
        url = f"https://patents.google.com/patent/{patent_number}/en"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        claim_elements = soup.find_all('div', {'class': 'claim'})
        claims.extend([claim.get_text(strip=True) for claim in claim_elements])
    return claims

def get_top_keywords(clusters, labels, n_terms):
    vectorizer = CountVectorizer(stop_words='english')
    vec_data = vectorizer.fit_transform(clusters)
    terms = vectorizer.get_feature_names_out()
    df = pd.DataFrame(vec_data.toarray(), columns=terms)
    
    top_keywords = {}
    for i in range(len(set(labels))):
        cluster_terms = df[labels == i].sum().sort_values(ascending=False)[:n_terms]
        top_keywords[i] = cluster_terms.index.tolist()
    
    return top_keywords

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/group_claims', methods=['GET'])
def group_claims():
    num_groups = int(request.args.get('groups', 3))
    patent_numbers = ['US20100238865A1', 'US20070178504A1', 'US20100029327A1']
    claims = get_patent_claims(patent_numbers)
    embeddings = bert_model.encode(claims)
    
    # Fit KMeans with the specified number of clusters
    kmeans_model.set_params(n_clusters=num_groups)
    labels = kmeans_model.fit_predict(embeddings)
    
    # Get top keywords for each cluster
    top_keywords = get_top_keywords(claims, labels, 3)  # Adjust the number of keywords as needed
    
    groups = {}
    for i in range(num_groups):
        groups[i] = {'title': ', '.join(top_keywords[i]), 'claims': []}
    
    for label, claim in zip(labels, claims):
        groups[label]['claims'].append(claim)
    
    response = [{'title': group['title'], 'number_of_claims': len(group['claims'])} for group in groups.values()]
    return jsonify({'groups': response})

if __name__ == '__main__':
    app.run(debug=True)
