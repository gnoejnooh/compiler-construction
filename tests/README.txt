Explanations of each test cases are put here because I don't know if your program can handle comments

Here is what rule each test cases test:

1: class -> ...
2: class_body_decl -> field_decl
3: class_body_decl -> constructor_decl
4: class_body_decl -> method_decl
5: stmt -> var_decl
6: method_decl -> ...
7: Same as 6
8: stmt -> while, stmt_list -> stmt+
9: stmt -> if
10: primary -> new id '(' ')'
11: stmt -> stmt_expr -> assign
12: lhs -> field_access
13: stmt -> for
14: comment
15, 16, 17: modifier -> ...
18: type -> id
19: stmt -> return
20: primary -> literal -> null
21: method_invocation -> field_access '(' ')'
22: stmt -> break; stmt -> continue;
23: primary -> new id '(' argument+ ')'
24: new_array -> new type ( '[' expr ']' )+
25: array_access -> primary '[' expr ']'
26: string literals
27: new_array -> new type ( '[' expr ']' )+ ('[' ']')*
all: combination of above

err#: various error cases
multierr#: test one input with multiple errors
