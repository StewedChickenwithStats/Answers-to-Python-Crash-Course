codewords={
	'array':'an arrangement of aerials spaced to give desired directional characteristics',
	'byte':'computer memory unit',
	'boolean':'a data type with only two possible values: true or false',
	'debug':'locate and correct errors in a computer program code',
	'address':'the code that identifies where a piece of information is stored'
}

# add five words
codewords['append']='a procedure for concatenating (linked) lists or arrays in some high-level programming languages'
codewords['adapter']='device that enables something to be used in a way different from that for which it was intended or makes different pieces of apparatus compatible'
codewords['constant']='a non-varying value'
codewords['branch']='a division of a stem'
codewords['copy']='reproduce or make an exact copy of'

# print all words
for k,v in codewords.items():
	print(k+": "+v)
