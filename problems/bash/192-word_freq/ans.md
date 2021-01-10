sed 's/[ \t]\+/\n/g' test01.txt | sort -r | uniq -c | awk '{print $2, $1}'

## incorrect
cat test02.txt | tr "[ \t]+" '\n' | sort -r | uniq -c


sed 's/[ \t]\+/\n/g' words.txt | sort -r | uniq -c | awk '{print $2, $1}'

a  a   b

# Read from the file words.txt and output the word frequency list to stdout.
sed 's/[ \t]\+/\n/g' words.txt | sed '/^$/d' | sort | uniq -c | sort -nr | awk '{print $2, $1}'

sed 's/^ \+//;s/ \+$//;s/ \+/\n/g' test04.txt | sort | uniq -c | sort -nr | awk '{print $2,$1}'
sed 's/^ \+//;s/ \+$//;s/ \+/\n/g' words.txt | sort | uniq -c | sort -r | awk '{print $2,$1}'
