import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Load tasks
tasks = pd.read_csv('small_mental_health_tasks.csv')

# Clean column names (replace spaces with underscores, lowercase)
tasks.columns = [col.strip().replace(' ', '_').lower()
                 for col in tasks.columns]

# Names list
names = ['Evelyn', 'Mia', 'Noah', 'Emma', 'Benjamin', 'Jack', 'Sofia', 'Nora', 'Mason', 'Leah',
         'Jackie', 'Charlotte', 'Samantha', 'Luna', 'Zoe', 'Henry', 'Gabriel', 'Hannah', 'Daniel',
         'Dessy', 'Layla', 'Olivia', 'Ruby', 'Luisa', 'Ella', 'Penelope', 'Ava', 'Aria', 'Matthew',
         'Alexander', 'Madison', 'Grayson', 'Zach', 'Sebastian', 'Amelia', 'Isabella', 'Chloe',
         'Harper', 'Levi', 'Ethan', 'Sarah', 'Aiden', 'Anna', 'Elijah', 'Ally', 'Aurora',
         'Victoria', 'Wyatt', 'Stella', 'Scarlett']

# Assign random authors
tasks['author'] = np.random.choice(names, size=len(tasks), replace=True)

# Ensure datetimes are correct format
tasks['created_at'] = pd.to_datetime(
    tasks['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')

# Save clean CSV
tasks.to_csv('small_mental_health_tasks_clean.csv', index=False)
