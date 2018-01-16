languages = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC'.split(':')
l = [i.strip() for i in languages]
n = int(input().strip())
for _ in range(n):
    s = input().strip().split()[1]
    if s in l:
        print('VALID')
    else:
        print('INVALID')