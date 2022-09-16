#!/bin/bash -l
while [ $# -gt 0 ]; do
      case "$1" in
        --file_names=*)
            file_names="${1#*=}"
        ;;
        --type=*)
            file_type="${1#*=}"
        ;;
        *)
            printf "***************************\n"
            printf "* Error: Invalid argument.*\n"
            printf "***************************\n"
            exit 1
    esac
    shift
    done

NUMBER_TASK=`grep -c '^[^#]' $file_names`
#echo "$NUMBER_TASK"
#infile=$(sed -n -e "$SGE_TASK_ID p" $file_names)

#./myprog < $infile
i=0
while read LINE;
do
    
        filename=`grep -oP '(\/((?!\/).)*\.)' <<< "$LINE"`
        printf "$LINE\n" 
        printf "emb/${file_type}${filename}emb\n"
        embed_names="emb/${file_type}${new_filename}emb\n"
        qsub -N creating_embs_$i create_embs_3.sh $filename $embed_names
        ((i=i+1))
done<$file_names
#qsub -t 1-$NUMBER_TASK -tc 5 create_embs_3.sh $infile $new_filename
