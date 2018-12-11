import sys
import subprocess
import time
import os

on_file_name = sys.argv[1]
dc_file_name = sys.argv[2]
bw = int(sys.argv[3]);
blif_file_name = "rect_func_"+str(bw)+".blif"
# print out_file;
on_file = open(on_file_name,'r');
dc_file = open(dc_file_name,'r');
blif_file = open(blif_file_name,'w');

blif_file.write(".model "+"ON_EXDC_BW_"+str(bw)+"\n");
inp_line = ".inputs ";
for i in range(bw):
	inp_line = inp_line + "a_" + str(i) + "_ "
for i in range(bw):
	inp_line = inp_line + "b_" + str(i) + "_ "
blif_file.write(inp_line+"\n");
blif_file.write(".outputs rf\n");

on_poly = on_file.readline();
on_poly = on_poly.strip();
on_pp = on_poly.split("+");
# print on_pp;
count = 0;

for p in on_pp:
	count+=1;
	if p == '1':
		blif_file.write(".names p"+str(count)+"\n"+"1\n");
	else:
		variables = p.split("*")
		vlen = len(variables);
		blif_file.write(".names ")
		for v in variables:
			blif_file.write(v+" ")
		blif_file.write("p"+str(count)+"\n")
		blif_file.write("1"*vlen + " 1\n")
# print count;
for c in range(count-1):
	s = c+1;
	if s==1:
		blif_file.write(".names p1 p2 s1\n10 1\n01 1\n");
	else:
		blif_file.write(".names p"+str(s+1)+" s"+str(s-1)+" s"+str(s)+"\n");
		blif_file.write("10 1\n01 1\n");

if count == 1:
	blif_file.write(".names p1 rf\n0 1\n");
else:
	blif_file.write(".names s"+str(s)+" rf\n0 1\n\n\n");


blif_file.write(".exdc\n");
blif_file.write(inp_line+"\n");
blif_file.write(".outputs rf\n");

dc_poly = dc_file.readline();
dc_poly = dc_poly.strip();
dc_pp = dc_poly.split("+");
# print on_pp;
count = 0;

for p in dc_pp:
	count+=1;
	if p == '1':
		blif_file.write(".names pdc"+str(count)+"\n"+"1\n");
	else:
		variables = p.split("*")
		vlen = len(variables);
		blif_file.write(".names ")
		for v in variables:
			blif_file.write(v+" ")
		blif_file.write("pdc"+str(count)+"\n")
		blif_file.write("1"*vlen + " 1\n")
# print count;
for c in range(count-1):
	s = c+1;
	if s==1:
		blif_file.write(".names pdc1 pdc2 sdc1\n10 1\n01 1\n");
	else:
		blif_file.write(".names pdc"+str(s+1)+" sdc"+str(s-1)+" sdc"+str(s)+"\n");
		blif_file.write("10 1\n01 1\n");

if count == 1:
	blif_file.write(".names pdc1 rf\n0 1\n");
else:
	blif_file.write(".names sdc"+str(s)+" rf\n0 1\n\n\n");

blif_file.write(".end\n")

on_file.close();
dc_file.close();
blif_file.close();
