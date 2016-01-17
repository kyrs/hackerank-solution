'''
Coded by Kumar Shubham
Date: 17/01/2015

'''
import scipy.stats as st

def cdf(number):
	return st.norm.cdf(number,loc=70,scale=10)


print ('%.2f'%(100-cdf(80)*100))
print ('%.2f'%(100-cdf(60)*100))
print ('%.2f'%(cdf(60)*100))
