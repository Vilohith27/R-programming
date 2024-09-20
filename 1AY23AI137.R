vec=c(1,2,3,4)
matrix1=matrix(1:9,nrow = 3,ncol = 3)
otherlist= list(a=1,b=2)
mylist= list(vec=vec,matrix1=matrix1,otherlist=otherlist)
firstele=mylist[[1]]
secondele=mylist[[2]]
print(firstele)
print(secondele)
