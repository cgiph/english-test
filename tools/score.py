#!/usr/bin/env python3
"""Simple scorer for objective items.

Usage:
  python3 tools/score.py --answers answers.json --key tests/keys/all_keys.json

The script prints a JSON summary with counts and percent correct, and includes the manual essay score if present.
"""
import json
import argparse
import sys
from pathlib import Path

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def score_grammar(answers, key):
    total = len(key)
    correct = 0
    for q,a in key.items():
        if answers.get(q, '').strip().lower() == a.strip().lower():
            correct += 1
    return correct, total

def score_reading(answers, key):
    mc_keys = {k:v for k,v in key.items() if not k.startswith('r1_sa')}
    sa_keys = {k:v for k,v in key.items() if k.startswith('r1_sa')}
    correct = 0
    total = 0
    # MC
    for k,v in mc_keys.items():
        total += 1
        if answers.get(k, '').strip().lower() == v.strip().lower():
            correct += 1
    # Short answers: accept if any keyword from key list present (simple matching)
    for k,vals in sa_keys.items():
        total += 1
        ans = answers.get(k, '').strip().lower()
        for acceptable in vals:
            if acceptable.lower() in ans:
                correct += 1
                break
    return correct, total

def score_listening(answers, listening_key):
    # Listening is summary-style. This function gives a simple partial score:
    # If answer length >= 20 chars -> 1 point per item as basic check; custom checking can be added.
    correct = 0
    total = len(listening_key)
    for lid in listening_key:
        text = answers.get(lid, '').strip()
        if len(text) >= 20:
            correct += 1
    return correct, total

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--answers', required=True)
    p.add_argument('--key', required=True)
    args = p.parse_args()
    answers = load(args.answers)
    keys_map = load(args.key)
    grammar_key = load(keys_map['grammar'])
    reading_key = load(keys_map['reading'])
    listening_key = keys_map.get('listening', {})
    result = {}
    g_correct,g_total = score_grammar(answers.get('grammar', {}), grammar_key)
    result['grammar'] = {'correct': g_correct, 'total': g_total, 'percent': g_correct / g_total * 100}
    rc_correct,rc_total = score_reading(answers.get('reading', {}), reading_key)
    result['reading'] = {'correct': rc_correct, 'total': rc_total, 'percent': rc_correct / rc_total * 100}
    l_correct,l_total = score_listening(answers.get('listening', {}), listening_key)
    result['listening'] = {'correct': l_correct, 'total': l_total, 'percent': l_correct / l_total * 100}
    # Essay score (manual)
    essay_score = answers.get('writing', {}).get('essay_score')
    result['writing'] = {'essay_score': essay_score}
    print(json.dumps({'summary': result}, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
