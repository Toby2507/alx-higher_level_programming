#!/usr/bin/python3
def best_score(a_dict):
    if a_dict:
        return sorted(a_dict.items(), key=lambda x: x[1], reverse=True)[0][0]
