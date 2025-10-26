import math

def wilson(x1,v1,v2,a12,a21,temp):
    x2=1-x1
    delta12 = (v2/v1)*math.e**(-a12/(8.314*temp))
    delta21 = (v1/v2)*math.e**(-a21/(8.314*temp))
    ln_gamma1 = -1*math.log(x1+x2*delta12)+x2*((delta12/(x1+x2*delta12))-(delta21/(x2+x1*delta21)))
    ln_gamma2 = -1*math.log(x2+x1*delta21)-x1*((delta12/(x1+x2*delta12))-(delta21/(x2+x1*delta21)))
    return math.e**(ln_gamma1), math.e**(ln_gamma2)

def nrtl(x1,b12,b21,alpha,temp):
    x2 = 1-x1
    tau12 = b12/(8.314*temp)
    tau21 = b21/(8.314*temp)
    g12 = math.e**(-1*alpha*tau12)
    g21 = math.e**(-1*alpha*tau21)
    ln_gamma1 = (x2**2)*(tau21*(g21/(x1+x2*g21))**2 + ((g12*tau12)/((x2+x1*g12)**2)))
    ln_gamma2 = (x1**2)*(tau12*(g12/(x2+x1*g12))**2 + ((g21*tau21)/((x1+x2*g21)**2)))
    return math.e**(ln_gamma1), math.e**(ln_gamma2)

def vap_pressure(A,B,C,temp):
    temp = temp - 273.15
    ln_psat = A-B/(temp+C)
    return math.e**(ln_psat)

def boiling_pt(A,B,C,psat):
    return (B/(A-math.log(psat))-C) + 273.15