
echo $1
if [ ! -f $1 ];then
    cp template.py $1
fi
code $1
