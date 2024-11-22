local codeEditorInfos=[[
int result = simZMQ.bind(string socket, string endpoint)
int result = simZMQ.close(string socket)
int result = simZMQ.connect(string socket, string endpoint)
int result = simZMQ.ctx_get(string context, int option_name)
string context = simZMQ.ctx_new()
int result = simZMQ.ctx_set(string context, int option_name, int option_value)
int result = simZMQ.ctx_shutdown(string context)
int result = simZMQ.ctx_term(string context)
string context = simZMQ.ctx_singleton()
int result = simZMQ.disconnect(string socket, string endpoint)
int result = simZMQ.errnum()
int result, buffer value = simZMQ.getsockopt(string socket, int option_name, int option_len)
int result = simZMQ.has(string capability)
int result = simZMQ.msg_close(string msg)
int result = simZMQ.msg_copy(string dest, string src)
buffer data = simZMQ.msg_data(string msg)
simZMQ.msg_destroy(string msg)
int result, string value = simZMQ.msg_gets(string msg, string property)
int result = simZMQ.msg_get(string msg, int property)
int result = simZMQ.msg_init_size(string msg, int size)
int result = simZMQ.msg_init(string msg)
int result = simZMQ.msg_more(string msg)
int result = simZMQ.msg_move(string dest, string src)
string msg = simZMQ.msg_new()
int result = simZMQ.msg_recv(string msg, string socket, int flags)
int result = simZMQ.msg_send(string msg, string socket, int flags)
int result = simZMQ.msg_set(string msg, int property, int value)
int result = simZMQ.msg_size(string msg)
int result, int[] revents = simZMQ.poll(string[] sockets, int[] events, int timeout=0)
int result = simZMQ.proxy_steerable(string frontend, string backend, string capture, string control)
int result = simZMQ.proxy(string frontend, string backend, string capture)
int result, buffer data = simZMQ.recv(string socket, int flags, int max_buf_size=nil)
int result = simZMQ.send(string socket, buffer data, int flags)
int result = simZMQ.setsockopt(string socket, int option_name, buffer option_value)
int result = simZMQ.socket_monitor(string socket, string endpoint, int events)
string socket = simZMQ.socket(string context, int type)
string message = simZMQ.strerror(int errnum)
int result = simZMQ.unbind(string socket, string endpoint)
int major, int minor, int patch = simZMQ.version()
int result = simZMQ.ctx_set_ext(string context, int option_name, buffer option_value)
int result, buffer data = simZMQ.ctx_get_ext(string context, int option_name)
int result = simZMQ.join(string socket, string group)
int result = simZMQ.leave(string socket, string group)
int result = simZMQ.connect_peer(string socket, string addr)
int result = simZMQ.msg_set_routing_id(string msg, int routing_id)
int routing_id = simZMQ.msg_routing_id(string msg)
int result = simZMQ.msg_set_group(string msg, string group)
int result, string group = simZMQ.msg_group(string msg)
]]

registerCodeEditorInfos("simZMQ",codeEditorInfos)
