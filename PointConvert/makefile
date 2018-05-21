target=PointConvert
cflags=--std=c++11
cc=g++ -g
src=$(wildcard *.cpp)
INC=$(addprefix -I , $(wildcard ./))

all:
	#echo $(INC)
	$(cc) -o $(target) $(cflags) $(src) $(INC)
clean:
	rm -rf $(target) 
	
	
	
