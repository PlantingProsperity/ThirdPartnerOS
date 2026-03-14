"""
Partner OS — GenAI Client Factory
=================================

**Principal's Summary:**
This is the system's "Communications Hub" for talking to Google's AI models. 
It securely handles the credentials (keys) needed to use the Gemini AI, ensuring 
that all agents can talk to the brain securely and reliably.

**Integration Note:**
Centralized initialization for the Google GenAI SDK.
Supports both OAuth (ADC) and API Key authentication. Used by the Embedder 
and Retriever to interact with Google's text-embedding-004 model.
"""

import os
from google import genai
from google.genai import types
import google.auth
from google.auth.exceptions import DefaultCredentialsError
from src.utils.logger import get_logger

log = get_logger(__name__)

def get_genai_client() -> genai.Client:
    """
    Returns an initialized Gemini Client.
    Prioritizes GOOGLE_API_KEY from environment, fallbacks to OAuth (ADC).
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    http_options = types.HttpOptions(api_version="v1beta")
    
    if api_key:
        log.debug("Initializing Gemini Client using API Key.")
        return genai.Client(api_key=api_key, http_options=http_options)
    
    try:
        log.debug("Attempting to initialize Gemini Client using OAuth (ADC).")
        credentials, _ = google.auth.default()
        return genai.Client(credentials=credentials, http_options=http_options)
    except DefaultCredentialsError:
        log.warning("No Application Default Credentials found. Attempting unauthenticated client.")
        return genai.Client(http_options=http_options)
    except Exception as e:
        log.error(f"Failed to initialize Gemini Client: {e}")
        raise
