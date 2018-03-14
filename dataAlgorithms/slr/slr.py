# function to predict y in a simple linear regression with a given w_0 and w_1 value
def predictY(w0,w1,x):
    predY = []
    for i in range(0,len(x)):
        predY.append(w0 + w1*x[i])
    return predY

# function to compute the error of SLR
def computeError(predY,y):
    error = [a - b for a, b in zip(predY, y)]
    return error

# function to compute the derivative
def computeCoeffDerivative(x,error):
    import numpy as np
    w0Der = sum(error)
    w1Der = np.sum(np.dot(x, error))
    der = [w0Der,w1Der]
    return der

# function to compute adjustment of coefficient
def computeCoeffAdjust(derivative,eta):
    adjustment = derivative*eta
    return adjustment

# function to adjust the regression coefficients
def adjustCoeff(w,adjustment):
    w = w-adjustment
    return w

# function to compute magnitude of a gradient
def magnitudeGrad(w0_error, w1_error):
    magnitude = float(((w0_error)**2 + (w1_error)**2)**0.5)
    return magnitude

# function to determine if converged
def solutionConverged(magnitude,mu):
    return magnitude < mu

# function to carry out one step of gradient descent algorithm
def gradientDescentIteration(w0,w1,x,y,eta,mu):
    
    # Step 1
    predY = predictY(w0,w1,x)
    
    # Step 2
    error = computeError(predY,y)
    
    # Step 3 & 4
    derivatives = computeCoeffDerivative(x,error)
    
    # Step 3.1
    w0Der = derivatives[0]
    # Step 3.2
    w0adj = computeCoeffAdjust(w0Der,eta)
    # Step 3.3
    w0 = adjustCoeff(w0,w0adj)
    
    # Step 4.1
    w1Der = derivatives[1]
    # Step 4.2
    w1adj = computeCoeffAdjust(w1Der,eta)
    # Step 4.3
    w1 = adjustCoeff(w1,w1adj)
    
    # Step 5
    magnitude = magnitudeGrad(w0Der,w1Der)
    
    # Step 6
    converged = solutionConverged(magnitude,mu)
    
    newCoeff = [w0,w1,converged]
    return newCoeff

# function to find optimal solution for slr using gradientDescent

def fit(x,y,w0,w1,eta,mu,maxIterations = 500):
    notConverged = True
    i = 0
    while notConverged:
        i = i+1
        update = gradientDescentIteration(w0,w1,x,y,eta,mu)
        w0 = update[0]
        w1 = update[1]
        if update[2]:
            notConverged = False
        if i == maxIterations:
            notConverged = False
    output = [w0,w1,i]
    return output

# eta = stepsize, mu = tolerance level, w0 = intercept, w1 = slope, x = input, y = output/response
