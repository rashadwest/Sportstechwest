#!/usr/bin/env python3
"""
Full Integration: Vector Database Memory Management
Manages memory context using vector databases for semantic search.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
MEMORY_DIR = PROJECT_ROOT / "documents"

# Vector database configuration (supports Pinecone, Weaviate, Qdrant)
VECTOR_DB_TYPE = "file"  # Options: "file", "pinecone", "weaviate", "qdrant"

def store_memory_vector(memory_data_json: str) -> dict:
    """Store memory context as vector (file-based for now, can upgrade to Pinecone/Weaviate/Qdrant)."""
    try:
        # Parse memory data
        if isinstance(memory_data_json, str):
            try:
                memory_data = json.loads(memory_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', memory_data_json)
                if json_match:
                    memory_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            memory_data = memory_data_json
        
        results = {
            "status": "success",
            "vector_stored": False,
            "vector_id": None,
            "errors": []
        }
        
        # For now, use file-based storage (can upgrade to vector DB later)
        # Create semantic index file
        session_id = memory_data.get("sessionId") or f"session-{datetime.now().timestamp()}"
        vector_file = MEMORY_DIR / f"memory-vector-{session_id}.json"
        
        # Create vector representation (simplified - can use embeddings later)
        vector_data = {
            "id": session_id,
            "timestamp": datetime.now().isoformat(),
            "metadata": {
                "bookId": memory_data.get("bookId"),
                "prompt": memory_data.get("prompt", "")[:200],  # First 200 chars for search
                "systems": memory_data.get("systems", []),
                "updates": memory_data.get("updates", {})
            },
            "content": memory_data,
            "keywords": extract_keywords(memory_data)
        }
        
        # Save vector data
        vector_file.parent.mkdir(parents=True, exist_ok=True)
        vector_file.write_text(json.dumps(vector_data, indent=2), encoding='utf-8')
        
        results["vector_stored"] = True
        results["vector_id"] = session_id
        results["vector_file"] = str(vector_file)
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "vector_stored": False,
            "errors": [str(e)]
        }

def search_memory_vectors(query: str, limit: int = 5) -> dict:
    """Search memory vectors by semantic similarity (keyword matching for now)."""
    try:
        results = {
            "status": "success",
            "query": query,
            "matches": [],
            "errors": []
        }
        
        # Load all vector files
        vector_files = list(MEMORY_DIR.glob("memory-vector-*.json"))
        
        query_keywords = extract_keywords({"query": query})
        
        # Score each vector file
        scored_vectors = []
        for vector_file in vector_files:
            try:
                with open(vector_file, 'r', encoding='utf-8') as f:
                    vector_data = json.load(f)
                
                # Simple keyword matching (can upgrade to embeddings later)
                score = calculate_similarity(query_keywords, vector_data.get("keywords", []))
                
                if score > 0:
                    scored_vectors.append({
                        "score": score,
                        "vector_id": vector_data.get("id"),
                        "metadata": vector_data.get("metadata", {}),
                        "timestamp": vector_data.get("timestamp")
                    })
            except Exception as e:
                results["errors"].append(f"Error loading {vector_file}: {str(e)}")
        
        # Sort by score and return top matches
        scored_vectors.sort(key=lambda x: x["score"], reverse=True)
        results["matches"] = scored_vectors[:limit]
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "matches": [],
            "errors": [str(e)]
        }

def extract_keywords(data: Dict) -> List[str]:
    """Extract keywords from data for semantic search."""
    keywords = []
    
    # Extract from various fields
    if "prompt" in data:
        keywords.extend(data["prompt"].lower().split()[:10])
    if "bookId" in data:
        keywords.append(f"book{data['bookId']}")
    if "systems" in data:
        keywords.extend([s.lower() for s in data["systems"]])
    if "updates" in data:
        for update_type, updates in data["updates"].items():
            keywords.append(update_type.lower())
    
    return list(set(keywords))  # Remove duplicates

def calculate_similarity(query_keywords: List[str], vector_keywords: List[str]) -> float:
    """Calculate similarity score between query and vector keywords."""
    if not query_keywords or not vector_keywords:
        return 0.0
    
    # Simple intersection-based similarity
    intersection = set(query_keywords) & set(vector_keywords)
    union = set(query_keywords) | set(vector_keywords)
    
    if not union:
        return 0.0
    
    return len(intersection) / len(union)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Vector Database Memory Management")
    parser.add_argument("--store", help="Store memory vector (JSON string or file path)")
    parser.add_argument("--search", help="Search memory vectors by query")
    parser.add_argument("--limit", type=int, default=5, help="Limit search results")
    
    args = parser.parse_args()
    
    if args.store:
        # Store memory vector
        if Path(args.store).exists():
            input_json = Path(args.store).read_text(encoding='utf-8')
        else:
            input_json = args.store
        
        result = store_memory_vector(input_json)
        print(json.dumps(result, indent=2))
        
        if result.get("status") == "error":
            sys.exit(1)
    
    elif args.search:
        # Search memory vectors
        result = search_memory_vectors(args.search, args.limit)
        print(json.dumps(result, indent=2))
        
        if result.get("status") == "error":
            sys.exit(1)
    
    else:
        print("Usage: --store <json> or --search <query>")
        sys.exit(1)


