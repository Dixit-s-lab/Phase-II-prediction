source ~/.bashrc
tsp -S 10
#j=0
for i in $(ls *.mop | sed 's/.mop//g')
do
	tsp /opt/mopac/MOPAC2016.exe $i.mop
	#j=$j+1	
done
mop=$(ls -1q *.mop | wc -l)
#	echo "number of mop files"
#echo "$mop"
while [ $mop -gt $(ls  *.arc | wc -l) ];
do
    #arc_files= $(ls -1q *.arc | wc -l)
    echo "creating .arc file"
    sleep 5s
		
done
#echo "number of .arc files"
#echo "$(ls -1q *.arc | wc -l)"

echo "Mopac jobs completed"
#sleep 1800s

#echo "analyzing mopac output files"
#echo "analyzing mopac output files" > mopac-anion-energies.txt
echo "molecule mopacE" >> mopac-anion-energies.txt
for m in $(ls *anion*.arc | sed 's/.arc//g')
do
	geomstatus=$(grep "FINAL GEOMETRY OBTAINED" $m.arc)
	if [[ -z "$geomstatus" ]]; then
		echo "$m jobs probably failed, thus check and resubmit" >> mopac-anion-energies.txt
	else
		mopacE=$(grep "HEAT OF FORMATION       =" $m.arc | awk '{print $5}')
		
		echo "$m $mopacE" >> mopac-anion-energies.txt
	fi
done

#echo "analyzing mopac output files" > mopac-energies.txt
echo "molecule mopacE" >> mopac-energies.txt
for m in $(ls *neutral*.arc | sed 's/.arc//g')
do
	geomstatus=$(grep "FINAL GEOMETRY OBTAINED" $m.arc)
	if [[ -z "$geomstatus" ]]; then
		echo "$m jobs probably failed, thus check and resubmit" >> mopac-energies.txt
	else
		mopacE=$(grep "HEAT OF FORMATION       =" $m.arc | awk '{print $5}')
		
		echo "$m $mopacE" >> mopac-energies.txt
	fi
done
