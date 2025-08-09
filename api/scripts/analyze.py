import argparse, json
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--video", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    # TODO: call actual pipeline; write empty timeline for now
    timeline = {"video_id": Path(args.video).name, "fps": 30, "events": []}
    Path(args.out).write_text(json.dumps(timeline, indent=2))
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
