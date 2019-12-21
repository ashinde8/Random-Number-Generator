# Random-Number-Generator
Uniform Distributed Random Number Generator 
Here I have built a random number generator by creating a class called LCG whose instance can generate random numbers by Linear Conguential Generator algorithm.
The class LCG has these data attributes: 
self.seed, self.multiplier, self.increment, self.modulus which are assigned in initializer ( init ()).
The class’s instance has function attributes that allows us to  : 
1) get the seed; 2) set the seed; 3) initialize the generator (start from the seed); 4) give me the next random number; 5) give me
a sequence (list) of random number.
We can test the performance of the random number generator, by using a simple Monte Carlo method .
