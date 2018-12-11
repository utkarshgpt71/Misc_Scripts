import sys
import subprocess
import time
import os

poly_file_name = sys.argv[1]
pla_file_name = sys.argv[2]
bw = int(sys.argv[3]);
# print out_file;
poly_file = open(poly_file_name,'r');
pla_file = open(pla_file_name,'w');

var_index = {}
var_list = [-1]*(2*bw); #just an initialization
for i in range(bw):
	vname = "b_"+str(bw-i-1)+"_";
	var_index[vname] = i;
	var_list[i] = vname;
	vname = "a_"+str(bw-i-1)+"_"
	var_index[vname] = bw+i;
	var_list[bw+i] = vname;

pla_file.write(".i "+str(bw*2)+"\n")
pla_file.write(".o 1\n.ilb ")
pla_file.write(' '.join(var_list)+"\n");
pla_file.write(".ob rf\n.type esop\n");

poly = poly_file.readline();
poly = poly.strip();
pp = poly.split("+");

if pp[-1] == '1': #inverting the AND-XOR expression
	pp.remove('1')
else:
	pp.append('1')

for p in pp:
	cube = ['-']*(bw*2);
	if p != '1':
		variables = p.split('*');
		for v in variables:
			cube[var_index[v]] = '1'
	# print cube
	pla_file.write(''.join(cube)+' 1\n')
pla_file.write(".e")

poly_file.close();
pla_file.close();
