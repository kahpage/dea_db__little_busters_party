import sys
import json
from pathlib import Path
from typing import Any
import requests
from bs4 import BeautifulSoup
import lxml
import re
import unicodedata
from urllib.parse import urljoin, urlparse

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
    is_to_add,
)

PATH_EVENT = Path(__file__).parent
PATH_CIRCLES_JSON = PATH_EVENT / "circles.json"
NAME = PATH_EVENT.name
PATH_HELPER = PATH_EVENT.parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def sanitize_string(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[\s\n\t]+", " ", s)
    return s


def main():
    """Create circles.json"""
    print(f"Retrieving circles information for {NAME} ...")
    circles: list[Circle] = []

    # Manual, from https://web.archive.org/web/20261026195531/https://mattari-an.net/angelbeats/1st/kannai.pdf
    raw_circles: list[
        tuple[
            str,  # position
            str,  # circle_name
        ]
    ] = [
        ("A-01", "MerryCLOVER"),
        ("A-02", "ARI-COM"),
        ("B-01", "桃雪"),
        ("B-02", "やたや"),
        ("B-03", "WB+"),
        ("B-04", "ごったに"),
        ("C-01", "燈篭華"),
        ("C-02", "遠い海鳴りの音"),
        ("C-03", "箱庭のアリス"),
        ("C-04", "waterharbor"),
        ("C-05", "恋歌月姫"),
        ("C-06", "睦月屋臨時店舗"),
        ("C-07", "中央食堂"),
        ("C-08", "夢幻眠姫"),
        ("C-09", "dewdrops"),
        ("C-10", "Ease etc"),
        ("C-11", "しんきゃら"),
        ("C-12", "re-laive"),
        ("C-13", "月影広場"),
        ("C-14", "My Big Mistake"),
        ("D-01", "CyberCube"),
        ("D-02", "なんとかの線"),
        ("D-03", "雪月華音"),
        ("D-04", "桃缶"),
        ("D-05", "夕暮らね"),
        ("D-06", "狸工房"),
        ("D-07", "ゲキガンガーサークル"),
        ("D-08", "LOST VERMILLION"),
        ("D-09", "とろろのお宿"),
        ("D-10", "ひまわりランド"),
        ("D-11", "なんとなくの日常"),
        ("D-12", "ねこまんま"),
        ("D-13", "任務：『萌』世界征服！"),
        ("D-14", "はりけぇんみきさぁ"),
    ]

    for position, circle_name in raw_circles:
        circle = Circle(
            aliases=[circle_name],
            position=position,
        )
        circles.append(circle)

    # circles.sort(key=lambda c: c.position or "")

    # Save the extracted circle information to a JSON file
    with open(PATH_CIRCLES_JSON, "w", encoding="utf-8") as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=2)
    print(f"Saved {len(circles)} circles to {PATH_CIRCLES_JSON}")


if __name__ == "__main__":
    main()
