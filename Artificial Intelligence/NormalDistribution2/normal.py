'''
Coded by Kumar Shubham
Date: 17/01/2015

'''
import scipy.stats as st

def cdf(number):
	return st.norm.cdf(number,loc=20,scale=2)


print ('%.3f'%cdf(19.5))
#print ('%.3f'%(1-cdf(21)))
print ('%.3f'%(cdf(22)-cdf(20)))
