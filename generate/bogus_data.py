"""Generate a CSV with a whole bunch of bogus data to be uploaded into supabase"""

from itertools import product 
import pandas as pd
import random

user_ids = [
    "566cd376-d620-40fa-8e7f-61111e8c29af",
    "f67adcd4-4fbb-423d-8107-61e373185f48",
    "ca378a36-bb9e-47a0-9af3-0a89ae53832f",
    "9eb5408c-08fe-465d-9ac0-baaa8c31c425",
    "fe2e6586-55b5-4deb-9294-375e0cae411a",
    "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
    "4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9d",
    "5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9d0e",
    "3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f",
    "19c2f059-ad95-4616-97bd-1b483fda15af",
    "fdefb20a-afdb-44e3-a62d-754aab937ff2",
    "99f82544-95b3-453e-9ed0-66897d4a7bb2",
    "2850ab49-c636-4c9f-bbf1-91e0f1685eff",
    "6970e598-d058-456d-91bd-e394502b8b7c",
    "c9bd4c67-7937-4ee3-959d-21a1b3db70eb",
    "8d245124-6baa-48e3-8f20-ce125d5c22b7"
]
review_ids = [i for i in range(154, 181)]

num_rows = 100

cross_product = list(product(user_ids, review_ids))
selected = random.sample(cross_product, 100)

data = {
    'user_id': [],
    'review_id': [],
    'upvote': []
}

for row in selected: 
    user, review = row
    upvote = random.choice(["TRUE", "FALSE"])
    data['user_id'].append(user)
    data['review_id'].append(review)
    data['upvote'].append(upvote)

df = pd.DataFrame(data)
df.to_csv('generate/generate_data.csv', index=False)