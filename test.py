from SessionConnector import fsp_proto_pb2 as fpb

strcp=fpb.PublishStreamCP()
print strcp.stream_id
strcp.stream_id="10"
strcp.client_id="20"
strcp.client_ip="192"

tt=strcp.SerializeToString()
# print tt

# pp=fpb.PublishStreamCP()
# pp.ParseFromString(tt)
# print pp.client_ip

# buf=[]
edic=fpb.ProtoDictionary.Value('Enum2Login')
print edic