# Definition

## Tokens

Character ::= a-z | A-Z | ? | _ | ~ | "+" | - | "*" | & | > | < | (Everything that isn't in other tokens)

Digit ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |9

Delimiter ::= ( | ) | [ | ] | "{" | "}" | , | ; | " | / | \

Operator ::= = | :Lang Definition


## Grammar

Exp ::= Def | SecondaryExp | Id : Start | Id ; | HttpGet ;

Def ::= Id = Prim ; | Id = Object ; | Id = SecondaryExp ; | Id = Int ;

SecondaryExp ::= Id : Second | Id : Third

Object ::= json : "{""}" | json : "{"{ String : ObjectParam , }* String : ObjectParam "}" | HttpGet

ObjectParam ::= String | Id | Exp

Prim ::= CreateServer

Second ::= SetRoutes | SetRoutes : Third

Third ::= CreateData | ReadData

Start ::= start ;

HttpGet ::= httpGet (from = String)

ReadData ::= readData (body = Id)

SetRoutes ::= setRoutes (url = String)

CreateData ::= createData (object = Id)

CreateServer ::= createServer () | createServer (port = Int)

String ::= " {Character | Digit | Delimiter | Operator}* "

Comment ::= // {Character | Digit | Delimiter | Operator}* \\

Id ::= Character {Character | Int}*

Int ::= Digit+
