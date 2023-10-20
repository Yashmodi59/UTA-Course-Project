import sys
import random
import math

#  euclidean distance
def euclidean_dis(point1, point2):
    """
    :param point1:
    :param point2:
    :return:
    """
    differences = [point1[x] - point2[x] for x in range(len(point1))]
    differences_squared = [difference ** 2 for difference in differences]
    sum_of_squares = sum(differences_squared)
    return sum_of_squares ** 0.5


n = len(sys.argv)
# print("Give input in this format python3 k_means_cluster.py <data_file> <k> <iterations>")
    
input_path = sys.argv[1]
K = int(sys.argv[2])
n_iter = int(sys.argv[3])
random.seed()


# read using file path and read each line
def file_read():
    fileOpen = open(input_path, 'r')
    line = fileOpen.readlines()
    fileOpen.close()
    return line


# read the input file
lines = file_read()
dim = 0


def initializeCluster(K, lines):
    """
    Here we initialize some random cluster 
    :param K:
    :param lines:
    :return:
    """
    cluster = [[] for i in range(K)]
    il = []
    for line in lines:
        fValue = [float(val) for val in line.strip().split()] # Convert value into float
        dim = len(fValue)-1 # calculate dim length
        fValue = fValue[0:dim] 
        il.append(fValue)
        index = random.randint(0, K - 1) # choose random integer
        cluster[index].append(fValue)
    return dim,cluster,il

dim, cluster, input_list = initializeCluster(K, lines)


# empty centroid for given dim for each cluster(K)
def clusterCentroid(K, dim, cluster):
    """
    Create empty cluster of given dimention for each cluste
    :param K:
    :param dim:
    :param cluster:
    :return:
    """
    c = [[0]*dim for i in range(K)] # initialize cluster with Zero
    n=0
    while n != K:
        x=len(cluster[n]) # for each of the cluster do following thisn
        for i in range(x):
            y = len(cluster[n][0])
            for j in range(y):
                c[n][j] = c[n][j]+ cluster[n][i][j] # create centrod val
        n=n+1
    return c

centroids = clusterCentroid(K, dim, cluster)


def calculateCentroid(K, dim, cluster, centroids):
    """
    # calculate the centroid for each of the input 
    this code is reused mant times to calculate
    :param K:
    :param dim:
    :param cluster:
    :param centroids:
    :return:
    """
    i= 0
    while (i != K):
        if(len(cluster[i])>0):
            n = len(cluster[i])
            j=0
            while (j != dim):
                centroids[i][j] = centroids[i][j]/n # divide by length of dimention of centroid
                j = j+1
        i = i +1
    return centroids

centroids = calculateCentroid(K, dim, cluster, centroids)
# print(centroids)

for itr in range(n_iter+1):
    # in each iteration
    # for each points in input_list
    error = 0
    cluster.clear() # to clear initial cal
    cluster = [[] for i in range(K)]
    for point in input_list:
        # for each point find the closest centroid
        mini =  float('inf')
        index = 0 
        j = 0
        while j != K:
            d = euclidean_dis(point,centroids[j]) # calculate minimum dist if minimum store that index as minimum index
            if(d < mini):
                mini = d
                index = j
            j = j+1

        cluster[index].append(point)
        error += mini # append into error

    if(itr==0):
        print("After initialization: error = %.4f"%(error))
    else:
        print("After iteration %2d: error = %.4f"%(itr,error))

    centroids.clear() # again clear centroid
    centroids = clusterCentroid(K, dim, cluster)

    centroids = calculateCentroid(K, dim, cluster, centroids)     # re-calculate the centroid for next iteration
