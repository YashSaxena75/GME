 #hey
if [ "$1" == "" ]
then
echo "Usage: ./ping.sh [network]"
echo "Example: ./ping.sh 10.100.11"
else
for x in  `seq 230 254`;do
ping -c 1 $1.$x |grep "64 bytes" 
done
fi
