# spatial_ablation.py
# ─────────────────────────────────────────────────────────────
# Isolates the contribution of the spatial re-ranking component.
#
# For every task that targets a city, retrieval is run two ways over the
# SAME vector index:
#   (a) semantic-only  : plain top-K cosine similarity (spatial re-ranking OFF)
#   (b) spatial        : over-fetch, then boost chunks within 15km of the task
#                        city's centroid, then take top-K (spatial re-ranking ON)
# We measure how often the retrieved context comes from the task's OWN city.
# This is a controlled ablation (identical query, index and anchor), so any
# difference is attributable to the spatial component alone. No LLM generation
# is required, so it is cheap and fully reproducible.
#
# Usage: python spatial_ablation.py
# ─────────────────────────────────────────────────────────────

import json
from collections import defaultdict

from config import TASKS_FILE, TOP_K, RESULTS_DIR
from rag_pipeline import get_vectorstore, _similarity_search_filtered
from spatial import CITY_CENTROIDS, haversine_distance


def own_city_rate(chunks, city):
    if not chunks:
        return 0.0
    return sum(1 for c in chunks if c == city) / len(chunks)


def semantic_topk(vs, query):
    raw = _similarity_search_filtered(vs, query, TOP_K)
    return [d.metadata.get("city") for d, _ in raw]


def spatial_topk(vs, query, city):
    lat, lon = CITY_CENTROIDS[city]
    raw = _similarity_search_filtered(vs, query, TOP_K * 4)
    scored = []
    for d, score in raw:
        sim = 1.0 / (1.0 + score)
        clat, clon = d.metadata.get("lat"), d.metadata.get("lon")
        boost = 0.0
        if clat is not None and clon is not None:
            dist = haversine_distance(lat, lon, clat, clon)
            if dist <= 15:
                boost = max(0, 0.15 * (1 - dist / 15))
        scored.append((d.metadata.get("city"), sim + boost))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [c for c, _ in scored[:TOP_K]]


def main():
    tasks = json.load(open(TASKS_FILE))
    vs = get_vectorstore()

    per_city = defaultdict(lambda: {"sem": [], "spa": [], "n": 0})
    overall = {"sem": [], "spa": []}

    tasks = [t for t in tasks if t.get("city") and t["city"] in CITY_CENTROIDS]
    for i, t in enumerate(tasks, 1):
        city = t["city"]
        q = t["task"]
        sem = own_city_rate(semantic_topk(vs, q), city)
        spa = own_city_rate(spatial_topk(vs, q, city), city)
        per_city[city]["sem"].append(sem)
        per_city[city]["spa"].append(spa)
        per_city[city]["n"] += 1
        overall["sem"].append(sem)
        overall["spa"].append(spa)
        print(f"[{i}/{len(tasks)}] {t['id']:12} own-city retrieval  semantic={sem:.0%}  spatial={spa:.0%}")

    def mean(xs):
        return sum(xs) / len(xs) if xs else 0.0

    lines = ["# Spatial Re-ranking Ablation\n",
             "Own-city retrieval rate: share of the top-8 retrieved chunks that come "
             "from the task's own authority. Higher is better.\n",
             "| City | n | Semantic-only | Spatial re-ranked | Gain |",
             "|---|---|---|---|---|"]
    for city in sorted(per_city):
        v = per_city[city]
        s, p = mean(v["sem"]), mean(v["spa"])
        lines.append(f"| {city} | {v['n']} | {s:.1%} | {p:.1%} | {p-s:+.1%} |")
    s, p = mean(overall["sem"]), mean(overall["spa"])
    lines.append(f"| **all** | {len(overall['sem'])} | **{s:.1%}** | **{p:.1%}** | **{p-s:+.1%}** |")

    out = RESULTS_DIR / "spatial_ablation.md"
    out.write_text("\n".join(lines) + "\n")
    print("\n" + "\n".join(lines))
    print(f"\nWritten to {out}")


if __name__ == "__main__":
    main()
