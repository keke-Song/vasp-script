#!/bin/bash
read_file=XDATCAR
writ_file=POSCAR
rm POSCAR_*

read -p "Pleas input the increment to extract the frame what you want: " incr
echo "Your inrement is $incr, I am gonna extract the frames of 1, 1+$incr, 1+ 2*$incr ..."
sleep "3s"

N_tota_conf=$(grep -c "Direct configuration=" $read_file)
echo "grand total of frames in the $read_file is $N_tota_conf"

conf_size=$(sed -n '7p' $read_file | awk '{print $1 + $2}')
echo "count to atoms per frame is $conf_size"

for((i=1;i<=$N_tota_conf;i=i+$incr))
do
	star_line=$(grep -n "Direct configuration" $read_file |awk -F: '{print $1}' | sed -n ''$i'p')
	end_line=$((star_line + conf_size))
	sed -n '1,7p' $read_file > ${writ_file}_$i
	sed -n ''$star_line','$end_line'p' $read_file >> ${writ_file}_$i
	echo "The ${i}-th frame extracted and written into the file ${writ_file}_$i, next ..."	
done
echo "All done, bye"

