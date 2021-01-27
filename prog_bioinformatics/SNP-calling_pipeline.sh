#!/bin/bash

# project_info  - A script to align FASTQ files to reference genome, process the alignment files and call the variants
gtusername="rbk3"
#exec 1>"${gtusername}".log 2>&1

function get_user_input () {
	# function to get user input
	v=0
	gunzip=0
	realign=0
	output="solution"
	index=0
	readme=0
	answer=0
	while getopts "a:b:r:f:eovzih" options
	do
		case $options in
			a) reads1=$OPTARG; echo "Reads-1 file is ${reads1}";;
                	b) reads2=$OPTARG; echo "Reads-2 file is ${reads2}";;
                	r) ref=$OPTARG; echo "Reference genome for mapping is ${ref}";;
			e) realign=1; echo "User has chosen option to realign. Will perform realignment";;
			o) output="${gtusername}"; echo "Name of output file will be ${output}.vcf";;
                	f) millsFile=$OPTARG; echo "The mills file for realignment is ${millsFile}";;
                	z) gunzip=1; echo "User has asked to gunzip the output file.";;
                	v) v=1;;
                	i) index=1; echo "User has asked to index the .bam file";;
                	h) readme=1;;
			*) echo "Invalid option. Try again. Provide  -h  with script for lookup into the help menu for usage information"
				exit 1;;
        	esac
	done
	# if help option taken
	if [ "$readme" -eq 1 ];then
echo "snp pipeline(1)                                                                        User Commands                                                                 snp pipeline(1)                NAME
       SNP-calling pipeline  - perform alignment of FASTQ files to reference genome, process the alignment files and call the variants

SYNOPSIS
       SNP-calling_pipeline.sh -a [VALUE]... -b [VALUE]...

DESCRIPTION
       Perform the snp calling pipeline function to generate .vcf files.

       -a     Input reads file – pair 1 ; path/of/reads file 1
       -b     Input reads file – pair 2 ; path/of/reads file 2
       -r     Reference genome file     ; path/to/ref genome file
       -e     Perform read re-alignment ; for realigning the sorted .bam file 
       -o     Output VCF file name      ; name of the ouput file user wants
       -f     Mills file location       ; path/to/mills file
       -z     Output VCF file should be gunzipped (*.vcf.gz) ; to unzip the output file
       -v     Verbose mode              ; print each instruction/command to tell the user what your script is doing right now
       -i     Index your output BAM file (using samtools index) ; 
       -h     Print usage information (how to run your script and the arguments it takes in) and exit

AUTHOR
       Written by Rohan.

REPORTING BUGS
       BIOC coreutils online help: <https:// coming soon >
       Report echo translation bugs to <https:// coming soon >

COPYRIGHT
       Copyright © 2020 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <http:// coming soon 
       or available locally via: will be updated soon

BIOC coreutils 0.01                                                                          September 2020                                                                   snp pipeline(1)"
		exit 0
	fi

	[ "$v" -eq 1 ] && echo "verbose mode is on" || echo "verbose mode is off"

	return 0
}

function verify_files () {

	# verify if input files exist
	#Checking

	#See if input was given or not.

	[ "$v" -eq 1 ] && echo "Running basic requirement checks to see if the necessary files are provided."; 

	if [ -z "$reads1" ] || [ -z "$reads2" ] || [ -z "$ref" ] || [ -z "$millsFile" ];then
		echo "Some or more (reads1 , reads2 , ref , millsFile) of the essential files/parameters not provided. Please check HELP page (provide -h with script)"
		return 1
	fi

	#Checking for read file 1.
	if [ ! -f "$reads1" ]
       	then
		echo "File named ${reads1} NOT found !!"
		return 1
        fi
	
	#Checking for read file 2.
	if [ ! -f "$reads2" ]
        then
                echo "File named ${reads2} NOT found !!"
		return 1
        fi
	
	#Checking for chromosome reference.
        if [ ! -f "$ref" ]
        then
                echo "Species reference Genome file ${ref} NOT found !!"
                return 1
        fi

	#Checking for mills file.
	if [ ! -f "$millsFile" ]
	then	
		echo "File named ${millsFile} NOT found !!"
		return 1
	fi


	#Checking if output files exist.
	if [ -f "$output".vcf ];then
		echo "output VCF file already exists. Do you want to overwrite the existing ${output} file or continue the program? (Y/n) : "
		read -r answer

		if [ "$answer" == "Y" ];then
			echo "User has chosen to overwrite the output.vcf file. Will run the pipeline"
		elif [ "$answer" == "n" ];then
			echo "User does not want to generate new.vcf file. Will skip the steps and move to conversion file format step.";
		else
			echo "Wrong input given. Exiting the program now........"
			return 1
		fi
# 140
	else
		answer="Y"
        fi
	return 0
}

function project_essentials () {
	#defining project and tmp directories to variables 
        [ "$v" -eq 1 ] && echo "Defining path variables now and creating a temporary directory for project if it not exists !!"

	project_dir=$(pwd)
	tmp_dir="${project_dir}/tmp"	
	if [ ! -d "$tmp_dir" ]; then
  		echo "Temporary directory for the project does not exist. Creating new one"
		new_tmp_dir=$(mktemp -d tmp.XXXX)
		tmp_dir="${project_dir}/${new_tmp_dir}"
	fi
	_id="biol7200"
	_sm="${ref%.*}"
	_lb="lab-6"
	return 0
}

function reads_mapping () {
	#method to perform mapping of reads to genome
	if [ "$answer" == "n" ];then
		echo "Skipping the reads mapping steps....";
		return 1
	fi

        [ "$v" -eq 1 ] && echo "Initiating..... Mapping input reads to the reference genome"; echo "Creating the index file";
	
	echo "Do you wish to index reference genome file ? (Y/n) :"
	read -r u_input
	
	if [ "$u_input" == "n" ];then
                :
        elif [ "$u_input" == "Y" ];then
                [ "$v" -eq 1 ] && echo "Running ref genome indexing now";
                bwa index "$ref"
        else
                echo "Wrong input = ${u_input} given. Exiting now......"; exit 1;
        fi
	
	[ "$v" -eq 1 ] && echo "Creating .sam files while mapping reads to the reference. It takes time, be patient";

	if [ -e "${project_dir}/lane.sam" ];then
		echo "The file lane.sam already exists after mapping reads1 , reads2 to the ref reference genome. Do you wish to overwrite? (Y/n) : "
		read -r user_input
	else
		user_input="Y"
	fi
	
        if [ "$user_input" == "n" ];then
		:
	elif [ "$user_input" == "Y" ];then
		[ "$v" -eq 1 ] && echo "Running mapping now";
		bwa mem -R '@RG\tID:biol7200id\tSM:species\tLB:lab-6' "$ref" "$reads1" "$reads2" > "${project_dir}/lane.sam"
	else
		echo "Wrong input = \$user_input given. Exiting now......"; exit 1;
	fi
# 204   
	[ "$v" -eq 1 ] && echo "Successfully generated the .sam file"; echo "Running fixes via fixmate and sorting to provide alignment.";


	if [ -e "${project_dir}/lane_fixmate.bam" ];then
		echo "The fix_xyz.sam file after cleaning up read information and flags already exists. Moving to the next steps. Do you wish to overwrite? (Y/n) : "
		read -r user_input
	else
                user_input="Y"
        fi

	if [ "$user_input" == "n" ];then
                :
        elif [ "$user_input" == "Y" ];then
                [ "$v" -eq 1 ] && echo "Running fixmate now to remove flags";
		samtools fixmate -O bam "${project_dir}/lane.sam" "${project_dir}/lane_fixmate.bam"
	else
		echo "Wrong input = \$user_input given. Exiting now......"; exit 1;
	fi
	
	if [ -e "${project_dir}/lane_sorted.bam" ];then
		echo "The lane_sort_xyz.bam file exists in the directory. Do you wish to overwrite? (Y/n) : "
		read -r user_input
	else
		user_input="Y"
	fi
	
	if [ "$user_input" == "n" ];then
                :
        elif [ "$user_input" == "Y" ];then
                [ "$v" -eq 1 ] && echo "Running the sort method to convert to coordinate order"
		samtools sort -O bam -o "${project_dir}/lane_sorted.bam" -T "${tmp_dir}/lane_temp" "${project_dir}/lane_fixmate.bam"
	else
                echo "Wrong input = \$user_input given. Exiting now......"; exit 1;
	fi

	if [ -e "${project_dir}/lane_sorted.bam" ];then
		echo "Successfully finished mapping the ${reads1} and ${reads2} FASTQ files to the ${ref} genome."
	else
		echo "Something went wrong. Please check"
	fi

	return 0
}

function run_improvement () {
	#method to run the imporvemnet steps
        if [ "$answer" == "n" ];then
                echo "Skipping the reads mapping steps....";
                return 1
        fi

        [ "$v" -eq 1 ] && echo "Initiating..... Improvement to realign for reducing the number of miscalls of INDELs in the data"; echo "Running some pre-requisite steps to generate .fai and .dict files, as for GATK realignment steps we need them."
	# to generate some required files
	samtools faidx "$ref"

	samtools dict "$ref" -o "${project_dir}/$_sm.dict"
	# index to use below later
	samtools index "${project_dir}/lane_sorted.bam"

        [ "$v" -eq 1 ] && echo "Successfully generated .dict and .fai files for use in realignment steps next.";

	# if realign given
	if [ "$realign" -eq 1 ];then	
		#Creating intervals file.
		if [ -e "${project_dir}/lane.intervals" ];then
			echo "The .intervals file exists in the project directory. Do you wish to overwrite? (Y/n) : "
			read -r user_input
        	else
                	user_input="Y"
        	fi

		if [ "$user_input" == "n" ];then
                	echo "Using the existing file";
        	elif [ "$user_input" == "Y" ];then
                	["$v" -eq 1 ] && echo "Initiating..........Running the realignment steps with the raw gapped alignment to generate instervals.";
			# now running the gatk steps
			java -Xmx2g -jar "${project_dir}/GenomeAnalysisTK.jar" -T RealignerTargetCreator -R "$ref" -I "${project_dir}/lane_sorted.bam" -o "${project_dir}/lane.intervals" --known "$millsFile"
			# if done success then
			["$v" -eq 1 ] && echo "Successfully performed the steps to generate .intervals file."		
		else
                	echo "Wrong input = \$user_input given. Exiting now......"; exit 1;
		fi

		#Creating realigned file.
		if [ -e "${project_dir}/lane_realigned.bam" ];then
			echo "The xyz_realigned.bam already exists in the directory. Do you wish to overwrite? (Y/n) : "
			read -r user_input
                else
                        user_input="Y"
                fi

		if [ "$user_input" == "n" ];then
			echo "Using the existing file.";
                elif [ "$user_input" == "Y" ];then
			["$v" -eq 1 ] && echo "Running the realignment steps for now. This requires .intervals file from previous steps.";
			# now running the indel realignment steps
			##
			java -Xmx4g -jar "${project_dir}/GenomeAnalysisTK.jar" -T IndelRealigner -R "$ref" -I "${project_dir}/lane_sorted.bam" -targetIntervals "${project_dir}/lane.intervals" -known "$millsFile" -o "${project_dir}/lane_realigned.bam"
			# if successful then
			["$v" -eq 1 ] && echo "Successfully completed the realignment steps for now.";
		else
                        echo "Wrong input = \$user_input given. Exiting now......"; exit 1;
		fi
		# realign_file variable to be used below
		realign_file="${project_dir}/lane_realigned.bam"
	else
		realign_file="${project_dir}/lane_sorted.bam"

	fi		
	
	# recalibration steps. Commenting them out as it almost crashed my system when i first try to execute them. Less compute power.
	#if [ -e "${project_dir}/lane_recal.table}" ];then
	#	echo "The xyz_recal.table already exists in the directory. Skipping this step."
	#else
	#	echo "Running the recalibration steps to reduce the effects of analysis artefacts produced by the sequencing machines."
	#	java -Xmx4g -jar "${toolkit_dir}/GenomeAnalysisTK.jar" -T BaseRecalibrator -R "$ref" -knownSites "${project_dir}/dbsnp_142.b38.vcf" -I <lane.bam> -o <lane_recal.table>
	#	java -Xmx2g -jar GenomeAnalysisTK.jar -T PrintReads -R <ref.fa> -I <lane.bam> --BSQR <lane_recal.table> -o <lane_recal.bam>
	#	echo "Successfully generated recalibrated .bam file"
	#fi
	
	if [ "$index" -eq 1 ];then
		#
        	[ "$v" -eq 1 ] && echo "Intialising.......Running the indexing steps for realigned .bam file";
		samtools index "${project_dir}/${realign_file}"; 
		[ "$v" -eq 1 ] && echo "Successfully indexed the realigned .bam file";
	fi

	return 0
}	

function variant_calling () {
	#to do variant calling
	if [ "$answer" == "n" ];then
                echo "Skipping the reads mapping steps....";
                return 1
        fi

	[ "$v" -eq 1 ] && echo "Initiating..... Running the final variant calling steps to generate the .vcf files"; echo "Intiating steps required to convert the BAM file into genomic positions using mpileup, resulting in .bcf file containing all of locations of genome.";
	
	[ "$realign" -eq 1 ] && echo "Realignment was done. Taking xyz_realigned.bam file"; realign_file="${project_dir}/lane_realigned.bam" || echo "Realignment not done."; realign_file="${project_dir}/lane_sorted.bam"

	# check verbose mode
	[ "$v" -eq 1 ] && echo "Running variant calling";
	if [ "$gunzip" -eq 1 ];then
		bcftools mpileup -Ob -o "${project_dir}/genome_location.bcf" -f "$ref" "${realign_file}"; 
		bcftools call -vmO z -o "${output}.vcf.gz" "${project_dir}/genome_location.bcf";	
	else
		[ "$v" -eq 1 ] && echo "User has requested to save the file in .vcf format";
		bcftools mpileup -Ob -o "${project_dir}/genome_location.bcf" -f "$ref" "${realign_file}";
		bcftools call -vmO v -o "${output}.vcf" "${project_dir}/genome_location.bcf";
	fi

	[ "$v" -eq 1 ] && echo "Successfully generated ${output}.vcf files. User can now analyse their results."; echo "Viola !!";
	# did not executed these steps as it was optional
	#tabix -p vcf <study.vcf.gz>
	#bcftools filter -O z -o <study_filtered..vcf.gz> -s LOWQUAL -i'%QUAL>10' <study.vcf.gz>
	echo "Viola !!"
	return 0
}

function vcf_to_bed () {
	#method to convert .vcf file to .bed file format and also generate snps.txt and indels.txt
	echo "Initiating........conversion of vcf file to bed file format";  
	read -p "Please provide a standard .vcf file for conversion: " vcf_file
	#echo "${vcf_file##*.}"
	if [ "${vcf_file##*.}" == "vcf" ]
	then
		:
	else
                echo " .vcf file not provided. Exiting for now."
                return 1
	fi

	if [ -f "$vcf_file" ];then
		echo "Converting ${vcf_file} to BED format........."
		fl=${vcf_file%.*}
		cat "$vcf_file" | sed '/^#/d' | awk '{print $1,$2,$4,$5}' | awk '{gsub(/[^[:digit:]]/, "", $1)}1' | awk '{print $1"\t"$2"\t"$2+length($4)-length($3)"\t"length($4)-length($3)}' > ${fl}.bed
		echo "generating snps.txt file....."
		cat "$vcf_file" | sed '/^#/d' | grep -v "INDEL" | awk '{print $1,$2,$4,$5}' | awk '{gsub(/[^[:digit:]]/, "", $1)}1' | awk '{print $1"\t"$2"\t"$2+length($4)-length($3)"\t"length($4)-length($3)}' > snps.txt
		cat "$vcf_file" | sed '/^#/d' | grep "INDEL" | awk '{print $1,$2,$4,$5}' | awk '{gsub(/[^[:digit:]]/, "", $1)}1' | awk '{print $1"\t"$2"\t"$2+length($4)-length($3)"\t"length($4)-length($3)}' > indels.txt
		echo "Summary files successfully generated for the project."
	else
		echo "The ${vcf_file} file not found. Exiting for now."
		return 1
	fi

	return 0
}

main() {
	
	# call every method stepwise
	get_user_input "$@"
	# check if files exist
	verify_files "$v" "$reads1" "$reads2" "$ref" "$millsFile" "$output"
	
	project_essentials "$v" "$ref"
      		
	reads_mapping "$v" "$answer" "$ref" "$reads1" "$reads2" "$tmp_dir"
	
	run_improvement "$v" "$answer" "$ref" "$project_dir" "$_sm" "$realign" "$millsFile" "$index"
	
	variant_calling "$v" "$answer" "$realign" "$gunzip" "$output" "$v" "$ref" "$project_dir"
	
	vcf_to_bed # add args here
}

# call function
main "$@"

