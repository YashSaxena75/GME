 #hey
if [ "$1" == "" ]
then
echo "Usage: rmdir [PATH]"
echo "Example: rmdir ./root/Desktop/new"
else
for x in  `seq 1 255`;do
rmdir /root/Desktop/new $1.$x  
done
fi
