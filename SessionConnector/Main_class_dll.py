# -*- coding: utf-8 -*-
from ctypes import *
import time
import os.path
from .import login as pbbuf

'''
bool Init();
int  CreateSession(char* ip, char* port, unsigned int appid);
bool SendSessionMsg(int session_id, const char* msg, unsigned int msg_len);
bool RecvSessionMsg(int session_id, char* msg, unsigned int msg_size, int time_out);
void CloseSession(int Session_id);
'''

        		
class Main_class_dll():
      dllName = "libSessionConnectorBinary.so" 
      dllABSPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dllName
      dll = cdll.LoadLibrary(dllABSPath)
      judeInit=False

      def __init__(self):
          pass

      def int_create_(self):
         self.dll.Init.restype = c_bool
         if self.judeInit == False:
               sign = self.dll.Init()
               return sign
#              self.judeInit=True
         else:
               pass

      def Do_work_connector(self,ip,port,appid):
        self.dll.CreateSession.argtypes=[c_char_p,c_char_p,c_uint]   
        self.dll.CreateSession.restype = c_int               
        self.session_id = self.dll.CreateSession(ip,port,appid)
        return self.session_id

      def Do_work_send_recv(self,buf,session_id):
        time.sleep(2)
        self.session_id=session_id
        self.dll.SendSessionMsg.restype = c_bool
        self.dll.SendSessionMsg.argtypes=[c_int,c_char_p,c_uint]
        ret = self.dll.SendSessionMsg(self.session_id, buf, len(buf) + 1)
        self.dll.RecvSessionMsg.argtypes=[c_int,c_char_p,c_uint,c_int]
        self.dll.RecvSessionMsg.restype = c_bool
        recv_buf = create_string_buffer(1024)
        ret = self.dll.RecvSessionMsg(self.session_id, recv_buf, 1024, 3000)

        return recv_buf.value

      def Close_Session(self,session_id):
          self.session_id=session_id
          self.dll.MainSessionClosed.argtypes = [c_int]
          self.dll.MainSessionClosed.restype = None
          self.dll.MainSessionClosed(self.session_id)

      def test(self):
          dllName = "libSessionConnector.so"
          dllABSPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dllName
          return dllABSPath



a=Main_class_dll()
mysession_id=a.Do_work_connector("192.168.7.75","","1")
# currently the client token format is 1;xxxxxx, the cp will not verify this client currntly
client_token="1;ujfnto"
buf=pbbuf.LoginCP(client_token,0)
myresp=a.Do_work_send_recv(buf,mysession_id)

print myresp