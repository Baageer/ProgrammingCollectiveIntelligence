import clusters

blognames,words,data=clusters.readfile('blogdata.txt')
clust=clusters.hcluster(data)
#clusters.printclust(clust,labels=blognames)

#clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

#rdata = clusters.rotatematrix(data)
#wordclust = clusters.hcluster(rdata)
#clusters.drawdendrogram(wordclust, labels=words, jpeg='wordclust.jpg')

kclust = clusters.kcluster(data, k=10)

print([blognames[r] for r in kclust[0]])
print([blognames[r] for r in kclust[1]])
