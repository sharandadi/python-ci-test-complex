import numpy as np
import pandas as pd
import requests
import time
import sys

def complex_calculation():
    print("Starting complex calculation...")
    # Create a large random matrix
    matrix_a = np.random.rand(100, 100)
    matrix_b = np.random.rand(100, 100)
    
    # Compute dot product
    start_time = time.time()
    result = np.dot(matrix_a, matrix_b)
    end_time = time.time()
    
    print(f"Matrix multiplication completed in {end_time - start_time:.4f} seconds")
    print(f"Result shape: {result.shape}")
    print(f"Mean value: {np.mean(result)}")
    return result

def fetch_data():
    print("\nFetching data from public API...")
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Fetched {len(data)} items")
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def process_data(data):
    if not data:
        print("No data to process")
        return

    print("\nProcessing data with Pandas...")
    df = pd.DataFrame(data)
    
    # Analyze userId distribution
    user_counts = df['userId'].value_counts().sort_index()
    print("Posts per User ID (first 5):")
    print(user_counts.head())
    
    # Analyze title lengths
    df['title_length'] = df['title'].apply(len)
    avg_len = df['title_length'].mean()
    print(f"Average title length: {avg_len:.2f}")

def main():
    print("=== Complex Job Started ===")
    
    # CPU Bound Task
    complex_calculation()
    
    # IO Bound Task
    data = fetch_data()
    
    # Data Processing Task
    process_data(data)
    
    print("\n=== Complex Job Completed Successfully ===")
    sys.exit(0)

if __name__ == "__main__":
    main()
