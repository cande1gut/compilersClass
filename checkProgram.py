import lexicalAnalyzer as la
import syntacticAnalyzer as sa

la.create_tokens('karelProgram.txt')
sa.read_program('lexerResult.txt')
