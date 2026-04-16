import json
import os
from typing import Any

import requests

BASE = "https://www.agenthansa.com/api"
API_KEY = os.environ["AGENTHANSA_API_KEY"]
MODEL_API_BASE = os.environ.get("MODEL_API_BASE", "https://api.openai.com/v1")
MODEL_API_KEY = os.environ.get("MODEL_API_KEY")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4.1-mini")

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {API_KEY}"})


def solve_with_model(payload: dict[str, Any]) -> str:
    if not MODEL_API_KEY:
        raise RuntimeError("MODEL_API_KEY is required for red-packet solving.")

    prompt = (
        "You are answering an AgentHansa red-packet challenge. "
        "Read the JSON and return only the final answer with no explanation.\n\n"
        f"{json.dumps(payload, ensure_ascii=False)}"
    )

    response = requests.post(
        f"{MODEL_API_BASE}/chat/completions",
        headers={
            "Authorization": f"Bearer {MODEL_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def post_checkin() -> None:
    response = session.post(f"{BASE}/agents/checkin", timeout=30)
    print("checkin:", response.status_code, response.text[:400])


def inspect_feed() -> None:
    response = session.get(f"{BASE}/agents/feed", timeout=30)
    response.raise_for_status()
    feed = response.json()
    print("feed summary:", json.dumps(feed.get("summary", {}), ensure_ascii=False))

    quests = feed.get("quests") or []
    if quests:
        print("top quest:", json.dumps(quests[0], ensure_ascii=False))

    urgent = feed.get("urgent") or []
    if urgent:
        print("urgent item:", json.dumps(urgent[0], ensure_ascii=False))


def join_active_red_packets() -> None:
    response = session.get(f"{BASE}/red-packets", timeout=30)
    response.raise_for_status()
    packets = response.json()
    active_packets = packets.get("active") or []

    if not active_packets:
        print("no active red packet; next at:", packets.get("next_packet_at"))
        return

    for packet in active_packets:
        packet_id = packet["id"]
        challenge = session.get(f"{BASE}/red-packets/{packet_id}/challenge", timeout=30)
        challenge.raise_for_status()
        challenge_payload = challenge.json()
        answer = solve_with_model(challenge_payload)
        join = session.post(
            f"{BASE}/red-packets/{packet_id}/join",
            json={"answer": answer},
            timeout=30,
        )
        print("joined red packet:", packet_id, join.status_code, join.text[:400])


def list_open_quests() -> None:
    response = session.get(f"{BASE}/alliance-war/quests?per_page=20", timeout=30)
    response.raise_for_status()
    quests = response.json().get("quests", [])
    open_quests = [q for q in quests if q.get("status") == "open"]
    print("open quests:", len(open_quests))
    for quest in open_quests[:5]:
        print("-", quest["id"], "|", quest["title"])


if __name__ == "__main__":
    post_checkin()
    inspect_feed()
    join_active_red_packets()
    list_open_quests()
