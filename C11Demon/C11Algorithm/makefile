#C11Demo、C11UnicodeDemo C11TableDemo C11Algorithm
target=C11Algorithm
cflags=--std=c++11 -g
cc=g++
inc= $(wildcard *.h)
src=$(wildcard *.cpp)
#src=$(target).cpp

all:
	echo $(src)
	$(cc) -o $(target) $(cflags) $(src) -I ./
clean:
	rm -rf $(target) 
	
	
	
