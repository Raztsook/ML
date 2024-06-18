from flask import Flask, request, jsonify, send_from_directory
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__, static_folder='.', static_url_path='')

# Load pre-trained model
bert_model = SentenceTransformer('all-MiniLM-L6-v2')
kmeans_model = joblib.load('kmeans_bert_model.pkl')  # Ensure this is saved from your previous training

def get_patent_claims(patent_number):
    url = f"https://patents.google.com/patent/{patent_number}/en"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page for {patent_number}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the claims section by looking for divs with the class 'claim'
    claims_section = soup.find('section', {'itemprop': 'claims'})

    if not claims_section:
        print(f"No claims section found for {patent_number}")
        return []

    # Extract the text of each claim inside the 'claim-text' divs
    claims_text = []
    for claim in claims_section.find_all('div', class_='claim'):
        claim_text_div = claim.find('div', class_='claim-text')
        if claim_text_div:
            claims_text.append(claim_text_div.get_text(separator=' ', strip=True))

    return claims_text

def get_top_keywords(clusters, labels, n_terms):
    vectorizer = TfidfVectorizer(stop_words='english')
    vec_data = vectorizer.fit_transform(clusters)
    terms = vectorizer.get_feature_names_out()
    
    df = pd.DataFrame(vec_data.toarray(), columns=terms)
    
    top_keywords = {}
    
    for i in range(len(set(labels))):
        cluster_terms = df.iloc[labels == i].sum().sort_values(ascending=False).head(n_terms)
        top_keywords[i] = cluster_terms.index.tolist()
    
    return top_keywords

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/group_claims', methods=['GET'])
def group_claims():
    num_groups = int(request.args.get('groups', 3))
    patent_numbers = ['GB2478972A', 'US9634864B2', 'US9980046B2']
    all_claims = []

    for patent_number in patent_numbers:
        claims = get_patent_claims(patent_number)
        all_claims.extend(claims)

    embeddings = bert_model.encode(all_claims)
    
    # Fit KMeans with the specified number of clusters
    kmeans_model.set_params(n_clusters=num_groups)
    labels = kmeans_model.fit_predict(embeddings)
    
    # Get top keywords for each cluster
    top_keywords = get_top_keywords(all_claims, labels, 1)  # Adjust the number of keywords as needed
    
    groups = {}
    for i in range(num_groups):
        groups[i] = {'title': ', '.join(top_keywords[i]), 'claims': []}
    
    for label, claim in zip(labels, all_claims):
        groups[label]['claims'].append(claim)
    
    response = [{'title': group['title'], 'number_of_claims': len(group['claims'])} for group in groups.values()]
    return jsonify({'groups': response})

if __name__ == '__main__':
    app.run(debug=True)
