#!/usr/bin/python3
def multiple_returns(sent):
    return (len(sent), sent[0] if len(sent) > 0 else None)
