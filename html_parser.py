from html.parser import HTMLParser

index=0
dict={}
file = open('vvrs01-20130301 (20130316)-0416.trs','r',encoding='utf-8')
data = file.read().replace('\t',"")
data2 =data.replace('\n',"")
 
class MyParser(HTMLParser):
#    def handle_startendtag(self, tag, attrs):
#         if(tag=="sync"):
#             print(attrs)
            
    def handle_data(self, data): 
        if(len(data) >= 2):
            if(self.is_cn_char(data[0]) or (self.is_cn_char(data[1]) and data[0]==" ")):
                """存入字典"""
                global index
                index = self.update_dict(index, dict, data)
                #print(data[1])
                   
            elif(data[0]=="-" or data[0]==" "):
                """直接接上一行"""
                self.append_dict(index, dict, data)   
    
    def is_cn_char(self, i): 
        """判斷是否為中文"""
        return 0x4e00<=ord(i)<0x9fa6 
    
    def update_dict(self,index,dict,data):
        """更新字典"""
        dict.update({index:data})
        index+=1
        return index
    def append_dict(self, index, dict, data):
        """將換行的部分接上上一句"""
        index_tmp = index - 1
        tmp=[]
        tmp.append(dict.pop(index_tmp))
        tmp.append(data)
        tmp1=''.join(tmp)
        dict.update({index_tmp:tmp1})
        
#     def change_data_value(self,data):
#         tmp = list(data)
#         tmp[0]=""
#         "".join(tmp)
         
parser = MyParser(strict=False)
parser.feed(data2)
for i in range(len(dict)):
      print(dict[i])