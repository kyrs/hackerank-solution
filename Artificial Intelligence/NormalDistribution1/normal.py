'''
Coded by Kumar Shubham
Date: 17/01/2015

'''
import scipy.stats as st

def cdf(number):
	return st.norm.cdf(number,loc=30,scale=4)


print ('%.3f'%cdf(40))
print ('%.3f'%(1-cdf(21)))
print ('%.3f'%(cdf(35)-cdf(30)))
