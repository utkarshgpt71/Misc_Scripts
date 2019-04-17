import sys
import subprocess
import time
import os

bw = int(sys.argv[1])
mfix = int(sys.argv[2]); #may need to change this
out_file = "bits_in_W.sing" 
sing = open(out_file, 'w');

sing.write("ring R = (2,x), (W), lp;\n\n");

prim_poly = open("bprimtive",'r'); #Extracting the primitive polynomial from bprimtive
found_poly = 0;

for bp in prim_poly.readlines():
	if bp.strip() != '':
		bp_list = bp.strip().split(' ');
		if bp_list[-1] == str(bw):
			sing.write("minpoly = ")
			for d in reversed(bp_list):
				sing.write("x^"+d+"+");
			sing.write("1;\n\n")
			found_poly = 1;
			break;
prim_poly.close()

if found_poly == 0:
	sing.write("minpoly = ;\n\n");
	print "Primitive polynomial not found in the bprimtive inp_file";
	print "Please provide one with appropriate degree as used in ckt construction";

sing.write("int bw = "+str(bw)+";\n");
sing.write("int mfix = "+str(mfix)+";\n");
sing.write("int i,j;\n");
sing.write("matrix A[bw][bw];\n\n");

sing.write("for(i=1;i<=bw;i++) \n{\n")
sing.write("  for(j=1;j<=bw;j++) \n  {\n")
sing.write("    A[i,j] = x ^ ( (2^(i-1)) * (j-1));\n") 
sing.write("  } \n}\n\n");

sing.write("matrix B[bw][1];\n\n");

sing.write("for(i=1;i<=bw;i++) \n{\n")
sing.write("  B[i,1] = W^(2^(i-1));\n}\n\n")

sing.write("matrix tmp[bw][bw];\nlist L;\n\n");

sing.write("for(i=1;i<=mfix;i++)\n{\n");
sing.write("  tmp = A;\n");
sing.write("  tmp[1..bw,i] = B;\n");
sing.write("  L[i] = det(tmp);\n}\n\n")

sing.write("string s = \"Computed_Lists/bits_in_W_\" + string(bw)+ \"_\" + string(mfix) +\".list\";\n")
sing.write("write(\":w \"+s,L);\n")
sing.write("quit;")

sing.close();

subprocess.call(['Singular bits_in_W.sing'], shell = True);
subprocess.call(['rm bits_in_W.sing'], shell = True);
