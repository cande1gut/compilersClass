#!/usr/bin/python2.6
import sys
import json
import lexicalAnalyzer as la
import syntacticAnalyzer as sa

lines = sys.stdin.readlines()

la.create_tokens(json.loads(lines[0]))
sa.read_program('lexerResult.txt')
