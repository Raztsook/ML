import joblib
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
import requests
from bs4 import BeautifulSoup

# Function to get patent claims
def get_patent_claims(patent_numbers):
    claims = []
    for patent_number in patent_numbers:
        url = f"https://patents.google.com/patent/{patent_number}/en"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        claim_elements = soup.find_all('div', {'class': 'claim'})
        claims.extend([claim.get_text(strip=True) for claim in claim_elements])
    return claims

# Load patent claims
patent_numbers = ['US20100238865A1', 'US20070178504A1', 'US20100029327A1']
claims = get_patent_claims(patent_numbers)

# Load pre-trained BERT model
bert_model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = bert_model.encode(claims)

# Train KMeans model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(embeddings)

# Save the KMeans model
joblib.dump(kmeans, 'kmeans_bert_model.pkl')
