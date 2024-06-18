import joblib
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
import requests
from bs4 import BeautifulSoup

# Function to get patent claims
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

# Load patent claims
patent_numbers = ['GB2478972A', 'US9634864B2', 'US9980046B2']
all_claims = []

for patent_number in patent_numbers:
    claims = get_patent_claims(patent_number)
    print(f"Extracted {len(claims)} claims for {patent_number}")
    all_claims.extend(claims)

# Load pre-trained BERT model
bert_model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = bert_model.encode(all_claims)

# Train KMeans model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(embeddings)

# Save the KMeans model
joblib.dump(kmeans, 'kmeans_bert_model.pkl')

print(f"Extracted {len(all_claims)} claims.")
print("KMeans model trained and saved successfully.")
