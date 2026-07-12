import math
from typing import Optional
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY

# City centroids for the corpus cities. Used to tag chunks at ingestion
# time deterministically (zero API calls, fully reproducible) — the chunk's
# city is already known from its docs/ subfolder. LLM-based extraction
# (below) is reserved for query time, where the location is not known.
CITY_CENTROIDS = {
    "bristol":     (51.4545, -2.5879),
    "london":      (51.5074, -0.1278),
    "birmingham":  (52.4862, -1.8904),
    "leeds":       (53.8008, -1.5491),
    "liverpool":   (53.4084, -2.9916),
    "sheffield":   (53.3811, -1.4701),
    "newcastle":   (54.9783, -1.6178),
    "nottingham":  (52.9548, -1.1581),
    "leicester":   (52.6369, -1.1398),
    "southampton": (50.9097, -1.4044),
    "plymouth":    (50.3755, -4.1427),
    # "national" documents (NPPF) have no location — no entry on purpose
}

class LocationMetadata(BaseModel):
    """Pydantic model for LLM structured output of spatial entities"""
    location_name: Optional[str] = Field(None, description="The primary geographic location (e.g. city, neighbourhood) mentioned.")
    lat: Optional[float] = Field(None, description="Approximate latitude of the location in decimal degrees.")
    lon: Optional[float] = Field(None, description="Approximate longitude of the location in decimal degrees.")

_spatial_llm = None

def get_spatial_llm():
    global _spatial_llm
    if _spatial_llm is None:
        # We always use a cheap/fast model for extraction regardless of config
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
        _spatial_llm = llm.with_structured_output(LocationMetadata)
    return _spatial_llm

def extract_spatial_metadata(text: str) -> LocationMetadata:
    """Extract location and coordinates from text using an LLM."""
    llm = get_spatial_llm()
    prompt = (
        "Analyze the following text and extract the primary geographic location (e.g., city, neighbourhood, or specific site) if one is mentioned. "
        "Provide its approximate latitude and longitude coordinates. "
        "IMPORTANT: If the text discusses general policy (e.g. national guidelines, generic definitions) and DOES NOT refer to a specific geographic place, return null for all fields. "
        f"Text:\n{text[:1500]}"
    )
    try:
        res = llm.invoke(prompt)
        if res and res.lat == 0.0 and res.lon == 0.0:
            return LocationMetadata()
        return res or LocationMetadata()
    except Exception as e:
        print(f"Spatial extraction error: {e}")
        return LocationMetadata()

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great circle distance between two points on the earth in km."""
    if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
        return float('inf')
        
    R = 6371.0 # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
