# test.py
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

try:
    # Test basic import
    print("✅ Import successful!")
    
    # Test API key
    api_key = os.getenv("SERP_API_KEY")
    if api_key:
        print("✅ API key found!")
        
        # Test simple search (not flights, just to verify API works)
        search = GoogleSearch({
            "q": "coffee",
            "api_key": api_key
        })
        
        results = search.get_dict()
        
        if "error" in results:
            print(f"❌ API Error: {results['error']}")
        else:
            print("✅ API connection successful!")
            
    else:
        print("❌ API key not found - check your .env file")
        
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("Run: pip install google-search-results python-dotenv")
except Exception as e:
    print(f"⚠️ Other error: {e}")