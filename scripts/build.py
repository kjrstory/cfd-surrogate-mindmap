#!/usr/bin/env python3
import csv, json
from pathlib import Path

# 1) 입력·출력 파일 경로 정의
BASE = Path(__file__).parent.parent
INPUT_CSV  = BASE / "public/assets/data.csv"
OUTPUT_JSON = BASE / "public/assets/data.json"

# 2) CSV 행을 트리 형태로 변환하는 함수
def make_tree(rows):
    tree = {}
    for row in rows:
        bb = row["Backbone"]
        gt = row["GridType"]
        method = row["Method"]
        # 중첩된 dict에 기본값 생성
        tree.setdefault(bb, {}).setdefault(gt, {})[method] = {
            "year": int(row["Year"]),
            "source": row["Source"],
            "scenario": row["Scenario"].split(";"),
            "doi": row["DOI"] or None,
            "codeUrl": row["CodeURL"] or None
        }
    return tree

def main():
    # 3) CSV 읽기
    with open(INPUT_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # 4) 트리 생성
    hierarchy = make_tree(rows)

    # 5) JSON으로 저장
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(hierarchy, f, ensure_ascii=False, indent=2)

    print("✅ data.json이 생성되었습니다:", OUTPUT_JSON)

if __name__ == "__main__":
    main()
