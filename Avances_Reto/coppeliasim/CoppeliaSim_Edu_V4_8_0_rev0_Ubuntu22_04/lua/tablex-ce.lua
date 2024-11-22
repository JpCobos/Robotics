registerCodeEditorInfos('tablex', [[
table t = table.add(table t1, table t2, ...)
table tableOfTables = table.batched(table t, int n)
table copy = table.clone(table t)
int comparison = table.compare(table a, table b, function compareFunc = nil)
string s = table.concat(table t, string sep = '', int start = 1, int end = #t)
table copy = table.deepcopy(table t, table opts = {}, table copies = {})
bool equal = table.eq(table a, table b)
table.extend(table t, table t1, ...)
int? index = table.find(table t, any item, function equalsFunc = nil)
table.tbl1 = table.flatten(table tbl, table opts = {})
int n = table.getn(table t)
function fn = table.index(table t)
table.insert(table t, [int pos], any value)
bool arr = table.isarray(table t)
string s = table.join(table t, string sep = ', ', table opts = {}, visited = {})
table keys = table.keys(table t)
table.move(table a, int f, int e, int t, table ab = a)
table t = table.pack(...)
table.print(table t)
any removed = table.remove(table t, int pos)
table t = table.rep(any value, int size)
table reversed = table.reversed(table t)
table.setn(table t, int n)
table sliced = table.slice(table t, int first = 1, int last = #t, int step = 1)
table.sort(table t, function compareFunc = nil)
string s = table.tostring(table t, string sep, table opts = {}, visited = {})
table tbl1 = table.unflatten(table tbl, table opts = {})
... = table.unpack(table t)
]])
