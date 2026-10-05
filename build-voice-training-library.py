#!/usr/bin/env python3
"""
build-voice-training-library.py
Builds the machine-readable voice-training-library.json and voice-rule-matching-matrix.json
from Documents/Articles / Docs/Voice-Training-Library markdown files for Pitchee iOS App integration.
"""

import os
import re
import json
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STANDALONE_ARTICLES_DIR = "/Users/dannyfeng/Documents/Articles"
LOCAL_DOCS_DIR = os.path.join(REPO_ROOT, "Docs", "Voice-Training-Library")

DOCS_CANDIDATES = [
    STANDALONE_ARTICLES_DIR,
    LOCAL_DOCS_DIR,
    os.path.join(REPO_ROOT, "Dependencies", "Articles")
]

LIBRARY_DOCS_DIR = None
for cand in DOCS_CANDIDATES:
    if os.path.exists(cand) and len(glob.glob(os.path.join(cand, "**", "*.md"), recursive=True)) == 49:
        LIBRARY_DOCS_DIR = cand
        break

if not LIBRARY_DOCS_DIR:
    LIBRARY_DOCS_DIR = LOCAL_DOCS_DIR

RESOURCES_DIR = os.path.join(REPO_ROOT, "Resources", "VoiceTrainingLibrary")
os.makedirs(RESOURCES_DIR, exist_ok=True)

SECTION_ICON_MAP = {
    "一、声学机制与算法原理": "gearshape.2.fill",
    "二、症状自查与代偿排查": "stethoscope",
    "三、训练动作与实操指南": "figure.run",
    "四、权威文献与延伸参考": "books.vertical.fill"
}

def icon_for_heading(heading):
    if heading in SECTION_ICON_MAP:
        return SECTION_ICON_MAP[heading]
    if "机制" in heading or "原理" in heading:
        return "gearshape.2.fill"
    if "自查" in heading or "排查" in heading or "症状" in heading:
        return "stethoscope"
    if "训练" in heading or "动作" in heading or "实操" in heading or "指南" in heading:
        return "figure.run"
    if "文献" in heading or "参考" in heading or "循证" in heading:
        return "books.vertical.fill"
    return "doc.text.fill"

def parse_markdown(filepath):
    rel_path = os.path.relpath(filepath, LIBRARY_DOCS_DIR)
    folder = os.path.dirname(rel_path)
    filename = os.path.basename(rel_path)
    
    # Extract ID ending with two digits before Chinese/descriptive slug
    id_match = re.match(r"^([A-Z0-9\-]+?-\d{2})-(.*)\.md$", filename)
    if id_match:
        full_id = id_match.group(1)
        slug = id_match.group(2)
    else:
        full_id = filename.replace(".md", "")
        slug = full_id

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Extract all metadata bullet points in header
    meta = {}
    for line in lines[:25]:
        m = re.match(r"^\s*[-*]\s*\*\*([^*]+)\*\*[:：]\s*(.*)$", line.strip())
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()

    summary = (
        meta.get("适用场景") or 
        meta.get("推荐场景") or 
        meta.get("适用周期") or 
        meta.get("核心场景") or 
        title
    )

    user_persona = (
        meta.get("用户困惑") or 
        meta.get("阶段痛点") or 
        meta.get("用户画像") or 
        meta.get("生理现状") or 
        meta.get("常见症状") or 
        meta.get("心理反应") or 
        meta.get("心理现状") or 
        meta.get("用户痛点") or 
        meta.get("阶段特征") or 
        meta.get("能力瓶颈") or 
        meta.get("心理根源") or 
        meta.get("核心成因") or 
        meta.get("声学机制") or 
        meta.get("生理机制") or 
        meta.get("医学诊断") or 
        meta.get("危险动作") or 
        meta.get("声学原理") or 
        meta.get("声学概念") or 
        meta.get("声学混淆") or 
        meta.get("声学失衡") or 
        meta.get("工程定位") or 
        meta.get("物理现象") or 
        meta.get("临床基础") or 
        meta.get("理论来源") or 
        meta.get("专业角色") or 
        meta.get("医学铁律") or 
        meta.get("医学概念") or 
        meta.get("语言学概念") or 
        meta.get("社会语言学事实") or 
        meta.get("运动生理学法则") or 
        meta.get("生理概念") or 
        meta.get("系统逻辑") or 
        meta.get("算法契约") or 
        meta.get("用户目标") or 
        meta.get("阶段目标") or 
        meta.get("核心文献依据") or 
        meta.get("推荐工具") or 
        meta.get("核心认知") or 
        meta.get("核心概念") or 
        meta.get("适用场景") or 
        ""
    )

    core_goal = (
        meta.get("核心目标") or 
        meta.get("阶段目标") or 
        meta.get("核心诊断") or 
        meta.get("核心认知") or 
        meta.get("科学真相") or 
        meta.get("核心概念") or 
        meta.get("医学诊断") or 
        meta.get("用户目标") or 
        meta.get("医学铁律") or 
        meta.get("声学机制") or 
        meta.get("声学失衡") or 
        meta.get("系统逻辑") or 
        meta.get("行为契约") or 
        ""
    )

    # Determine tags and matching conditions
    matched_rules = []
    target_preferences = ["feminine", "masculine", "undecided"]
    min_score = 0
    max_score = 100

    if "RULE-PASS-BOOST" in filename:
        matched_rules = ["pass_boost"]
        target_preferences = ["feminine"]
        min_score = 80
        max_score = 100
    elif "RULE-HIGH-F0-STYLIZED" in filename:
        matched_rules = ["high_f0_stylized_cap"]
        target_preferences = ["feminine"]
        min_score = 0
        max_score = 30
    elif "RULE-HIGH-F0-MALE" in filename:
        matched_rules = ["high_f0_male_cap"]
        target_preferences = ["feminine"]
        min_score = 30
        max_score = 59
    elif "RULE-LOW-F0-NATURAL" in filename:
        matched_rules = ["low_f0_natural_cap"]
        target_preferences = ["feminine"]
        min_score = 40
        max_score = 59
    elif "RULE-LOW-F0-STYLIZED" in filename:
        matched_rules = ["low_f0_stylized_cap"]
        target_preferences = ["feminine"]
        min_score = 0
        max_score = 20
    elif "RULE-F0-UNAVAILABLE" in filename:
        matched_rules = ["f0_unavailable"]
        target_preferences = ["feminine", "masculine", "undecided"]
    elif "RULE-CONTINUOUS" in filename:
        matched_rules = ["continuous"]
        target_preferences = ["feminine", "masculine", "undecided"]
    elif "SCORE-STARTER" in filename:
        min_score = 0
        max_score = 49
        target_preferences = ["feminine"]
        matched_rules = ["continuous"]
    elif "SCORE-MID" in filename:
        min_score = 50
        max_score = 74
        target_preferences = ["feminine"]
        matched_rules = ["continuous"]
    elif "SCORE-ADVANCED" in filename:
        min_score = 75
        max_score = 89
        target_preferences = ["feminine"]
        matched_rules = ["continuous"]
    elif "SCORE-MASTER" in filename:
        min_score = 90
        max_score = 100
        target_preferences = ["feminine"]
        matched_rules = ["continuous"]
    elif "MASCULINE" in filename:
        target_preferences = ["masculine"]
        matched_rules = ["continuous", "masculine"]
    elif "NONBINARY" in filename:
        target_preferences = ["undecided"]
        matched_rules = ["continuous", "nonbinary"]
    elif "PRACTICE-AB" in filename:
        target_preferences = ["feminine", "masculine", "undecided"]
        matched_rules = ["guided_practice"]
    elif "QUALITY" in filename or "METRIC-DURATION" in filename:
        target_preferences = ["feminine", "masculine", "undecided"]
        matched_rules = ["quality"]
    elif "HEALTH" in filename:
        target_preferences = ["feminine", "masculine", "undecided"]
        matched_rules = ["health_clinical"]
    elif "METRIC" in filename:
        target_preferences = ["feminine", "masculine", "undecided"]
        matched_rules = ["acoustic_dimensions"]

    # Extract sections
    sections = []
    current_sec = None
    for line in lines:
        if line.startswith("## "):
            if current_sec:
                sections.append(current_sec)
            heading_text = line[3:].strip()
            current_sec = {"heading": heading_text, "content": []}
        elif current_sec:
            current_sec["content"].append(line)
    if current_sec:
        sections.append(current_sec)

    clean_sections = []
    for s in sections:
        clean_sections.append({
            "heading": s["heading"],
            "icon": icon_for_heading(s["heading"]),
            "body": "\n".join(s["content"]).strip()
        })

    return {
        "id": full_id,
        "title": title,
        "category": folder,
        "filename": filename,
        "summary": summary,
        "userPersona": user_persona,
        "coreGoal": core_goal,
        "matchedRules": matched_rules,
        "targetPreferences": target_preferences,
        "scoreRange": {"min": min_score, "max": max_score},
        "sections": clean_sections,
        "rawContent": content
    }

def main():
    md_files = sorted(glob.glob(os.path.join(LIBRARY_DOCS_DIR, "**", "*.md"), recursive=True))
    articles = []
    for f in md_files:
        articles.append(parse_markdown(f))

    print(f"Parsed {len(articles)} articles from {LIBRARY_DOCS_DIR}.")

    output_payload = {
        "schemaVersion": "1.0.0",
        "generatedAt": "2026-10-05T02:30:00Z",
        "description": "Pitchee iOS App Embedded Voice Training Text Resource Library",
        "totalArticles": len(articles),
        "articles": articles
    }

    # Write structured library to Resources/VoiceTrainingLibrary
    lib_path = os.path.join(RESOURCES_DIR, "voice-training-library.json")
    with open(lib_path, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote structured library to {lib_path}")

    # Build rule matching matrix
    rule_matrix = {
        "pass_boost": [a["id"] for a in articles if "pass_boost" in a["matchedRules"]],
        "high_f0_stylized_cap": [a["id"] for a in articles if "high_f0_stylized_cap" in a["matchedRules"]],
        "high_f0_male_cap": [a["id"] for a in articles if "high_f0_male_cap" in a["matchedRules"]],
        "low_f0_natural_cap": [a["id"] for a in articles if "low_f0_natural_cap" in a["matchedRules"]],
        "low_f0_stylized_cap": [a["id"] for a in articles if "low_f0_stylized_cap" in a["matchedRules"]],
        "f0_unavailable": [a["id"] for a in articles if "f0_unavailable" in a["matchedRules"]],
        "continuous": [a["id"] for a in articles if "continuous" in a["matchedRules"]],
        "score_starter": [a["id"] for a in articles if a["id"].startswith("SCORE-STARTER")],
        "score_mid": [a["id"] for a in articles if a["id"].startswith("SCORE-MID")],
        "score_advanced": [a["id"] for a in articles if a["id"].startswith("SCORE-ADVANCED")],
        "score_master": [a["id"] for a in articles if a["id"].startswith("SCORE-MASTER")],
        "masculine_specialization": [a["id"] for a in articles if a["targetPreferences"] == ["masculine"]],
        "nonbinary_exploration": [a["id"] for a in articles if a["targetPreferences"] == ["undecided"]],
        "guided_practice": [a["id"] for a in articles if a["id"].startswith("PRACTICE-AB")],
        "recording_quality": [a["id"] for a in articles if a["id"].startswith("QUALITY") or a["id"].startswith("METRIC-DURATION")],
        "health_safety": [a["id"] for a in articles if a["id"].startswith("HEALTH")],
        "acoustic_metrics": [a["id"] for a in articles if a["id"].startswith("METRIC")]
    }

    matrix_path = os.path.join(RESOURCES_DIR, "voice-rule-matching-matrix.json")
    with open(matrix_path, "w", encoding="utf-8") as f:
        json.dump(rule_matrix, f, ensure_ascii=False, indent=2)
    print(f"Wrote matching matrix to {matrix_path}")

    # Also write to standalone Articles directory if it exists
    if os.path.exists(STANDALONE_ARTICLES_DIR):
        standalone_lib_path = os.path.join(STANDALONE_ARTICLES_DIR, "voice-training-library.json")
        with open(standalone_lib_path, "w", encoding="utf-8") as f:
            json.dump(output_payload, f, ensure_ascii=False, indent=2)
        standalone_mat_path = os.path.join(STANDALONE_ARTICLES_DIR, "voice-rule-matching-matrix.json")
        with open(standalone_mat_path, "w", encoding="utf-8") as f:
            json.dump(rule_matrix, f, ensure_ascii=False, indent=2)
        print(f"Wrote mirror JSON copies to {STANDALONE_ARTICLES_DIR}")

if __name__ == "__main__":
    main()
