def txtWriteAPI(data,path):

    f = open(path,'w+')
    f.write(data)
    f.close()
    print("write down success! the txt save as %s" %(path))
if __name__=='__main__':
    data ="dataTest"
    path ="datatest.txt"
    txtWrite(data,path)