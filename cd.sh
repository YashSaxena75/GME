 #hey
if [ "$1" == "" ]
then
echo "Usage: ./cd.sh [path]"
echo "Example: ./ping.sh mkdir /root/Desktop/new"
else
for x in  `seq 1 255 `;do
mkdir /root/Desktop/new $1.$x 
done
fi
