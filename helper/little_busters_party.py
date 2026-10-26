# Notes:
import sys
import json
from pathlib import Path
from typing import Any

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
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== little_busters_party1 ====
    if i not in disabled_events:
        event_name = f"little_busters_party{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_i-img847x1200-17275155153015jfi3gh1085811.jpg",
                [
                    Source(
                        "https://auctions.yahoo.co.jp/jp/auction/d1154678647",
                        (RT.Likely, OT.External),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館 ６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20080505103355/http://mattari-an.net/littlebusters/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=[
                "リトバスパーティー",
                "Little Busters Party",
                "リトバスパーティー1",
                "Little Busters Party1",
            ],
            dates="2008.09.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20080505103355/http://mattari-an.net/littlebusters/index.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20090131045854/http://mattari-an.net/littlebusters/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            comments="Blog post mentioning the event: https://web.archive.org/web/20250831083609/http://innocent-dreamer.net/2008/09/post_482.html",
            last_edited="2026.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== little_busters_party2 ====
    if i not in disabled_events:
        event_name = f"little_busters_party{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_i-img847x1200-17275155153022eiwi811085078.jpg",
                [
                    Source(
                        "https://auctions.yahoo.co.jp/jp/auction/d1154678647",
                        (RT.Likely, OT.External),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館 ６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20090622072838/http://mattari-an.net/littlebusters/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["リトバスパーティー2", "Little Busters Party 2"],
            dates="2009.09.13",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20090622072838/http://mattari-an.net/littlebusters/index.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20100114003824/http://mattari-an.net/littlebusters/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== little_busters_party3 ====
    if i not in disabled_events:
        event_name = f"little_busters_party{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_d744d604.jpg",
                [
                    Source(
                        "http://blog.livedoor.jp/nagoya_repo/archives/51481804.html",
                        (RT.Likely, OT.External),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館 ６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20100909071009/http://mattari-an.net/littlebusters/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["リトバスパーティー3", "Little Busters Party 3"],
            dates="2010.09.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20100909071009/http://mattari-an.net/littlebusters/index.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20261026195531/https://mattari-an.net/angelbeats/1st/kannai.pdf",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with AB即売会戦線",
            comments="Blog post mentioning the event: http://www.i-love-key.net/archives/2010/09/litpa_ab_repo.html",
            last_edited="2026.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== little_busters_party4 ====
    if i not in disabled_events:
        event_name = f"little_busters_party{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "04_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20110917022631/http://mattari-an.net/littlebusters/index.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：神楽七姫 様（Navy Blue）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.01365, 135.7809429),
                address="9-1 Okazaki Seishojicho, Sakyo Ward, Kyoto, 606-8343, Japan",
                description="京都市勧業館　みやこめっせ　３階 第３展示場Ａ面",
                sources=[
                    Source(
                        "https://web.archive.org/web/20110917022631/http://mattari-an.net/littlebusters/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlur6oWztq77DaOuTZLw5MRyj3iDVD1CD-wl9_7wkEXC7e9JYhls5YX8XY6_936CE_RWP6CozLolZI73Mh7gleO-PgU9DJro4VpNaq7nQSPaHd9rChZ-VVge7urD47mbsVOMZ6B-A=s870-k-no",
                url="https://maps.app.goo.gl/8MjxYFEFKBxjhyTT8",
            ),
        ]
        event = Event(
            aliases=["リトバスパーティー4", "Little Busters Party 4"],
            dates="2011.03.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20110917022631/http://mattari-an.net/littlebusters/index.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20110831112014/http://mattari-an.net/littlebusters/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with AB即売会戦線2 and Keyパーティー",
            # comments=None,
            last_edited="2026.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "R"  # ==== little_busters_partyR ====
    if i not in disabled_events:
        event_name = f"little_busters_party{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "R_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130213202247/http://mattari-an.net/littlebusters/index.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="表紙絵提供：たくみ 様（くろたま）",
            ),
            Medium(
                "R_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20130212182116/http://mattari-an.net/littlebusters/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.01365, 135.7809429),
                address="9-1 Okazaki Seishojicho, Sakyo Ward, Kyoto, 606-8343, Japan",
                description="京都市勧業館 みやこめっせ　３階 第３展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130213202247/http://mattari-an.net/littlebusters/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlur6oWztq77DaOuTZLw5MRyj3iDVD1CD-wl9_7wkEXC7e9JYhls5YX8XY6_936CE_RWP6CozLolZI73Mh7gleO-PgU9DJro4VpNaq7nQSPaHd9rChZ-VVge7urD47mbsVOMZ6B-A=s870-k-no",
                url="https://maps.app.goo.gl/8MjxYFEFKBxjhyTT8",
            ),
        ]
        event = Event(
            aliases=["リトバスパーティーR", "Little Busters Party R"],
            dates="2013.03.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130213202247/http://mattari-an.net/littlebusters/index.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20260511000444/http://mattari-an.net/littlebusters/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== little_busters_party ====
    # if i not in disabled_events:
    #     event_name = f"little_busters_party{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=,
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="2026.10.26",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = ["https://mattari-an.net/littlebusters/index.html", "https://x.com/key_party_abss"]

    event_group = EventGroup(
        aliases=["リトバスパーティー", "Little Busters Party"],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                'Alias transliteration "Little Busters Party", best I could find.',
                (ReliabilityTypes.Guess, OriginTypes.Unsourced),
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.26",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
