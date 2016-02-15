#!/usr/bin/awk -f
# Collect the tranlations from the first file.
NR==FNR { repl[$1]=$2; next }

# Step through the input file, replacing as required.
{
for ( string in repl ) {
sub(string, repl[string])
}
if [string -eq NULL] ; then
echo "translation incomplete"
}
#if string is null-character,then we have to add rules,
#if repl[string] is null-character,then we have to delete rules or put # in front of all lines until we reach </rules> also
# And print.
1

#run this script as $ ./bash_script.sh input_chk.txt circos.conf