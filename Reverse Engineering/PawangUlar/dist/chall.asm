4           0 RESUME                   0

  5           2 LOAD_GLOBAL              1 (NULL + input)
             12 LOAD_CONST               1 ('masukkan password: ')
             14 CALL                     1
             22 LOAD_ATTR                3 (NULL|self + encode)
             42 CALL                     0
             50 STORE_FAST               0 (password)

  6          52 LOAD_FAST                0 (password)
             54 LOAD_ATTR                5 (NULL|self + hex)
             74 CALL                     0
             82 LOAD_CONST               2 ('d7d63743f5e60386479707f5a733f593e63346e633775793b7353484')
             84 LOAD_CONST               0 (None)
             86 LOAD_CONST               0 (None)
             88 LOAD_CONST               3 (-1)
             90 BUILD_SLICE              3
             92 BINARY_SUBSCR
             96 COMPARE_OP              40 (==)
            100 POP_JUMP_IF_FALSE       12 (to 126)

  7         102 LOAD_GLOBAL              7 (NULL + print)
            112 LOAD_CONST               4 ('medeni rek!')
            114 CALL                     1
            122 POP_TOP
            124 RETURN_CONST             0 (None)

  9     >>  126 LOAD_GLOBAL              7 (NULL + print)
            136 LOAD_CONST               5 ('maaf anda kurang beruntung')
            138 CALL                     1
            146 POP_TOP
            148 RETURN_CONST             0 (None)
