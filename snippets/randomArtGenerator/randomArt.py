import matplotlib.pyplot as plt
import numpy.random as npRandom

def randomArt(numPoints = 500, maxPointSize = 500, minPointSize = 1, markers = [".",",","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]):
  x = npRandom.rand(numPoints,1)
  y = npRandom.rand(numPoints,1)
  s = npRandom.random_integers(minPointSize,maxPointSize,numPoints)

  marker = [markers[npRandom.random_integers(0,(len(markers)-1),1)[0]] for i in range(numPoints)]

  c = [(npRandom.rand(1,1)[0][0],npRandom.rand(1,1)[0][0],npRandom.rand(1,1)[0][0],npRandom.rand(1,1)[0][0]) for i in range(numPoints)]

  import numpy as np

  markerIndexes = [np.where(marker == np.unique(markers[i])) for i in range(len(np.unique(marker)))]

  markerIndexes[1][0].tolist()
  plt.figure(figsize=(10,7.5))
  for i in range(len(markers)):
    plt.scatter(x[markerIndexes[i][0].tolist()],y[markerIndexes[i][0].tolist()],s[markerIndexes[i][0].tolist()],marker = markers[i], c = np.array(c)[markerIndexes[i][0].tolist()])
  plt.axis('off')

  plt.show()

randomArt(numPoints = 150,minPointSize=500,maxPointSize = 10000)